import duckdb
from pathlib import Path

DATA_PATH = Path("data/customers.csv")
SQL_PATH = Path("sql/customer_health_features.sql")
OUTPUT_PATH = Path("output/customer_health_features.csv")

OUTPUT_PATH.parent.mkdir(exist_ok=True)

conn = duckdb.connect("output/customer_health.duckdb")

conn.execute(f"""
CREATE OR REPLACE TABLE customers AS
SELECT *
FROM read_csv_auto('{DATA_PATH.as_posix()}');
""")

sql = SQL_PATH.read_text()
conn.execute(sql)

features = conn.execute("""
SELECT *
FROM customer_health_features;
""").df()

features.to_csv(OUTPUT_PATH, index=False)

print(f"Created {OUTPUT_PATH}")
print(features.head())
print(f"Rows: {len(features)}")