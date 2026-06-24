import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

csv_files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

for file in csv_files:

    print("\nProcessing:", file)

    df = pd.read_csv(os.path.join(RAW_PATH, file))

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # convert date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # fill missing values
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # validate NAV > 0
    if 'nav' in df.columns:
        df = df[df['nav'] > 0]

    # standardize transaction types
    if 'transaction_type' in df.columns:

        df['transaction_type'] = (
            df['transaction_type']
            .str.upper()
            .replace({
                'SIP ': 'SIP',
                'LUMP SUM': 'LUMPSUM'
            })
        )

    # save cleaned file
    save_path = os.path.join(PROCESSED_PATH, file)

    df.to_csv(save_path, index=False)

    print("Saved:", save_path)

print("\nCleaning completed")