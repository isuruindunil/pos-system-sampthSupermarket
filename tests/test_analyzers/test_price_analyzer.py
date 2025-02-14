import pytest
from src.analyzers.price_analyzer import PriceAnalyzer
import os

class TestPriceAnalyzer:
    """Unit tests for PriceAnalyzer"""
    
    def test_price_analysis(self, sample_sales_data):
        """Test price analysis calculations"""
        analyzer = PriceAnalyzer(sample_sales_data)
        results = analyzer.analyze()
        
        assert results is not None
        assert len(results) > 0
        assert 'Product Name' in results[0]
        assert 'mean' in results[0]
        
        # Check if plot is generated
        assert os.path.exists('price_analysis.html') 