import plotly.graph_objects as go
import numpy as np
from .base_analyzer import BaseAnalyzer

class SalesDistributionAnalyzer(BaseAnalyzer):
    def analyze(self) -> dict:
        if not self.validate_data():
            return {"error": "No data available"}
            
        # Create histogram
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=self.data['Total Sales Amount'],
            nbinsx=50,
            name='Sales Distribution'
        ))
        
        fig.update_layout(
            title='Distribution of Total Sales per Transaction',
            xaxis_title='Total Sales Amount (Rs.)',
            yaxis_title='Frequency',
            bargap=0.1
        )
        
        # Add mean and median lines
        mean_sales = self.data['Total Sales Amount'].mean()
        median_sales = self.data['Total Sales Amount'].median()
        
        fig.add_vline(x=mean_sales, line_dash="dash", line_color="red",
                     annotation_text=f"Mean: Rs.{mean_sales:,.2f}")
        fig.add_vline(x=median_sales, line_dash="dash", line_color="green",
                     annotation_text=f"Median: Rs.{median_sales:,.2f}")
        
        # Save interactive plot
        fig.write_html('sales_distribution.html')
        
        # Calculate statistics
        stats = {
            'mean': mean_sales,
            'median': median_sales,
            'std': self.data['Total Sales Amount'].std(),
            'min': self.data['Total Sales Amount'].min(),
            'max': self.data['Total Sales Amount'].max()
        }
        
        return stats 