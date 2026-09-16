#!/usr/bin/env python3
"""
Final grammar normalization for all descriptions.
Converts the awkward 'X is an MCP server that [raw excerpt]' format
into a clean, professional 2-3 sentence description.
"""
import csv, re, json

with open('data/final/mcp_dataset.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

HEADERS = list(rows[0].keys())
fixes = 0

for r in rows:
    desc = r.get('description', '')
    original = desc

    # ── Pattern 1: "X is an MCP server that [raw excerpt starting with uppercase]"
    # When the excerpt starts with uppercase, it reads as a new sentence fragment.
    # Fix: normalise to proper sentence.
    # e.g. "Foo is an MCP server that Foo Bar for doing X" → "Foo is an MCP server for doing X"
    m = re.match(r'^(.+? is an MCP server) that ([A-Z][^a-z]{0,4}[A-Z].{0,40}) that (.+)$', desc)
    if m:
        desc = f"{m.group(1)} that {m.group(3)}"

    # ── Pattern 2: "X is an MCP server that An MCP server ..."
    desc = re.sub(r'is an MCP server that [Aa]n MCP [Ss]erver\s+(for|to|that|which)?\s*', 'is an MCP server that ', desc)

    # ── Pattern 3: Remaining double 'that'
    desc = re.sub(r'\bthat\s+that\b', 'that', desc, flags=re.IGNORECASE)

    # ── Pattern 4: "X is an MCP server that [UPPERCASE_WORD] that"
    # e.g. "X is an MCP server that Critical Rules that..."
    desc = re.sub(r'(is an MCP server that )[A-Z][A-Za-z\s]{1,25} that ', r'\1', desc)

    # ── Pattern 5: "X is an MCP server that version that" etc.
    desc = re.sub(r'(is an MCP server that \w+) that ', r'\1 — ', desc)

    # ── Pattern 6: Clean up multiple dashes
    desc = re.sub(r'\s*—\s*—\s*', ' — ', desc)

    # ── General cleanup
    desc = re.sub(r'\s{2,}', ' ', desc).strip()
    if desc and not desc.endswith(('.', '!', '?')):
        desc += '.'

    if desc != original:
        r['description'] = desc
        fixes += 1

print(f'Grammar normalizations applied: {fixes}')

# Spot check remaining issues
remaining_double_that = sum(1 for r in rows if re.search(r'\bthat\s+\bthat\b', r['description'], re.I))
awkward = [r for r in rows if re.search(r'is an MCP server that [A-Z][^a-z]{0,5}[A-Z].{0,30} that', r['description'])]
print(f'Remaining double-that: {remaining_double_that}')
print(f'Remaining Title-case-that pattern: {len(awkward)}')

# Sample 8 descriptions now
import random; random.seed(77)
for r in random.sample(rows, 8):
    print(f'[{r["mcp_name"]}] {r["description"][:200]}')
    print()

# Save all formats
with open('data/final/mcp_dataset.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

with open('data/final/mcp_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)

with open('data/final/mcp_dataset.csv', 'r', encoding='utf-8') as fin, \
     open('data/final/mcp_dataset.tsv', 'w', encoding='utf-8') as fout:
    for row_data in csv.reader(fin):
        fout.write('\t'.join(row_data) + '\n')

print('✅ Saved CSV, JSON, TSV.')
