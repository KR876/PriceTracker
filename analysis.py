import sys
import io
import sqlite3
import pandas as pd
from category_map import CATEGORY_MAP

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

conn = sqlite3.connect('prices.db')
df = pd.read_sql_query('''
    SELECT p.store, p.category, p.name, pr.price
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
''', conn)
conn.close()

STORES = ['rimi', 'selver', 'prisma', 'barbora']

rows = []
for cat_name, store_cats in CATEGORY_MAP.items():
    store_data = {}
    for store in STORES:
        if store not in store_cats:
            continue
        ids = store_cats[store]
        sub = df[(df['store'] == store) & (df['category'].isin(ids))]
        if not sub.empty:
            store_data[store] = sub

    # Skip if fewer than 2 stores have data
    if len(store_data) < 2:
        continue

    row = {'Kategooria': cat_name}
    for store in STORES:
        if store in store_data:
            row[f'{store}_avg'] = round(store_data[store]['price'].mean(), 2)
            row[f'{store}_count'] = len(store_data[store])
        else:
            row[f'{store}_avg'] = None
            row[f'{store}_count'] = 0
    rows.append(row)

results = pd.DataFrame(rows).sort_values('Kategooria')

# Per-category comparison table
print("=" * 85)
print("HINNAVÕRDLUS — RIMI vs SELVER vs PRISMA")
print("=" * 85)
print(f"{'Kategooria':<35} {'Rimi':>8} {'Selver':>8} {'Prisma':>8}  Odavam")
print("-" * 85)

for _, row in results.iterrows():
    avgs = {s: row[f'{s}_avg'] for s in STORES if pd.notna(row[f'{s}_avg'])}
    if not avgs:
        continue
    cheapest = min(avgs, key=avgs.get)
    rimi   = f"{row['rimi_avg']:.2f}"   if pd.notna(row['rimi_avg'])   else "  N/A"
    selver = f"{row['selver_avg']:.2f}" if pd.notna(row['selver_avg']) else "  N/A"
    prisma = f"{row['prisma_avg']:.2f}" if pd.notna(row['prisma_avg']) else "  N/A"
    barbora = f"{row['barbora_avg']:.2f}" if pd.notna(row['barbora_avg']) else "  N/A"
    print(f"{row['Kategooria']:<35} {rimi:>8} {selver:>8} {prisma:>8}  {cheapest.capitalize()}")

# Overall summary
print("\n" + "=" * 85)
print("KOKKUVÕTE — KESKMINE HIND KÕIGIS KATEGOORIATES")
print("=" * 85)

for store in STORES:
    col = f'{store}_avg'
    valid = results[col].dropna()
    if valid.empty:
        continue
    wins = 0
    for _, row in results.iterrows():
        avgs = {s: row[f'{s}_avg'] for s in STORES if pd.notna(row[f'{s}_avg'])}
        if avgs and min(avgs, key=avgs.get) == store:
            wins += 1
    print(f"{store.capitalize():<10} keskmine kategooria hind: {valid.mean():.2f} EUR  |  odavam {wins} kategoorias")