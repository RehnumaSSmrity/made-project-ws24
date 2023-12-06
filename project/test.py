import unittest
import os
import sqlite3
import numpy as np
import pandas as pd
from main.authpipeline import ETLPipeline, DataSource, CSVFile, SQLiteDB

class TestDatasetProcessing(unittest.TestCase):
    def setUp(self):
        # You can modify this path based on your project structure
        self.base_path = r'\Users\rehnuma\Documents\GitHub\made-project-ws24\Project'

    def test_bike_pipeline(self):
        # Bike Sharing Data Pipeline Test
        data_source = DataSource(
            data_name="bike sharing data",
            url="https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing/?select=SeoulBikeData.csv",
            source_type=DataSource.KAGGLE_DATA,
            files=(CSVFile(
                file_name="SeoulBikeData.csv",
                encoding='latin-1',
                sep=",",
                names=None,
                dtype={
                    "date": "str",
                    "Rented Bike Count": float,
                    "Hour": float,
                    "Temperature(°C)": float,
                    "Wind speed (m/s)": float,
                    "Visibility (10m)": float,
                    "Dew point temperature(°C)": float,
                    "Solar Radiation (MJ/m2)": float,
                    "Rainfall(mm)": float,
                    "Snowfall (cm)": float,
                    "season": float,
                    "Seasons": "str",
                    "Holiday": "str",
                    "Working Day": "str",  # Adjusted column name
                },
            ),)
        )

        sqlite_db = SQLiteDB(
            db_name="seoul.sqlite",
            table_name="bike_data",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            method=None,
            output_directory=self.base_path,
        )

        bike_pipeline = ETLPipeline(data_source=data_source, sqlite_db=sqlite_db)
        bike_pipeline.run_pipeline()

        # Ensure the SQLite database is created and the table is populated
        db_path = os.path.join(self.base_path, 'seoul.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bike_data")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 1, "The 'bike_data' table does not exist.")

    def test_weather_pipeline(self):
        # Air Pollution in Seoul Data Pipeline Test
        data_source = DataSource(
            data_name="Air Pollution in Seoul",
            url="https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul",
            source_type=DataSource.KAGGLE_DATA,
            files=(CSVFile(
                file_name="Measurement_summary.csv",
                encoding='latin-1',
                sep=",",
                names=None,
                dtype={
                    "Measurement date": "str",
                    "Station code": float,
                    "Address": "str",
                    "Latitude": "int64",
                    "Longitude": "int64",
                    "SO2": np.float64,
                    "NO2": np.float64,
                    "O3": np.float64,
                    "CO": float,
                    "PM10": float,
                    "PM2.5": float,
                },
            ),)
        )

        sqlite_db = SQLiteDB(
            db_name="seoul.sqlite",
            table_name="air",
            if_exists=SQLiteDB.REPLACE,
            index=False,
            method=None,
            output_directory=self.base_path,
        )

        air_pipeline = ETLPipeline(data_source=data_source, sqlite_db=sqlite_db)
        air_pipeline.run_pipeline()

        # Ensure the SQLite database is created and the table is populated
        db_path = os.path.join(self.base_path, 'seoul.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM air")
        result = cursor.fetchall()
        conn.close()

        self.assertGreater(len(result), 1, "The 'air' table does not exist.")
    
    def test_main_sqlite_exists(self):
        # Check if the main SQLite database file exists
        assert os.path.exists(os.path.join(self.base_path, "seoul.sqlite"))

if __name__ == '__main__':
    unittest.main()

