
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

COLUMNS = ["Date", "Product", "Region", "Quantity", "Amount"]


# 1. Enter Sales Data
def get_sales_data():
    records = []
    seen_records = set()

    while True:
        try:
            rows = int(input("\nHow many rows of sales data do you want to enter? "))

            if rows > 0:
                break

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(1, rows + 1):

        print(f"\nEnter details for Row {i}:")

        date = input("Date (YYYY-MM-DD): ").strip()
        product = input("Product: ").strip()
        region = input("Region: ").strip()
        quantity = input("Quantity: ").strip()
        amount = input("Amount: ").strip()

        # Validate Date
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Row {i} skipped: invalid Date '{date}'")
            continue

        # Validate Product
        if not product:
            print(f"Row {i} skipped: invalid Product '{product}'")
            continue

        # Validate Region
        if not region:
            print(f"Row {i} skipped: invalid Region '{region}'")
            continue

        # Validate Quantity
        try:
            quantity_value = int(quantity)

            if quantity_value <= 0:
                raise ValueError

        except ValueError:
            print(f"Row {i} skipped: invalid Quantity '{quantity}'")
            continue

        # Validate Amount
        try:
            amount_value = float(amount)

            if amount_value < 0:
                raise ValueError

        except ValueError:
            print(f"Row {i} skipped: invalid Amount '{amount}'")
            continue

        # Store Valid Record
        record = {
            "Date": date,
            "Product": product,
            "Region": region,
            "Quantity": quantity_value,
            "Amount": amount_value
        }

        record_key = tuple(record[col] for col in COLUMNS)

        # Check Duplicate
        if record_key in seen_records:
            print(f"Row {i} skipped: Duplicate record")
            continue

        seen_records.add(record_key)
        records.append(record)

    return pd.DataFrame(records, columns=COLUMNS)


# 2. Best Selling Product
def best_selling_product(df):

    if df.empty:
        print("\nNo sales data available.")
        return

    product_sales = df.groupby("Product")["Quantity"].sum()

    highest_sales = product_sales.max()

    best_products = product_sales[
        product_sales == highest_sales
    ]

    print("\n--- BEST SELLING PRODUCT ---")

    for product, quantity in best_products.items():
        print(f"Product: {product}")
        print(f"Total Quantity Sold: {quantity}")


# 3. Sales Summary
def sales_summary(df):

    if df.empty:
        print("\nNo valid sales data available.")
        return

    total_revenue = df["Amount"].sum()
    transactions = len(df)

    print("\n--- SALES SUMMARY ---")

    print(f"Total Revenue: {total_revenue:g}")
    print(f"Transactions: {transactions}")
    print(f"Total Units Sold: {df['Quantity'].sum()}")

    # Display Best Selling Product
    best_selling_product(df)


# 4. Group Analysis
def group_analysis(df):

    if df.empty:
        print("\nNo valid sales data available.")
        return

    # Sales by Product
    print("\n--- SALES BY PRODUCT ---")

    product_sales = df.groupby("Product")["Amount"].sum()
    print(product_sales)

    # Sales by Region
    print("\n--- SALES BY REGION ---")

    region_sales = df.groupby("Region")["Amount"].sum()
    print(region_sales)

    # Product and Region Analysis
    print("\n--- PRODUCT AND REGION ANALYSIS ---")

    pivot = pd.pivot_table(
        df,
        values="Amount",
        index="Product",
        columns="Region",
        aggfunc="sum",
        fill_value=0
    )

    print(pivot)

    # Product Sales Chart
    product_sales.plot(
        kind="bar",
        title="Revenue by Product"
    )

    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

    # Region Sales Chart
    region_sales.plot(
        kind="bar",
        title="Revenue by Region"
    )

    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()


# 5. Main Menu
def main():

    print("================================")
    print("       SALES DATA ANALYZER")
    print("================================")

    # Enter Sales Data
    df = get_sales_data()

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Sales Summary")
        print("2. Group by Product and Region")
        print("3. Enter New Sales Data")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            # Automatically Analyze All Valid Rows
            sales_summary(df)

        elif choice == "2":

            # Automatically Analyze All Valid Rows
            group_analysis(df)

        elif choice == "3":

            new_data = get_sales_data()

            if not new_data.empty:
                df = pd.concat(
                    [df, new_data],
                    ignore_index=True
                ).drop_duplicates()

        elif choice == "4":

            print("\nThank you for using Sales Data Analyzer!")
            break

        else:

            print("\nInvalid choice. Please select 1 to 4.")


# Run Program
if __name__ == "__main__":
    main()
