# Importing the pandas library
import pandas as pd

# Define columns to be kept from the dataset
columns_selected = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]

# Data source URL
data_url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'

# Load the dataset, specifying necessary parameters
# Skip the first 6 rows, use specific columns, and set encoding
vehicle_data = pd.read_csv(data_url, sep=';', encoding='latin-1', dtype={1: str},
                           skiprows=6, usecols=columns_selected)

# Drop the last 4 rows from the dataframe
vehicle_data = vehicle_data[:-4]

# Renaming the dataframe columns for clarity
column_labels = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas',
                 'electro', 'hybrid', 'plugInHybrid', 'others']
vehicle_data.columns = column_labels

# Filter out rows with invalid CIN values (length not equal to 5)
vehicle_data = vehicle_data[vehicle_data['CIN'].str.len() == 5]

# Remove rows with non-positive values in specific columns
fuel_types = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
for fuel in fuel_types:
    # Convert columns to integers, replacing non-numeric values
    vehicle_data[fuel] = pd.to_numeric(vehicle_data[fuel], errors='coerce')
    # Keep rows with positive values only
    vehicle_data = vehicle_data[vehicle_data[fuel] > 0]

# Save the transformed data to a SQLite database
vehicle_data.to_sql('vehicle_registry', 'sqlite:///vehicle_registry.sqlite', if_exists='replace', index=False)
