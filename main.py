import sys
import os
from src.data_loader import DataLoader
from src.analyzers.monthly_sales_analyzer import MonthlySalesAnalyzer
from src.analyzers.price_analyzer import PriceAnalyzer
from src.analyzers.weekly_sales_analyzer import WeeklySalesAnalyzer
from src.analyzers.product_preference_analyzer import ProductPreferenceAnalyzer
from src.analyzers.sales_distribution_analyzer import SalesDistributionAnalyzer
from typing import Union, List

class SalesAnalysisSystem:
    def __init__(self):
        self.data = None

    def load_data(self, file_path: str):
        loader = DataLoader()
        self.data = loader.load_data(file_path)
        if self.data is None:
            print(f"Error: Could not load data from {file_path}")
            sys.exit(1)
        else:
            print(f"Successfully loaded data from {file_path}")

    def show_menu(self):
        print("\nSales Analysis System")
        print("1. Monthly Sales Analysis by Branch")
        print("2. Price Analysis by Product")
        print("3. Weekly Sales Analysis")
        print("4. Product Preference Analysis")
        print("5. Sales Distribution Analysis")
        print("6. Exit")

    def get_branch_selection(self, analyzer: MonthlySalesAnalyzer) -> Union[str, List[str]]:
        """Get branch selection from user"""
        available_branches = analyzer.get_available_branches()
        
        print("\nBranch Selection:")
        print("0. All Branches")
        for i, branch in enumerate(available_branches, 1):
            print(f"{i}. {branch}")
            
        while True:
            try:
                choice = int(input("\nEnter branch selection (0 for all): "))
                if choice == 0:
                    return 'ALL'
                elif 1 <= choice <= len(available_branches):
                    return available_branches[choice - 1]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def run_analysis(self, choice: int):
        """Run the selected analysis"""
        if self.data is None:
            print("Please load data first!")
            return
            
        if choice == 1:
            analyzer = MonthlySalesAnalyzer(self.data)
            selected_branches = self.get_branch_selection(analyzer)
            results = analyzer.analyze(selected_branches)
            self.display_monthly_sales(results)
            print("\nPlot has been saved as 'monthly_sales.html'")
            
        elif choice == 2:
            analyzer = PriceAnalyzer(self.data)
            results = analyzer.analyze()
            print("\nPrice analysis results:")
            for item in results:
                print(f"\nProduct: {item['Product Name']} ({item['Brand']})")
                print(f"Average Price: Rs.{item['mean']:,.2f}")
            print("\nPlot has been saved as 'price_analysis.html'")
            
        elif choice == 3:
            analyzer = WeeklySalesAnalyzer(self.data)
            results = analyzer.analyze()
            print("\nWeekly sales analysis complete.")
            print("Plot has been saved as 'weekly_sales.html'")
            
        elif choice == 4:
            analyzer = ProductPreferenceAnalyzer(self.data)
            results = analyzer.analyze()
            print("\nTop 10 Most Sold Products:")
            for item in results[:10]:
                print(f"{item['Product Name']}: {item['Quantity']} units")
            print("\nPlot has been saved as 'product_preference.html'")
            
        elif choice == 5:
            analyzer = SalesDistributionAnalyzer(self.data)
            stats = analyzer.analyze()
            print("\nSales Distribution Statistics:")
            print(f"Mean Sales: Rs.{stats['mean']:,.2f}")
            print(f"Median Sales: Rs.{stats['median']:,.2f}")
            print(f"Standard Deviation: Rs.{stats['std']:,.2f}")
            print(f"Range: Rs.{stats['min']:,.2f} - Rs.{stats['max']:,.2f}")
            print("\nPlot has been saved as 'sales_distribution.html'")
                
    def display_monthly_sales(self, results: dict):
        """Display monthly sales results"""
        for branch, sales in results.items():
            print(f"\n{branch} Monthly Sales:")
            for period, amount in sales.items():
                print(f"{period}: Rs. {amount:,.2f}")

    def run(self):
        """Main application loop"""
        print("Welcome to Sales Analysis System!")
        self.load_data("data/pos_sales_data.csv")
        
        while True:
            self.show_menu()
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if choice == 6:
                    print("Thank you for using Sales Analysis System!")
                    break
                elif 1 <= choice <= 5:
                    self.run_analysis(choice)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    system = SalesAnalysisSystem()
    system.run()

if __name__ == "__main__":
    main()