#!/usr/bin/env python3
"""
AIOrbit Ecosystem Data Ingestion Pipeline
=========================================
Aggregates, normalizes, deduplicates, and maps relationships across
the 14 key domains of the global AI ecosystem:
Tools, Tasks, Companies, News, Videos, Robots, Devices, Models,
Repositories, MCP Servers, Collections, Personal AI, Creative Tools,
and Recent Launches.

Usage:
    python3 run.py
"""
import sys
import os

# Ensure local src directory is on import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.pipeline import run

if __name__ == "__main__":
    summary = run()
    print("\n=== FINAL BREAKDOWN BY DOMAIN ===")
    for entity_type, count in summary["by_type"].items():
        print(f"  {entity_type:20}: {count:4d} entities")
    print("-" * 40)
    print(f"  {'TOTAL UNIQUE ENTITIES':20}: {summary['total_entities']:4d}")
    print(f"  {'TOTAL RELATIONSHIPS':20}: {summary['total_relationships']:4d}")
    print("=" * 40)
