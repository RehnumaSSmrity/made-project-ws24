# Python imports
import os

# Third-party imports
import numpy as np
import pandas as pd

# Self imports6
from main.authpipeline import (
    ETLPipeline,
    DataSource,
    CSVFile,
    SQLiteDB,
)

if __name__ == "__main__":
    data_directory = os.path.join(os.getcwd(), "data")
    
    # Seoul Bike Sharing Data Pipeline
    
    bike_output_db = SQLiteDB(
        db_name="seoul.sqlite",
        table_name="bike_data",
        if_exists=SQLiteDB.REPLACE,
        index=False,
        method=None,
        output_directory=data_directory,
    )
    bike_file_dtype = {
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
        "Functioning Day": "str",
    }

    def transform_bike(data_frame: pd.DataFrame):
        
        data_frame = data_frame.rename(columns={"Functioning Day": "Working Day"})
        return data_frame

    bike_file = CSVFile(
        file_name="SeoulBikeData.csv",
        sep=",",
        names=None,
        dtype=bike_file_dtype,
        transform=transform_bike,
        encoding='latin-1',
    )
    bike_data_source = DataSource(
        data_name="bike sharing data",
        url="https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing/?select=SeoulBikeData.csv",
        source_type=DataSource.KAGGLE_DATA,
        files=(bike_file,),
    )
    bike_pipeline = ETLPipeline(
        data_source=bike_data_source,
        sqlite_db=bike_output_db,
    )
    bike_pipeline.run_pipeline()

    # Air Pollution in Seoul Data Pipeline
    
    air_output_db = SQLiteDB(
        db_name="seoul.sqlite",
        table_name="air",
        if_exists=SQLiteDB.REPLACE,
        index=False,
        method=None,
        output_directory=data_directory,
    )
    air_file_dtype = {
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
    }
    

    
    air_file = CSVFile(
        file_name="Measurement_summary.csv",
        sep=",",
        names=None,
        dtype=air_file_dtype,
        encoding='latin-1',
    )
    air_data_source = DataSource(
        data_name="Air Pollution in Seoul",
        url="https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul",
        source_type=DataSource.KAGGLE_DATA,
        files=(air_file,),
    )
    weather_pipeline = ETLPipeline(
        data_source=air_data_source,
        sqlite_db=air_output_db,
    )
    weather_pipeline.run_pipeline()