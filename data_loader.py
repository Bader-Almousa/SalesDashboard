import pandas as pd

def load_sales_data(file_path):
    """Load sales data from an Excel file."""
    try:
        data = pd.read_excel(file_path, parse_dates=['Date'])  # استخدام read_excel بدلاً من read_csv
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading the Excel file: {e}")
        return None

def summarize_data(data):
    """Summarize sales data for a quick overview."""
    summary = data.groupby('Product').agg(
        total_sales=('Sales', 'sum'),
        avg_sales=('Sales', 'mean'),
        total_marketing_spend=('Marketing Spend', 'sum')
    ).reset_index()
    return summary
