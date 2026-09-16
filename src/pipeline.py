# src/pipeline.py
import json
import os
from datetime import datetime

from src.extractors import (
    mcp,
    models,
    repositories,
    news,
    companies,
    tools,
    videos,
    robots,
    devices,
    tasks,
    collections,
    personal,
    creative,
    new_entities,
)
from src.deduplicator import deduplicate
from src.validator import validate_all
from src.relationship_mapper import build_relationships

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../data/ingestion")

def run() -> dict:
    """Execute the full AIOrbit ecosystem data ingestion pipeline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_raw_entities = []
    stats_by_type = {}

    extractors = [
        ("mcp",        mcp.extract,          {"limit": 35}),
        ("model",      models.extract,        {}),
        ("company",    companies.extract,     {}),
        ("tool",       tools.extract,         {}),
        ("repository", repositories.extract,  {}),
        ("news",       news.extract,          {}),
        ("video",      videos.extract,        {}),
        ("robot",      robots.extract,        {}),
        ("device",     devices.extract,       {}),
        ("task",       tasks.extract,         {}),
        ("collection", collections.extract,   {}),
        ("personal",   personal.extract,      {}),
        ("creative",   creative.extract,      {}),
        ("new",        new_entities.extract,  {}),
    ]

    print("=" * 60)
    print("AIOrbit Ecosystem Data Ingestion Pipeline Starting...")
    print("=" * 60)

    for entity_type, extractor_fn, kwargs in extractors:
        try:
            print(f"[*] Extracting domain: {entity_type}...")
            records = extractor_fn(**kwargs)
            validated_records = validate_all(records, entity_type)
            all_raw_entities.extend(validated_records)
            stats_by_type[entity_type] = len(validated_records)
            print(f"    -> Extracted {len(validated_records)} validated {entity_type} records")
        except Exception as e:
            print(f"    [!] Error extracting {entity_type}: {e}")
            stats_by_type[entity_type] = 0

    print("\n[*] Performing cross-domain deduplication and canonicalization...")
    unique_entities = deduplicate(all_raw_entities)
    dedup_count = len(all_raw_entities) - len(unique_entities)
    print(f"    -> Total raw records: {len(all_raw_entities)}, Unique after dedup: {len(unique_entities)} (Removed {dedup_count} duplicates)")

    print("\n[*] Generating multi-domain ecosystem relationship graph...")
    relationships_data = build_relationships(unique_entities)
    total_rels = relationships_data["metadata"]["total_relationships"]
    print(f"    -> Generated {total_rels} relationships across {len(relationships_data['metadata']['predicates_used'])} predicates")

    # Output paths
    entities_path = os.path.join(OUTPUT_DIR, "entities.json")
    relationships_path = os.path.join(OUTPUT_DIR, "relationships.json")
    summary_path = os.path.join(OUTPUT_DIR, "summary.json")

    # Save entities.json
    with open(entities_path, "w", encoding="utf-8") as f:
        json.dump(unique_entities, f, indent=2, ensure_ascii=False)
    print(f"[*] Saved entities to: {entities_path}")

    # Save relationships.json
    with open(relationships_path, "w", encoding="utf-8") as f:
        json.dump(relationships_data, f, indent=2, ensure_ascii=False)
    print(f"[*] Saved relationships to: {relationships_path}")

    # Save summary.json
    summary = {
        "run_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_entities": len(unique_entities),
        "total_relationships": total_rels,
        "by_type": stats_by_type,
        "predicates": relationships_data["metadata"]["predicates_used"],
        "outputs": {
            "entities": entities_path,
            "relationships": relationships_path,
            "summary": summary_path,
        }
    }
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"[*] Saved pipeline run summary to: {summary_path}")

    print("\n" + "=" * 60)
    print(f"PIPELINE RUN COMPLETE: {len(unique_entities)} entities | {total_rels} relationships")
    print("=" * 60)

    return summary
