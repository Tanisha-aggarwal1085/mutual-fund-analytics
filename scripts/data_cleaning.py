import pandas as pd
import os

# folders
RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

# create processed folder if not exists
os.makedirs(PROCESSED_PATH, exist_ok=True)

# all csv files
csv_files = [file for file in os.listdir(RAW_PATH) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} files\n")

for file in csv_files:

    print("=" * 60)
    print("Processing:", file)

    # read file
    df = pd.read_csv(os.path.join(RAW_PATH, file))

    # BEFORE CLEANING
    print("\nOriginal Shape:", df.shape)

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # missing values
    missing = df.isnull().sum()

    print("\nMissing Values:")
    print(missing)

    # fill numeric missing values
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # convert date column if exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # AFTER CLEANING
    print("\nCleaned Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    # save cleaned file
    save_path = os.path.join(PROCESSED_PATH, file)

    df.to_csv(save_path, index=False)

    print("\nSaved Cleaned File:", save_path)

print("\nAll datasets cleaned successfully")