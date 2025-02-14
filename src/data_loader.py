import pandas as pd
from typing import Optional

class DataLoader:
    """Singleton pattern for loading and managing sales data"""
    _instance = None
    _data = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        return cls._instance
    
    def load_data(self, file_path: str) -> Optional[pd.DataFrame]:
        """Load data from CSV file"""
        try:
            self._data = pd.read_csv(file_path)
            # Convert Date column to datetime
            self._data['Date'] = pd.to_datetime(self._data['Date'])
            return self._data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    @property
    def data(self) -> Optional[pd.DataFrame]:
        return self._data 