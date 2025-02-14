from .base_analyzer import BaseAnalyzer
import pandas as pd
import plotly.graph_objects as go
from typing import Union, List

class MonthlySalesAnalyzer(BaseAnalyzer):
    """Analyzer for monthly sales by branch"""
    
    def analyze(self, selected_branches: Union[str, List[str]] = 'ALL') -> dict:
        """
        Analyze monthly sales for selected branches
        Args:
            selected_branches: 'ALL' for all branches or list of branch names
        """
        if not self.validate_data():
            return {"error": "No data available"}
            
        # Add month and year columns
        self.data['Month'] = self.data['Date'].dt.month
        self.data['Year'] = self.data['Date'].dt.year
        self.data['YearMonth'] = self.data['Date'].dt.strftime('%Y-%m')
        
        # Filter branches if specific branches are selected
        df = self.data
        if selected_branches != 'ALL':
            if isinstance(selected_branches, str):
                selected_branches = [selected_branches]
            df = df[df['Branch'].isin(selected_branches)]
        
        # Group by branch and month
        monthly_sales = df.groupby(
            ['Branch', 'YearMonth']
        )['Total Sales Amount'].sum().reset_index()
        
        # Create the plot using Plotly
        fig = go.Figure()
        
        # Add a line for each branch
        for branch in monthly_sales['Branch'].unique():
            branch_data = monthly_sales[monthly_sales['Branch'] == branch]
            fig.add_trace(go.Scatter(
                x=branch_data['YearMonth'],
                y=branch_data['Total Sales Amount'],
                name=branch,
                mode='lines+markers'
            ))
        
        # Update layout
        fig.update_layout(
            title='Monthly Sales by Branch',
            xaxis_title='Month',
            yaxis_title='Sales Amount (Rs.)',
            xaxis={'tickangle': 45},
            height=600,
            showlegend=True,
            legend_title='Branches'
        )
        
        # Save the plot as HTML
        try:
            fig.write_html('monthly_sales.html')
            print("Successfully saved plot to monthly_sales.html")
        except Exception as e:
            print(f"Error saving plot: {e}")
        
        # Format results for return
        results = {}
        for branch in monthly_sales['Branch'].unique():
            branch_data = monthly_sales[monthly_sales['Branch'] == branch]
            results[branch] = {
                month: amount
                for month, amount in zip(
                    branch_data['YearMonth'],
                    branch_data['Total Sales Amount']
                )
            }
            
        return results
    
    def get_available_branches(self) -> List[str]:
        """Get list of all available branches"""
        return sorted(self.data['Branch'].unique().tolist()) 