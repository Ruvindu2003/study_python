import pandas as pd
import json
from pathlib import Path

# Resolve paths relative to this script's folder so it runs from anywhere
script_dir = Path(__file__).resolve().parent
data_path = script_dir / 'data' / 'sales.csv'
output_dir = script_dir / 'output'
output_dir.mkdir(parents=True, exist_ok=True)

# Read the CSV file
print(f"Reading: {data_path}")
df = pd.read_csv(data_path)
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Save as different formats
# 1. JSON format (good for web APIs)
(output_dir / 'sales_data.json').write_text(
	df.to_json(orient='records', indent=2)
)

# 2. Excel format (good for sharing)
try:
	df.to_excel(output_dir / 'sales_data.xlsx', index=False)
	excel_saved = True
except ImportError:
	excel_saved = False
	print("Note: openpyxl not installed; skipping Excel export.")

# 3. Updated CSV (with our new total column)
df.to_csv(output_dir / 'sales_with_totals.csv', index=False)

print("\nFiles saved:")
print(f"- {output_dir / 'sales_data.json'}")
if excel_saved:
	print(f"- {output_dir / 'sales_data.xlsx'}")
print(f"- {output_dir / 'sales_with_totals.csv'}")