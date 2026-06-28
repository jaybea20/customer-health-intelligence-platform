# Customer Health Intelligence Platform

## Overview

One of my previous projects involved building a customer health score to help Customer Success Managers prioritize outreach. At the time, the score was based on manually weighted business rules.

For this portfolio project, I wanted to revisit that idea using modern analytics tools. I created a fictional B2B SaaS company and built an end-to-end pipeline that generates customer data, engineers health features with SQL, calculates a customer health score in Python, and produces recommendations that could be sent back to Salesforce.

Although the data is synthetic, the business problem and workflow closely mirror the type of work performed by Customer Success analytics teams.

---

## The Business Problem

Customer Success Managers are responsible for hundreds of customer accounts, making it difficult to know which customers need attention first.

The goal of this project is to answer questions like:

- Which customers are at the highest risk?
- Which accounts should Customer Success contact today?
- Which customers might be good candidates for expansion?
- What factors are driving each customer's health score?

---

## What I Built

This project includes:

- A Python script that generates realistic SaaS customer data
- SQL feature engineering using DuckDB
- A weighted customer health scoring model in Python
- Business recommendations for each customer
- A Salesforce-ready export that could be consumed by Customer Success teams

---

## Technology

- Python
- SQL
- DuckDB
- Pandas
- Git & GitHub
- Power BI (coming next)

---

## Project Workflow

1. Generate synthetic customer data.
2. Engineer customer health features using SQL.
3. Calculate a customer health score.
4. Classify each customer as Healthy, Watch, or At Risk.
5. Generate recommended actions for Customer Success.

---

## Sample Output

The final dataset contains information such as:

- Customer Health Score
- Health Status
- Primary Risk Drivers
- Recommended Action
- Salesforce Update Date

---

## What I'd Improve Next

If this were moving into production, I would:

- Separate the data into multiple related tables instead of a single dataset.
- Add historical customer activity and trend analysis.
- Build a Power BI dashboard for leadership.
- Compare the rules-based score with a machine learning model.
- Automate the daily scoring pipeline.

---

## Why I Built This

I enjoy projects that sit at the intersection of business strategy and analytics.

This case study gave me an opportunity to recreate a real business problem I had previously worked on while modernizing the solution with SQL, Python, and a reproducible analytics pipeline.