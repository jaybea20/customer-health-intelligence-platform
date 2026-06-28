CREATE OR REPLACE TABLE customer_health_features AS

SELECT

    c.customer_id,
    c.company_name,
    c.industry,
    c.subscription_tier,
    c.annual_recurring_revenue,
    c.licensed_users,

    u.active_user_pct,
    u.login_days_30d,
    u.feature_adoption_pct,
    u.usage_trend_pct,

    s.support_tickets_30d,
    s.high_severity_cases,
    s.avg_resolution_days,

    cs.days_since_csm_touch,
    cs.last_qbr_days,
    cs.has_executive_sponsor,

    c.nps_score,
    c.renewal_days,

    CASE
        WHEN c.renewal_days <= 30 THEN 'Renewal due in 30 days'
        WHEN c.renewal_days <= 90 THEN 'Renewal due in 90 days'
        ELSE 'Renewal not imminent'
    END AS renewal_window,

    CASE WHEN u.active_user_pct < 40 THEN 1 ELSE 0 END AS low_usage_flag,

    CASE WHEN u.feature_adoption_pct < 50 THEN 1 ELSE 0 END AS low_adoption_flag,

    CASE WHEN s.support_tickets_30d >= 5 THEN 1 ELSE 0 END AS high_support_flag,

    CASE WHEN c.nps_score < 0 THEN 1 ELSE 0 END AS negative_nps_flag,

    CASE WHEN cs.days_since_csm_touch > 60 THEN 1 ELSE 0 END AS stale_csm_touch_flag

FROM customers c

LEFT JOIN product_usage u
ON c.customer_id = u.customer_id

LEFT JOIN support_cases s
ON c.customer_id = s.customer_id

LEFT JOIN customer_success cs
ON c.customer_id = cs.customer_id;