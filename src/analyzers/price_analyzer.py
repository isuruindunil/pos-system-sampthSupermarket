import plotly.graph_objects as go
import plotly.express as px
from .base_analyzer import BaseAnalyzer

class PriceAnalyzer(BaseAnalyzer):
    def analyze(self) -> dict:
        if not self.validate_data():
            return {"error": "No data available"}
            
        # Calculate average price per unit for each product
        price_analysis = self.data.groupby(['Product Name', 'Brand'])['Price Per Unit'].agg([
            'mean', 'min', 'max', 'std'
        ]).reset_index()
        
        # Create box plot
        fig = go.Figure()
        for product in self.data['Product Name'].unique():
            product_data = self.data[self.data['Product Name'] == product]
            fig.add_trace(go.Box(
                y=product_data['Price Per Unit'],
                name=product,
                boxpoints='outliers'
            ))
            
        fig.update_layout(
            title='Price Distribution by Product',
            yaxis_title='Price Per Unit (Rs.)',
            showlegend=False,
            height=800,
            xaxis={'tickangle': 45}
        )
        
        # Save interactive plot
        try:
            fig.write_html('price_analysis.html')
            print("Successfully saved plot to price_analysis.html")
        except Exception as e:
            print(f"Error saving plot: {e}")
        
        return price_analysis.to_dict('records') 