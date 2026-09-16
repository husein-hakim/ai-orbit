#!/usr/bin/env python3
"""
Google Sheets Upload Helper
============================
Generates a tab-separated file optimized for Google Sheets import,
and provides instructions for creating a public Google Sheet.
"""

import csv
import json
import os
import sys


def csv_to_tsv(csv_path: str, tsv_path: str) -> None:
    """Convert CSV to TSV for easy Google Sheets paste."""
    with open(csv_path, "r", encoding="utf-8") as fin:
        reader = csv.reader(fin)
        with open(tsv_path, "w", encoding="utf-8") as fout:
            for row in reader:
                fout.write("\t".join(row) + "\n")
    print(f"✅ TSV file created: {tsv_path}")


def generate_sheet_instructions():
    """Print instructions for creating the Google Sheet."""
    instructions = """
╔══════════════════════════════════════════════════════════════════╗
║        Google Sheets Upload Instructions                        ║
╚══════════════════════════════════════════════════════════════════╝

OPTION 1: Import CSV directly
─────────────────────────────
1. Open Google Sheets: https://sheets.google.com
2. Create a new spreadsheet
3. Go to File → Import → Upload
4. Upload the file: data/final/mcp_dataset.csv
5. Select "Replace spreadsheet" and "Detect automatically"
6. Click Import

OPTION 2: Copy-paste TSV
─────────────────────────
1. Open Google Sheets: https://sheets.google.com
2. Create a new spreadsheet
3. Open data/final/mcp_dataset.tsv in a text editor
4. Select all (Cmd+A), Copy (Cmd+C)
5. Paste into cell A1 in Google Sheets
6. Data → Split text to columns → Tab separator

AFTER IMPORT - Make it Public:
──────────────────────────────
1. Click "Share" (top right)
2. Under "General access", change to "Anyone with the link"
3. Set permission to "Viewer"
4. Copy the link

FORMATTING TIPS:
────────────────
1. Select Row 1 → Format → Bold
2. Select Row 1 → View → Freeze → 1 row
3. Auto-resize columns: Select all → Format → Column width → Fit to data
4. Add filters: Data → Create a filter
5. Name the sheet: "MCP Dataset - AIOrbit"

    """
    print(instructions)


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    final_dir = os.path.join(base_dir, "data", "final")

    csv_path = os.path.join(final_dir, "mcp_dataset.csv")
    tsv_path = os.path.join(final_dir, "mcp_dataset.tsv")

    if not os.path.exists(csv_path):
        print("❌ CSV file not found. Run extract_mcp_data.py first.")
        sys.exit(1)

    csv_to_tsv(csv_path, tsv_path)
    generate_sheet_instructions()

    # Also print a count
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        count = sum(1 for _ in reader)
    print(f"📊 Total records ready for upload: {count}")


if __name__ == "__main__":
    main()
