#!/usr/bin/env python3
"""
scripts/ingest_creati.py
========================
Discovers, fetches, cleans, enriches, and merges MCP Servers and Clients from Creati.ai
into the AIOrbit final dataset, expanding the collection toward ~10,000 verified records.
"""

import urllib.request
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../data/cache/creati")
SEARCH_INDEX_URL = "https://cdn-image.creati.ai/mcp/json/search/v3/mcp-search.json"
DETAIL_URL_TEMPLATE = "https://cdn-image.creati.ai/mcp/json/details/v3/{handle}.json"

os.makedirs(CACHE_DIR, exist_ok=True)
CACHE_FILE = os.path.join(CACHE_DIR, "creati_details.jsonl")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

def download_search_index():
    """Fetch the search index listing all products."""
    index_path = os.path.join(CACHE_DIR, "mcp-search.json")
    if os.path.exists(index_path) and os.path.getsize(index_path) > 100000:
        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f).get("products", [])
    
    print("[creati] Fetching search index from CDN...")
    req = urllib.request.Request(SEARCH_INDEX_URL, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    
    return data.get("products", [])

def load_cached_details():
    """Load already downloaded product details from cache."""
    cached = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    h = item.get("h") or (item.get("en", {}).get("handle"))
                    if h:
                        cached[h] = item
    return cached

def fetch_single(product):
    """Worker function to fetch details for a single product."""
    h = product["h"]
    url = DETAIL_URL_TEMPLATE.format(handle=h)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            data["h"] = h
            return h, data
    except Exception as e:
        return h, None

def fetch_all_details(products, cached, max_workers=25):
    """Fetch all details with multi-threading and append to cache."""
    to_fetch = [p for p in products if p["h"] not in cached]
    print(f"[creati] Total items: {len(products)} | Already cached: {len(cached)} | To fetch: {len(to_fetch)}")
    
    if not to_fetch:
        return cached

    success_count = 0
    fail_count = 0
    start_time = time.time()
    
    with open(CACHE_FILE, "a", encoding="utf-8") as out_f:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_h = {executor.submit(fetch_single, p): p["h"] for p in to_fetch}
            
            for i, future in enumerate(as_completed(future_to_h)):
                h, data = future.result()
                if data and data.get("en"):
                    cached[h] = data
                    out_f.write(json.dumps(data, ensure_ascii=False) + "\n")
                    success_count += 1
                else:
                    fail_count += 1
                
                if (i + 1) % 500 == 0 or (i + 1) == len(to_fetch):
                    elapsed = time.time() - start_time
                    rate = (i + 1) / elapsed if elapsed > 0 else 0
                    print(f"[creati] Progress: {i + 1}/{len(to_fetch)} ({rate:.1f} req/s) | Success: {success_count} | Failed: {fail_count}")
                    out_f.flush()

    return cached

if __name__ == "__main__":
    products = download_search_index()
    print(f"Products in index: {len(products)}")
    cached = load_cached_details()
    print(f"Already cached: {len(cached)}")
    all_details = fetch_all_details(products, cached, max_workers=30)
    print(f"Total details in cache: {len(all_details)}")
