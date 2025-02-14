import plotly.graph_objects as go
from .base_analyzer import BaseAnalyzer

class ProductPreferenceAnalyzer(BaseAnalyzer):
    def analyze(self) -> dict:
        if not self.validate_data():
            return {"error": "No data available"}
            
        # Aggregate product sales
        product_sales = self.data.groupby(['Product Name', 'Product Category'])['Quantity'].sum().reset_index()
        
        # Get top 10 products
        top_10_products = product_sales.nlargest(10, 'Quantity')
        
        # Create bar chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=top_10_products['Product Name'],
            y=top_10_products['Quantity'],
            text=top_10_products['Quantity'],
            textposition='auto',
        ))
        
        fig.update_layout(
            title='Top 10 Most Sold Products',
            xaxis_title='Product Name',
            yaxis_title='Quantity Sold',
            xaxis={'tickangle': 45}
        )
        
        # Save interactive plot
        fig.write_html('product_preference.html')
        
        return product_sales.to_dict('records') 