CREATE OR REPLACE TABLE customer_health_features AS

SELECT

    customer_id,
    company_name,
    industry,
    subscription_tier,
    annual_recurring_revenue,
    licensed_users,
    active_users,
    active_user_pct,
    feature_adoption_pct,
    login_days_30d,
    support_tickets_30d,
    avg_resolution_days,
    nps_score,
    renewal_days,
    days_since_csm_touch,
    has_executive_sponsor,

    CASE
        WHEN renewal_days <= 30 THEN 'Renewal due in 30 days'
        WHEN renewal_days <= 90 THEN 'Renewal due in 90 days'
        ELSE 'Renewal not imminent'
    END AS renewal_window,

    CASE
        WHEN active_user_pct < 40 THEN 1
        ELSE 0
    END AS low_usage_flag,

    CASE
        WHEN feature_adoption_pct < 50 THEN 1
        ELSE 0
    END AS low_adoption_flag,

    CASE
        WHEN support_tickets_30d >= 5 THEN 1
        ELSE 0
    END AS high_support_flag,

    CASE
        WHEN nps_score < 0 THEN 1
        ELSE 0
    END AS negative_nps_flag,

    CASE
        WHEN days_since_csm_touch > 60 THEN 1
        ELSE 0
    END AS stale_csm_touch_flag

FROM customers;