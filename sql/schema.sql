CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    subcategory TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    scheme_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    return_1yr REAL,
    return_3yr REAL,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    aum REAL
);