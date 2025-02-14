import plotly.graph_objects as go
from .base_analyzer import BaseAnalyzer

class WeeklySalesAnalyzer(BaseAnalyzer):
    def analyze(self) -> dict:
        if not self.validate_data():
            return {"error": "No data available"}
            
        # Add week number
        self.data['Week'] = self.data['Date'].dt.isocalendar().week
        self.data['Year'] = self.data['Date'].dt.year
        
        # Aggregate weekly sales
        weekly_sales = self.data.groupby(['Year', 'Week'])['Total Sales Amount'].sum().reset_index()
        weekly_sales['YearWeek'] = weekly_sales['Year'].astype(str) + '-W' + weekly_sales['Week'].astype(str).str.zfill(2)
        
        # Create line chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=weekly_sales['YearWeek'],
            y=weekly_sales['Total Sales Amount'],
            mode='lines+markers',
            name='Weekly Sales'
        ))
        
        fig.update_layout(
            title='Weekly Sales Trend',
            xaxis_title='Week',
            yaxis_title='Total Sales (Rs.)',
            xaxis={'tickangle': 45}
        )
        
        # Save interactive plot
        fig.write_html('weekly_sales.html')
        
        return weekly_sales.to_dict('records') 