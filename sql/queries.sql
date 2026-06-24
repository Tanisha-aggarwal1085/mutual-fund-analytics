-- Top 5 funds by AUM
SELECT * FROM aum_data
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav) AS average_nav
FROM nav_history;

-- Monthly NAV
SELECT strftime('%m', date) AS month,
AVG(nav)
FROM nav_history
GROUP BY month;

-- Funds with low expense ratio
SELECT *
FROM expense_ratio
WHERE expense_ratio < 1;

-- Top returns
SELECT *
FROM returns_3yr
ORDER BY return_3yr DESC
LIMIT 5;

-- Total schemes
SELECT COUNT(*) FROM fund_master;

-- Average SIP amount
SELECT AVG(sip_amount)
FROM sip_data;

-- High risk funds
SELECT *
FROM fund_master
WHERE risk_grade = 'High';

-- Total investors
SELECT COUNT(*)
FROM investor_data;

-- Average AUM
SELECT AVG(aum)
FROM aum_data;