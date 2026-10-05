"""
Handles data ingestion, engineering unit checking, missing value interpolation, and processing raw vehicle data logs.
"""



import pandas as pd
import numpy as np
import os

class CalibrationDataParser:
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Raw log data not found at {filepath}")

    def load_and_clean_data(self) -> pd.DataFrame:
        """Loads raw engine test logs and applies standard engineering cleanups."""
        df = pd.read_csv(self.filepath)
        
        # Replace missing or noisy signals with interpolation
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.interpolate(method='linear', inplace=True)
        
        # Derive key metric: Calculated Air-Fuel Ratio (AFR) based on Lambda (Stoichiometric = 14.7)
        df['calculated_afr'] = df['lambda_sensor'] * 14.7
        
        return df
      
