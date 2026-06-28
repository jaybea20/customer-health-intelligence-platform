import pandas as pd
import numpy as np
import random
from pathlib import Path

random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 5000
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

industries = ["Healthcare", "Manufacturing", "Financial Services", "Technology", "Education", "Logistics"]
tiers = ["Starter", "Professional", "Enterprise"]

prefixes = ["Apex", "Nimbus", "Vertex", "Summit", "BluePeak", "Evergreen", "Nova", "Pioneer", "Atlas", "Bright"]
suffixes = ["Solutions", "Systems", "Health", "Financial", "Logistics", "Networks", "Technologies", "Industries"]

customers = []
usage = []
support = []
customer_success = []

for i in range(NUM_CUSTOMERS):
    customer_id = f"CUST-{100000+i}"
    licensed = random.randint(15, 500)
    active_pct = round(np.clip(np.random.normal(72, 18), 5, 100), 1)

    customers.append({
        "customer_id": customer_id,
        "company_name": f"{random.choice(prefixes)} {random.choice(suffixes)}",
        "industry": random.choice(industries),
        "subscription_tier": random.choice(tiers),
        "annual_recurring_revenue": random.randint(12000, 300000),
        "licensed_users": licensed,
        "renewal_days": random.randint(1, 365),
        "nps_score": random.randint(-40, 80)
    })

    usage.append({
        "customer_id": customer_id,
        "active_user_pct": active_pct,
        "login_days_30d": random.randint(0, 30),
        "feature_adoption_pct": round(np.clip(np.random.normal(68, 22), 0, 100), 1),
        "usage_trend_pct": round(np.random.normal(0, 18), 1)
    })

    support.append({
        "customer_id": customer_id,
        "support_tickets_30d": np.random.poisson(2),
        "high_severity_cases": np.random.poisson(0.4),
        "avg_resolution_days": round(max(0.5, np.random.normal(3.5, 2)), 1)
    })

    customer_success.append({
        "customer_id": customer_id,
        "days_since_csm_touch": random.randint(0, 120),
        "last_qbr_days": random.randint(0, 180),
        "has_executive_sponsor": random.choice([0, 1])
    })

pd.DataFrame(customers).to_csv(DATA_DIR / "customers.csv", index=False)
pd.DataFrame(usage).to_csv(DATA_DIR / "product_usage.csv", index=False)
pd.DataFrame(support).to_csv(DATA_DIR / "support_cases.csv", index=False)
pd.DataFrame(customer_success).to_csv(DATA_DIR / "customer_success.csv", index=False)

print("Created:")
print("- data/customers.csv")
print("- data/product_usage.csv")
print("- data/support_cases.csv")
print("- data/customer_success.csv")
print(f"Rows per table: {NUM_CUSTOMERS}")