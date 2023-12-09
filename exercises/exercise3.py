import pandas as pd

# Load data with required columns and skip the first 6 rows
columns_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]

# URL of the data source
data_frame = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv',
                         sep=';', encoding='latin-1', dtype={1: str}, skiprows=6, usecols=columns_to_keep)

# Drop the last 4 rows
data_frame = data_frame[:-4]

# Rename columns
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
data_frame.columns = column_names

# Remove rows with invalid CIN values (not 5 characters long)
data_frame = data_frame[data_frame['CIN'].str.len() == 5]

# Remove rows with non-positive values in specific columns
positive_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
for column in positive_columns:
    data_frame = data_frame[data_frame[column] != '-']
data_frame[positive_columns] = data_frame[positive_columns].astype(int)
for column in positive_columns:
    data_frame = data_frame[data_frame[column] > 0]

# Save the transformed database
data_frame.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)