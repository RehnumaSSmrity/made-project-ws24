import pandas as pd

# Define the columns to keep from the dataset
columns_to_keep = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]

# URL of the data source
data_url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'

# Load data from the CSV file
# Skip the first 6 rows, use specific columns, and set proper encoding
data_frame = pd.read_csv(data_url, sep=';', encoding='latin-1', dtype={1: str},
                         skiprows=6, usecols=columns_to_keep)

# Drop the last 4 rows of the dataframe
data_frame = data_frame[:-4]

# Rename columns for better readability
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro',
                'hybrid', 'plugInHybrid', 'others']
data_frame.columns = column_names

# Filter out rows with invalid CIN values (not equal to 5 characters)
data_frame = data_frame[data_frame['CIN'].str.len() == 5]

# Replace non-numeric values with NaN and then drop these rows
positive_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
data_frame[positive_columns] = data_frame[positive_columns].replace('-', pd.NA)
data_frame.dropna(subset=positive_columns, inplace=True)

# Convert columns to integers
data_frame[positive_columns] = data_frame[positive_columns].astype(int)

# Keep only rows with positive values in specified columns
for column in positive_columns:
    data_frame = data_frame[data_frame[column] > 0]

# Save the transformed database to an SQLite database
data_frame.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)