import sqlite3
import pandas as pd

# Define the CSV file and SQLite database file
csv_file = '/Users/yorca/Downloads/latest_with-added-date.csv'
sqlite_db = 'sdk_interaction.db'
table_name = 'androzoo_metadb'

# Load CSV into a DataFrame
df = pd.read_csv(csv_file)

# Connect to SQLite (it will create the database if it doesn't exist)
conn = sqlite3.connect(sqlite_db)

# Write the DataFrame to a SQLite table
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print(f"CSV data has been successfully imported into {sqlite_db} in the {table_name} table.")
