from abc import ABC, abstractmethod
from typing import List
import pandas as pd

class BaseAnalyzer(ABC):
    """Base class for all analyzers following Template Method pattern"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
        
    @abstractmethod
    def analyze(self) -> dict:
        """Perform the analysis and return results"""
        pass
    
    def validate_data(self) -> bool:
        """Validate if required columns exist in the data"""
        return not self.data.empty 