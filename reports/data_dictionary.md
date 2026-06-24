# Data Dictionary

## fund_master.csv

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| scheme_code | Integer | Unique AMFI scheme code |
| scheme_name | Text | Mutual fund scheme name |
| fund_house | Text | AMC/Fund house |
| category | Text | Fund category |
| subcategory | Text | Fund subcategory |
| risk_grade | Text | Risk level |

---

## nav_history.csv

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| scheme_code | Integer | Fund code |
| date | Date | NAV date |
| nav | Float | Net asset value |

---

## investor_data.csv

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| investor_id | Integer | Investor ID |
| investment_amount | Float | Investment amount |