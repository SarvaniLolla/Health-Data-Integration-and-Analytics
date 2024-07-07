import pandas as pd
import pyodbc

# Connect to Azure SQL Database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=<azure_sql_server_name>.database.windows.net;DATABASE=<database_name>;UID=<username>;PWD=<password>')

# Example data transformation using pandas
def transform_data():
    # Load data from SQL into pandas DataFrame
    df = pd.read_sql("SELECT * FROM <table_name>", conn)

    # Perform data transformations (e.g., cleaning, aggregations)
    df['new_column'] = df['old_column'] * 2

    # Save transformed data back to SQL Database
    df.to_sql('<transformed_table_name>', conn, if_exists='replace', index=False)

transform_data()
