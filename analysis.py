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

stores = ['rimi', 'selver']

print("=" * 80)
print("HINNAVÕRDLUS KATEGOORIATE KAUPA — RIMI vs SELVER")
print("=" * 80)

rows = []
for cat_name, store_cats in CATEGORY_MAP.items():
    store_data = {}
    valid = True
    for store in stores:
        if store not in store_cats:
            valid = False
            break
        ids = store_cats[store]
        sub = df[(df['store'] == store) & (df['category'].isin(ids))]
        if sub.empty:
            valid = False
            break
        store_data[store] = sub

    if not valid:
        continue

    rimi_df = store_data['rimi']
    selver_df = store_data['selver']

    rimi_avg = rimi_df['price'].mean()
    selver_avg = selver_df['price'].mean()
    diff = selver_avg - rimi_avg
    cheaper = 'Rimi' if diff > 0 else 'Selver'

    rows.append({
        'Kategooria': cat_name,
        'Rimi kesk.': round(rimi_avg, 2),
        'Selver kesk.': round(selver_avg, 2),
        'Vahe': round(diff, 2),
        'Odavam': cheaper,
        'Rimi tooteid': len(rimi_df),
        'Selver tooteid': len(selver_df),
    })

results = pd.DataFrame(rows)

# Üldine kokkuvõte
print(f"\n{'Kategooria':<35} {'Rimi':>8} {'Selver':>8} {'Vahe':>8} {'Odavam':<10}")
print("-" * 75)
for _, row in results.sort_values('Kategooria').iterrows():
    print(f"{row['Kategooria']:<35} {row['Rimi kesk.']:>8.2f} {row['Selver kesk.']:>8.2f} {row['Vahe']:>+8.2f} {row['Odavam']:<10}")

print("\n" + "=" * 80)
print("KOKKUVÕTE")
print("=" * 80)
rimi_wins = (results['Vahe'] > 0).sum()
selver_wins = (results['Vahe'] < 0).sum()
print(f"Rimi odavam:   {rimi_wins} kategoorias")
print(f"Selver odavam: {selver_wins} kategoorias")
print(f"Rimi keskmine vahe kui odavam:   {results[results['Vahe'] > 0]['Vahe'].mean():.2f} EUR")
print(f"Selver keskmine vahe kui odavam: {results[results['Vahe'] < 0]['Vahe'].mean():.2f} EUR")

print("\n" + "=" * 80)
print("TOP 10 — RIMI ODAVAM")
print("=" * 80)
top_rimi = results[results['Vahe'] > 0].nlargest(10, 'Vahe')
for _, row in top_rimi.iterrows():
    print(f"{row['Kategooria']:<35} Rimi {row['Rimi kesk.']:.2f} vs Selver {row['Selver kesk.']:.2f} (vahe {row['Vahe']:+.2f})")

print("\n" + "=" * 80)
print("TOP 10 — SELVER ODAVAM")
print("=" * 80)
top_selver = results[results['Vahe'] < 0].nsmallest(10, 'Vahe')
for _, row in top_selver.iterrows():
    print(f"{row['Kategooria']:<35} Selver {row['Selver kesk.']:.2f} vs Rimi {row['Rimi kesk.']:.2f} (vahe {row['Vahe']:+.2f})")

print("\n" + "=" * 80)
print("ODAVAIM JA KALLEIM TOODE KATEGOORIAS")
print("=" * 80)
for cat_name, store_cats in CATEGORY_MAP.items():
    store_data = {}
    valid = True
    for store in stores:
        if store not in store_cats:
            valid = False
            break
        ids = store_cats[store]
        sub = df[(df['store'] == store) & (df['category'].isin(ids))]
        if sub.empty:
            valid = False
            break
        store_data[store] = sub
    if not valid:
        continue

    print(f"\n{cat_name}:")
    for store in stores:
        sub = store_data[store]
        cheapest = sub.loc[sub['price'].idxmin()]
        priciest = sub.loc[sub['price'].idxmax()]
        print(f"  {store.capitalize():<8} odavaim: {cheapest['price']:.2f} EUR — {cheapest['name'][:50]}")
        print(f"  {store.capitalize():<8} kalleim: {priciest['price']:.2f} EUR — {priciest['name'][:50]}")