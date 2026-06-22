import requests
import pandas as pd
import os

# save folder
SAVE_PATH = "data/raw"

# fund names + codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data['data'])

        file_name = f"{fund_name}.csv"

        nav_df.to_csv(os.path.join(SAVE_PATH, file_name), index=False)

        print("Saved:", file_name)

    else:
        print("Failed")