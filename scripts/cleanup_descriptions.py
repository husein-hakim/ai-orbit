#!/usr/bin/env python3
"""Final pass: fix remaining edge-case markdown in descriptions."""
import csv, re, json

with open('data/final/mcp_dataset.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

HEADERS = list(rows[0].keys())
cleaned = 0

for r in rows:
    desc = r.get('description', '')
    original = desc

    # Pattern: [Text]( with no URL — just remove the brackets leaving text
    desc = re.sub(r'\[([^\]]+)\]\(\s*\)', r'\1', desc)
    # Pattern: [Text](partial or empty
    desc = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', desc)
    # Any remaining [Text]( fragments
    desc = re.sub(r'\[([^\]]+)\]\(', r'\1 (', desc)
    desc = re.sub(r'\]\(', ' ', desc)

    # Backticks at start of words (npx -y pkg` → npx -y pkg)
    desc = re.sub(r'`+', '', desc)

    # Remove tool-call style artifacts: ($0.001), ($0.005) etc
    desc = re.sub(r'\(\$[\d.]+\)', '', desc)
    # Remove empty parentheses
    desc = re.sub(r'\(\s*\)', '', desc)
    # Remove repeated commas
    desc = re.sub(r',\s*,', ',', desc)

    # Collapse spaces
    desc = re.sub(r'\s{2,}', ' ', desc).strip()
    # Remove trailing lone commas or dashes
    desc = re.sub(r'[,\-]\s*$', '.', desc)
    desc = re.sub(r'\.\s*\.\s*$', '.', desc)

    # Ensure ends with .
    if desc and not desc.endswith(('.', '!', '?')):
        desc += '.'

    if desc:
        desc = desc[0].upper() + desc[1:]

    if desc != original:
        r['description'] = desc
        cleaned += 1

print(f'Additional descriptions cleaned: {cleaned}')

md_links = sum(1 for r in rows if '](' in r.get('description', ''))
backticks = sum(1 for r in rows if '`' in r.get('description', ''))
print(f'Remaining ]( : {md_links}')
print(f'Remaining ` : {backticks}')

# Duplicate check
names = [r['mcp_name'].lower().strip() for r in rows]
urls = [r['github_url'].lower().strip().rstrip('/') for r in rows]
print(f'Duplicate names: {len(names) - len(set(names))}')
print(f'Duplicate URLs: {len(urls) - len(set(urls))}')

# Save
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

print(f'\nTotal records: {len(rows)} | Columns: {len(HEADERS)}')
print('✅ Final cleanup complete.')
