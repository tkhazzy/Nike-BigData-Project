import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_NAME = "nikeusers"
DB_USER = "root"
DB_PASSWORD = "Takomborerwa15!"
DB_HOST = "localhost"
DB_PORT = 3306

# Create SQLAlchemy engine for MySQL database
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Read the Parquet file into a pandas DataFrame
parquet_file_path = "users.parquet"
df = pd.read_parquet(parquet_file_path)

# Inspect the DataFrame
print(df.head())

# Transfer data to the SQL table in chunks
table_name = "users"
chunk_size = 10000

try:
    df.to_sql(table_name, con=engine, if_exists="append", index=False, chunksize=chunk_size)
    print(f"Data successfully loaded into {table_name} table in {DB_NAME} database.")
except Exception as e:
    print(f"An error occurred: {e}")
