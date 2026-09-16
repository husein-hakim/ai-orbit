# src/deduplicator.py
import re

def normalize_name(name: str) -> str:
    """Canonicalize entity name for deduplication."""
    name = re.sub(r'\s+', ' ', name.lower().strip())
    name = re.sub(r'[\-_/]', ' ', name)
    return re.sub(r'\s+', ' ', name).strip()

def normalize_url(url: str) -> str:
    """Canonicalize URL format."""
    if not url:
        return ""
    url = url.lower().strip().rstrip('/').replace('http://', 'https://')
    return url

def deduplicate(entities: list[dict]) -> list[dict]:
    """
    Deduplicate entities based on stable UUID, domain-specific canonical name,
    and non-generic URLs within the same domain.
    """
    seen_ids = set()
    seen_type_names = set()
    seen_type_urls = set()
    unique_entities = []

    # Generic URLs that multiple distinct entities can share
    GENERIC_URLS = {
        "https://github.com",
        "https://huggingface.co",
        "https://huggingface.co/models",
        "https://openai.com",
        "https://anthropic.com",
        "https://google.com",
        "https://microsoft.com",
        "https://techcrunch.com",
        "https://venturebeat.com",
        "https://theverge.com",
        "https://aiorbit.com",
        "https://aiorbit.com/tasks"
    }

    for e in entities:
        eid = e.get("id", "")
        etype = e.get("entity_type", "")
        raw_name = e.get("name", "")
        norm_name = normalize_name(raw_name)
        raw_url = e.get("url", "")
        norm_url = normalize_url(raw_url)

        type_name_key = f"{etype}:{norm_name}"
        type_url_key = f"{etype}:{norm_url}"

        if eid in seen_ids:
            continue
        if type_name_key in seen_type_names:
            continue
        if norm_url and norm_url not in GENERIC_URLS and type_url_key in seen_type_urls:
            continue

        seen_ids.add(eid)
        if norm_name:
            seen_type_names.add(type_name_key)
        if norm_url and norm_url not in GENERIC_URLS:
            seen_type_urls.add(type_url_key)

        unique_entities.append(e)

    return unique_entities
