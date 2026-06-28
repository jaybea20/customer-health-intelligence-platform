import pandas as pd
from pathlib import Path

INPUT_PATH = Path("output/customer_health_features.csv")
OUTPUT_PATH = Path("output/customer_health_scores.csv")

df = pd.read_csv(INPUT_PATH)

# Component scores, each scaled 0-100
df["usage_score"] = df["active_user_pct"].clip(0, 100)
df["adoption_score"] = df["feature_adoption_pct"].clip(0, 100)
df["support_score"] = (100 - (df["support_tickets_30d"] * 12) - (df["avg_resolution_days"] * 4)).clip(0, 100)
df["sentiment_score"] = ((df["nps_score"] + 100) / 2).clip(0, 100)
df["engagement_score"] = (100 - df["days_since_csm_touch"]).clip(0, 100)

# Weighted customer health score
df["health_score"] = (
    df["usage_score"] * 0.30
    + df["adoption_score"] * 0.25
    + df["support_score"] * 0.20
    + df["sentiment_score"] * 0.15
    + df["engagement_score"] * 0.10
).round(1)

df["health_status"] = pd.cut(
    df["health_score"],
    bins=[-1, 50, 70, 100],
    labels=["At Risk", "Watch", "Healthy"]
)

def risk_reason(row):
    reasons = []
    if row["low_usage_flag"] == 1:
        reasons.append("Low active usage")
    if row["low_adoption_flag"] == 1:
        reasons.append("Low feature adoption")
    if row["high_support_flag"] == 1:
        reasons.append("High support volume")
    if row["negative_nps_flag"] == 1:
        reasons.append("Negative NPS")
    if row["stale_csm_touch_flag"] == 1:
        reasons.append("No recent CSM touch")
    if row["renewal_days"] <= 90:
        reasons.append("Upcoming renewal")
    return "; ".join(reasons) if reasons else "No major risk drivers"

def recommended_action(row):
    if row["health_status"] == "At Risk" and row["renewal_days"] <= 90:
        return "Escalate renewal risk and schedule executive outreach"
    if row["health_status"] == "At Risk":
        return "Prioritize CSM outreach and create success plan"
    if row["low_adoption_flag"] == 1:
        return "Schedule product enablement session"
    if row["high_support_flag"] == 1:
        return "Review support history and escalate recurring issues"
    if row["health_status"] == "Healthy" and row["annual_recurring_revenue"] > 100000:
        return "Evaluate expansion opportunity"
    return "Monitor"

df["primary_risk_reasons"] = df.apply(risk_reason, axis=1)
df["recommended_action"] = df.apply(recommended_action, axis=1)
df["salesforce_update_date"] = pd.Timestamp.today().date()

cols = [
    "customer_id",
    "company_name",
    "industry",
    "subscription_tier",
    "annual_recurring_revenue",
    "renewal_days",
    "health_score",
    "health_status",
    "primary_risk_reasons",
    "recommended_action",
    "salesforce_update_date"
]

df[cols].to_csv(OUTPUT_PATH, index=False)

print(f"Created {OUTPUT_PATH}")
print(df[cols].head())
print(f"Rows: {len(df)}")
print(df["health_status"].value_counts())