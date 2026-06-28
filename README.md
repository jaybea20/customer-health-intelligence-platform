# Customer Health Intelligence Platform

A portfolio case study recreating and modernizing a customer health scoring framework for a fictional B2B SaaS company, NimbusCloud.

## Business Problem

Customer Success teams need a consistent daily way to identify which accounts require attention before renewal. This project creates a customer health score using product usage, support burden, sentiment, engagement, and renewal timing.

## Tools Used

- Python
- SQL
- DuckDB
- Pandas
- GitHub
- Power BI-ready CSV output

## Workflow

1. Generate synthetic SaaS customer data
2. Use SQL to create customer health features
3. Use Python to calculate customer health scores
4. Export Salesforce-ready account recommendations

## Outputs

- `data/customers.csv`
- `output/customer_health_features.csv`
- `output/customer_health_scores.csv`

## Health Score Components

- Usage Score
- Feature Adoption Score
- Support Score
- Sentiment Score
- Engagement Score

## Example Recommendations

- Escalate renewal risk and schedule executive outreach
- Prioritize CSM outreach and create success plan
- Schedule product enablement session
- Evaluate expansion opportunity
- Monitor