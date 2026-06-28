import duckdb
from pathlib import Path

DATA_DIR = Path("data")
SQL_PATH = Path("sql/customer_health_features.sql")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)

conn = duckdb.connect(OUTPUT_DIR / "customer_health.duckdb")

# -------------------------
# Load CSVs into DuckDB
# -------------------------

tables = {
    "customers": "customers.csv",
    "product_usage": "product_usage.csv",
    "support_cases": "support_cases.csv",
    "customer_success": "customer_success.csv"
}

for table_name, file_name in tables.items():

    csv_path = DATA_DIR / file_name

    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_csv_auto('{csv_path.as_posix()}');
    """)

print("Loaded tables:")
for table in tables:
    print(f" - {table}")

# -------------------------
# Execute SQL
# -------------------------

sql = SQL_PATH.read_text()

conn.execute(sql)

features = conn.execute("""
SELECT *
FROM customer_health_features
""").df()

output_file = OUTPUT_DIR / "customer_health_features.csv"

features.to_csv(output_file, index=False)

print()
print(f"Created {output_file}")
print(f"Rows: {len(features)}")
print()
print(features.head())