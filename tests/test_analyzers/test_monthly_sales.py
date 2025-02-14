import pytest
import pandas as pd
from src.analyzers.monthly_sales_analyzer import MonthlySalesAnalyzer
import os

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-15', '2024-02-01'],
        'Branch': ['Colombo', 'Colombo', 'Kandy'],
        'Total Sales Amount': [100.0, 200.0, 300.0]
    })

def test_monthly_sales_analysis(sample_data):
    analyzer = MonthlySalesAnalyzer(sample_data)
    results = analyzer.analyze()
    
    assert 'Colombo' in results
    assert 'Kandy' in results
    assert results['Colombo']['2024-01'] == 300.0
    assert results['Kandy']['2024-02'] == 300.0

class TestMonthlySalesAnalyzer:
    """Integration tests for MonthlySalesAnalyzer"""
    
    def test_analyze_all_branches(self, sample_sales_data):
        """Test analysis for all branches"""
        analyzer = MonthlySalesAnalyzer(sample_sales_data)
        results = analyzer.analyze('ALL')
        
        assert results is not None
        assert 'Colombo' in results
        assert 'Kandy' in results
        
        # Check if plot is generated
        assert os.path.exists('monthly_sales.html')
    
    def test_analyze_specific_branch(self, sample_sales_data):
        """Test analysis for specific branch"""
        analyzer = MonthlySalesAnalyzer(sample_sales_data)
        results = analyzer.analyze('Colombo')
        
        assert results is not None
        assert 'Colombo' in results
        assert 'Kandy' not in results 