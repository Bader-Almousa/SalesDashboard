import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_over_time(data):
    """Plot sales over time."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Date', y='Sales', hue='Product', marker='o')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_sales_vs_marketing(data):
    """Plot sales vs marketing spend."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Marketing Spend', y='Sales', hue='Product', size='Sales', sizes=(40, 400), alpha=0.7)
    plt.title('Sales vs Marketing Spend')
    plt.xlabel('Marketing Spend')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.show()

def plot_sales_by_region(data):
    """Plot total sales by region."""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x='Region', y='Sales', hue='Product')
    plt.title('Total Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.show()