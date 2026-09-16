# src/extractors/mcp.py
import csv
import os
from src.normalizer import normalize

CSV_PATH = os.path.join(os.path.dirname(__file__), "../../data/final/mcp_dataset.csv")

def extract(limit: int = 35) -> list[dict]:
    """
    Load representative top MCP records from the completed 3,844-record dataset.
    Returns the top `limit` records ranked by quality_score.
    """
    if not os.path.exists(CSV_PATH):
        print(f"[mcp] CSV file not found at {CSV_PATH}")
        return []

    rows = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    # Sort descending by quality_score
    rows.sort(key=lambda r: int(r.get("quality_score", 0)), reverse=True)
    top_rows = rows[:limit]

    entities = []
    for row in top_rows:
        clients_str = row.get("supported_ai_clients", "")
        clients_list = [c.strip() for c in clients_str.split(",") if c.strip()]
        
        lang = str(row.get("programming_language", "")).lower()
        if "typescript" in lang or "javascript" in lang or "node" in lang:
            install_method = "npx"
        elif "python" in lang:
            install_method = "pip"
        elif "go" in lang or "rust" in lang:
            install_method = "binary"
        elif "docker" in lang:
            install_method = "docker"
        else:
            install_method = "npx"

        entity = normalize(
            raw={
                "name": row["mcp_name"],
                "description": row["description"],
                "url": row.get("official_website") or row.get("github_url"),
                "categories": [row.get("category", "Developer Tools"), row.get("subcategory", "General")],
                # Specialized MCP metadata fields
                "mcp_type": row.get("type", "Server"),
                "transport": row.get("mcp_transport", "stdio"),
                "supported_clients": clients_list if clients_list else ["Claude Desktop", "Cursor"],
                "install_method": install_method,
                "quality_score": int(row.get("quality_score", 70)),
                "is_official": str(row.get("is_official", "False")).lower() in ("true", "1", "yes"),
                "github_url": row.get("github_url", ""),
            },
            entity_type="mcp",
            source_name=row.get("discovery_source", "awesome-mcp-servers"),
            source_url="https://github.com/punkpeye/awesome-mcp-servers",
        )
        entities.append(entity)

    return entities
