from pathlib import Path

# Resolve paths relative to this script's directory so it works from anywhere
script_dir = Path(__file__).resolve().parent
project_cwd = Path.cwd()
print("Script directory:", script_dir)
print("Current working directory:", project_cwd)

# Build data path relative to the script location
data_path = script_dir / "data" / "sales.csv"

if data_path.exists():
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Tip: Ensure sales.csv exists under sales-analysis/data/")