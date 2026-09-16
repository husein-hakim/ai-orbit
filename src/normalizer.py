# src/normalizer.py
import uuid
import re
from datetime import datetime

TODAY = datetime.utcnow().strftime("%Y-%m-%d")

def make_id(entity_type: str, name: str) -> str:
    """Generate stable deterministic UUID from entity type and name."""
    key = f"{entity_type.lower().strip()}:{name.lower().strip()}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

def clean_text(text: str) -> str:
    """Remove HTML tags, markdown links, code spans, and normalize whitespace."""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'`+([^`]*)`+', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Normalize ending punctuation
    if text and not text.endswith(('.', '!', '?')):
        text += '.'
    return text

def normalize(raw: dict, entity_type: str, source_name: str, source_url: str) -> dict:
    """
    Normalize any raw entity dict into the standard common schema with specialized metadata.
    """
    name = raw.get("name", "Unknown").strip()
    desc = clean_text(raw.get("description", ""))
    url = raw.get("url", "").strip().rstrip("/")
    
    # Ensure categories is a clean list
    categories = raw.get("categories", [entity_type])
    if isinstance(categories, str):
        categories = [c.strip() for c in categories.split(",") if c.strip()]
    elif not isinstance(categories, list):
        categories = [entity_type]
    if entity_type not in categories:
        categories.insert(0, entity_type)

    base = {
        "id": make_id(entity_type, name),
        "entity_type": entity_type,
        "name": name,
        "description": desc if desc else f"{name} is an AI {entity_type} in the global AI ecosystem.",
        "url": url,
        "categories": categories,
        "source": {
            "name": source_name,
            "url": source_url
        },
        "ingested_at": TODAY,
    }
    
    # Merge any specialized domain-specific fields from raw
    specialized_keys = set(raw.keys()) - {"name", "description", "url", "categories", "id", "entity_type", "source", "ingested_at"}
    for k in specialized_keys:
        base[k] = raw[k]
    
    return base
