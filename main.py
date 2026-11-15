import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. TAKE SALES DATA FROM USER
# ==========================================

def get_sales_data():
    while True:
        try:
            n = int(input("\nHow many sales records do you want to enter? "))
            if n > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid whole number.")

    records = []

    for i in range(n):
        print(f"\n========== RECORD {i + 1} ==========")

        while True:
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            parsed_date = pd.to_datetime(date, errors="coerce")
            if pd.notna(parsed_date):
                break
            print("Invalid date. Please use YYYY-MM-DD.")

        while True:
            product = input("Enter Product Name: ").strip()
            if product:
                break
            print("Product name cannot be empty.")

        while True:
            region = input("Enter Region: ").strip()
            if region:
                break
            print("Region cannot be empty.")

        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be greater than zero.")
            except ValueError:
                print("Enter a valid whole number.")

        while True:
            try:
                amount = float(input("Enter Amount: "))
                if amount >= 0:
                    break
                print("Amount cannot be negative.")
            except ValueError:
                print("Enter a valid amount.")

        records.append({
            "Date": parsed_date,
            "Product": product,
            "Region": region,
            "Quantity": quantity,
            "Amount": amount
        })

    df = pd.DataFrame(records).drop_duplicates().reset_index(drop=True)

    print("\nSales data entered successfully!")
    print(f"Valid unique records: {len(df)}")
    print("\n========== ENTERED SALES DATA ==========")
    print(df.to_string(index=False))
    return df


# ==========================================
# 2. SELECT NUMBER OF ROWS TO ANALYZE
# ==========================================

def get_data_by_row_count(df):
    while True:
        print("\nHow many rows do you want to analyze?")
        print("Press Enter to analyze the complete dataset.")
        user_input = input("Enter number of rows: ").strip()

        if user_input == "":
            print("\nAnalyzing complete dataset...")
            return df.copy()

        try:
            rows = int(user_input)
            if rows <= 0:
                print("Enter a positive number.")
                continue
            if rows > len(df):
                print(f"Only {len(df)} records are available.")
                print("Analyzing complete dataset.")
                return df.copy()

            print(f"\nAnalyzing the first {rows} records...")
            return df.head(rows).copy()
        except ValueError:
            print("Invalid input! Enter a number or press Enter.")


# ==========================================
# 3. SALES SUMMARY
# ==========================================

def summary(df):
    if df.empty:
        print("No data available.")
        return

    total_revenue = df["Amount"].sum()
    total_transactions = len(df)
    total_units = df["Quantity"].sum()

    print("\n========== SALES SUMMARY ==========")
    print(f"Total Revenue      : {total_revenue:.2f}")
    print(f"Total Transactions : {total_transactions}")
    print(f"Total Units Sold   : {total_units}")

    print("\n========== TOP 5 PRODUCTS ==========")
    top_products = (
        df.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    print(top_products)

    plt.figure(figsize=(9, 5))
    top_products.plot(
        kind="bar",
        title="Top 5 Best-Selling Products",
        xlabel="Product",
        ylabel="Quantity Sold"
    )
    plt.tight_layout()
    plt.show()

    daily_revenue = df.groupby("Date")["Amount"].sum().sort_index()
    plt.figure(figsize=(9, 5))
    daily_revenue.plot(
        kind="line",
        marker="o",
        title="Daily Sales Revenue",
        xlabel="Date",
        ylabel="Revenue"
    )
    plt.tight_layout()
    plt.show()


# ==========================================
# 4. PRODUCT AND REGION ANALYSIS
# ==========================================

def group_analysis(df):
    if df.empty:
        print("No data available.")
        return

    print("\n========== PRODUCT-WISE SALES ==========")
    product_sales = (
        df.groupby("Product")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    print(product_sales)

    print("\n========== REGION-WISE SALES ==========")
    region_sales = (
        df.groupby("Region")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    print(region_sales)

    print("\n========== PRODUCT AND REGION SALES ==========")
    product_region = df.pivot_table(
        index="Product",
        columns="Region",
        values="Amount",
        aggfunc="sum",
        fill_value=0
    )
    print(product_region)

    plt.figure(figsize=(9, 5))
    region_sales.plot(
        kind="bar",
        title="Region-wise Sales",
        xlabel="Region",
        ylabel="Revenue"
    )
    plt.tight_layout()
    plt.show()

    product_region.plot(
        kind="line",
        marker="o",
        figsize=(9, 5),
        title="Product Sales Across Regions"
    )
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()


# ==========================================
# 5. MAIN MENU
# ==========================================

def main():
    print("======================================")
    print("         SALES DATA ANALYZER")
    print("======================================")

    while True:
        # Start each session by collecting fresh sales records.
        df = get_sales_data()

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Sales Summary")
            print("2. Group by Product and Region")
            print("3. Enter New Sales Data")
            print("4. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                selected_data = get_data_by_row_count(df)
                summary(selected_data)

            elif choice == "2":
                selected_data = get_data_by_row_count(df)
                group_analysis(selected_data)

            elif choice == "3":
                print("\nStarting a new data-entry session...")
                break

            elif choice == "4":
                print("\nThank you for using Sales Data Analyzer!")
                return

            else:
                print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
