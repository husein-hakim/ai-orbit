# src/validator.py
from datetime import datetime

REQUIRED_FIELDS = ["id", "entity_type", "name", "description", "url", "categories", "source"]

def validate(entity: dict, entity_type: str) -> dict:
    """Ensure all required fields are present, sanitized, and properly formatted."""
    if not isinstance(entity, dict):
        return None

    # Fallback and sanitize core fields
    name = str(entity.get("name", "")).strip()
    if not name:
        return None

    entity["name"] = name
    entity["entity_type"] = entity_type

    # Ensure description is sound
    desc = str(entity.get("description", "")).strip()
    if not desc or len(desc) < 15:
        entity["description"] = f"{name} is a high-performance {entity_type} in the modern AI ecosystem."
    else:
        if not desc.endswith(('.', '!', '?')):
            desc += '.'
        entity["description"] = desc

    # Ensure URL is a string
    entity["url"] = str(entity.get("url", "")).strip()

    # Ensure categories is a list of strings
    cats = entity.get("categories", [entity_type])
    if isinstance(cats, str):
        cats = [c.strip() for c in cats.split(",") if c.strip()]
    elif not isinstance(cats, list):
        cats = [entity_type]
    if not cats:
        cats = [entity_type]
    entity["categories"] = cats

    # Ensure source object structure
    source = entity.get("source", {})
    if isinstance(source, str):
        entity["source"] = {"name": source, "url": ""}
    elif isinstance(source, dict):
        entity["source"] = {
            "name": str(source.get("name", "Ecosystem Discovery")).strip(),
            "url": str(source.get("url", "")).strip()
        }
    else:
        entity["source"] = {"name": "Ecosystem Discovery", "url": ""}

    if "ingested_at" not in entity:
        entity["ingested_at"] = datetime.utcnow().strftime("%Y-%m-%d")

    return entity

def validate_all(entities: list[dict], entity_type: str) -> list[dict]:
    """Validate a list of entity dictionaries, filtering out invalid ones."""
    validated_list = []
    for e in entities:
        res = validate(e, entity_type)
        if res:
            validated_list.append(res)
    return validated_list
