import pandas as pd
import os

# dataset folder path
DATA_PATH = "data/raw"

# csv files list
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 50)
    print("FILE NAME:", file)

    try:
        # read csv
        df = pd.read_csv(os.path.join(DATA_PATH, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print("Error:", e)

print("\nAll files loaded successfully")