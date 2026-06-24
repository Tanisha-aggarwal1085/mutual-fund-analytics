import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine

DATABASE_PATH = "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

PROCESSED_PATH = "data/processed"

csv_files = [f for f in os.listdir(PROCESSED_PATH) if f.endswith(".csv")]

for file in csv_files:

    table_name = file.replace(".csv", "")

    print("\nLoading:", table_name)

    df = pd.read_csv(os.path.join(PROCESSED_PATH, file))

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print("Rows Loaded:", len(df))

print("\nSQLite database created successfully")