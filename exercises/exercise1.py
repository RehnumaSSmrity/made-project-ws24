import pandas as pd
from sqlalchemy import create_engine


class DataPipeline:
    def __init__(self) -> None:
        # Define the data source URL and the destination database URL
        self.data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
        self.database_url = "sqlite:///airports.sqlite"
   
    def extract(self):
        """
        Extract data from the specified CSV URL.
        """
        # Extract CSV data from the URL and display the first few rows
        self.data = pd.read_csv(self.data_url, sep=';')
        print(self.data.head())
           
    def transform(self):
        """
        Transform the extracted data and display information about the dataframe.
        """
        print("Transforming data:")
        # Display information about the dataframe
        print(self.data.info())
   
    def load(self):
        """
        Load the transformed data into the SQLite database.
        """
        # Create an SQLite engine and load data into the 'airports' table
        engine = create_engine(self.database_url)
        self.data.to_sql("airports", con=engine, index=False, if_exists="replace")
       
    def run_pipeline(self):
        """
        Run the entire data pipeline: extract, transform, and load.
        """
        self.extract()
        self.transform()
        self.load()

# Create an instance of the AirportDataPipeline class and run the data pipeline
pipeline = DataPipeline()
pipeline.run_pipeline()
