import pytest
from src.data_loader import DataLoader
import pandas as pd

class TestDataLoader:
    """Unit tests for DataLoader class"""
    
    def test_singleton_pattern(self):
        """Test if DataLoader follows Singleton pattern"""
        loader1 = DataLoader()
        loader2 = DataLoader()
        assert loader1 is loader2
    
    def test_load_data_success(self, sample_sales_data, test_file_path):
        """Test successful data loading"""
        # Save sample data to temp file
        sample_sales_data.to_csv(test_file_path, index=False)
        
        loader = DataLoader()
        data = loader.load_data(str(test_file_path))
        
        assert data is not None
        assert not data.empty
        assert 'Date' in data.columns
        
    def test_load_data_failure(self):
        """Test data loading with non-existent file"""
        loader = DataLoader()
        data = loader.load_data("nonexistent_file.csv")
        assert data is None 