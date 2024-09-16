from data_loader import load_sales_data, summarize_data
from data_visualization import plot_sales_over_time, plot_sales_vs_marketing, plot_sales_by_region

def main():
    # تحديث المسار ليكون المسار المطلق أو التأكد من المسار النسبي الصحيح
    file_path = 'data/sales_data.xlsx'  # تأكد من أن المسار صحيح ويشير إلى ملف البيانات Excel

    # تحميل البيانات
    sales_data = load_sales_data(file_path)

    if sales_data is not None:
        # تلخيص البيانات
        summary = summarize_data(sales_data)
        print("Summary of Sales Data:")
        print(summary)

        # عرض التصورات
        plot_sales_over_time(sales_data)
        plot_sales_vs_marketing(sales_data)
        plot_sales_by_region(sales_data)
    else:
        print("Error loading sales data.")

if __name__ == "__main__":
    main()
