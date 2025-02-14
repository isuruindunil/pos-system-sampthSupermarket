import pytest
import pandas as pd
import os

@pytest.fixture
def sample_sales_data():
    """Fixture providing sample sales data for testing"""
    return pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'Branch': ['Colombo', 'Kandy', 'Colombo'],
        'Product Name': ['Product A', 'Product B', 'Product A'],
        'Brand': ['Brand X', 'Brand Y', 'Brand X'],
        'Price Per Unit': [100.0, 150.0, 100.0],
        'Quantity': [2, 3, 1],
        'Total Sales Amount': [200.0, 450.0, 100.0]
    })

@pytest.fixture
def test_file_path(tmp_path):
    """Fixture providing temporary file path"""
    return tmp_path / "test_sales_data.csv" 