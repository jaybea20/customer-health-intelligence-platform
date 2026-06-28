from faker import Faker
import pandas as pd
import numpy as np
import random
from pathlib import Path

fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 5000
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

industries = ["Healthcare", "Manufacturing", "Financial Services", "Technology", "Education", "Logistics"]
tiers = ["Starter", "Professional", "Enterprise"]

customers = []

for i in range(NUM_CUSTOMERS):
    licensed = random.randint(15, 500)
    active = max(1, min(licensed, int(np.random.normal(licensed * 0.72, licensed * 0.15))))
    arr = random.randint(12000, 300000)

    customers.append({
        "customer_id": f"CUST-{100000+i}",
        "company_name": fake.company(),
        "industry": random.choice(industries),
        "subscription_tier": random.choice(tiers),
        "annual_recurring_revenue": arr,
        "licensed_users": licensed,
        "active_users": active,
        "renewal_days": random.randint(1, 365),
        "feature_adoption_pct": round(np.random.beta(5, 2) * 100, 1),
        "login_days_30d": random.randint(0, 30),
        "support_tickets_30d": np.random.poisson(2),
        "avg_resolution_days": round(max(0.5, np.random.normal(3.5, 2)), 1),
        "nps_score": random.randint(-40, 80),
        "days_since_csm_touch": random.randint(0, 120),
        "has_executive_sponsor": random.choice([0, 1])
    })

df = pd.DataFrame(customers)

df["active_user_pct"] = round(df["active_users"] / df["licensed_users"] * 100, 1)

df.to_csv(DATA_DIR / "customers.csv", index=False)

print("Created data/customers.csv")
print(df.head())
print(f"Rows: {len(df)}")