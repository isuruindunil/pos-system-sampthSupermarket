import pytest
import os
from datetime import datetime
import webbrowser
import sys

def run_tests():
    """Run tests and generate HTML report"""
    try:
        # Get current directory and print it for debugging
        current_dir = os.getcwd()
        print(f"Current directory: {current_dir}")
        
        # Create reports directory if it doesn't exist
        reports_dir = os.path.join(current_dir, 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
            print(f"Created reports directory at: {reports_dir}")
        
        # Generate timestamp for report name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_name = f'test_report_{timestamp}.html'
        report_path = os.path.join(reports_dir, report_name)
        
        print(f"Will generate report at: {report_path}")
        
        # Run tests with coverage and generate HTML report
        args = [
            '-v',
            '--html=' + report_path,
            '--self-contained-html',
            '--cov=src',
            '--cov-report=html:' + os.path.join(reports_dir, 'coverage'),
            'tests'  # directory containing tests
        ]
        
        exit_code = pytest.main(args)
        
        print(f"pytest exit code: {exit_code}")
        
        # Verify if report was generated
        if os.path.exists(report_path):
            print(f"\nTest report generated successfully at: {report_path}")
            # Automatically open the report in default browser
            webbrowser.open(f'file://{report_path}')
        else:
            print(f"\nError: Report file was not generated at {report_path}")
            # List contents of reports directory
            if os.path.exists(reports_dir):
                print("\nContents of reports directory:")
                for file in os.listdir(reports_dir):
                    print(f"- {file}")
        
        # Print coverage report location
        coverage_path = os.path.join(reports_dir, "coverage", "index.html")
        if os.path.exists(coverage_path):
            print(f"Coverage report generated at: {coverage_path}")
            webbrowser.open(f'file://{coverage_path}')
        else:
            print(f"Coverage report not found at: {coverage_path}")
        
    except Exception as e:
        print(f"Error running tests: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return exit_code

if __name__ == "__main__":
    sys.exit(run_tests()) 