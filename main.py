
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

COLUMNS = ["Date", "Product", "Region", "Quantity", "Amount"]


# 1. Enter Sales Data
def get_sales_data():
    records = []
    seen_records = set()

    print("\nEnter sales data.")
    print("Press Enter without entering a date to finish.")

    i = 1

    while True:
        print(f"\nEnter details for Row {i}:")

        date = input("Date (YYYY-MM-DD): ").strip()

        # Stop data entry when date is blank
        if not date:
            break

        product = input("Product: ").strip()
        region = input("Region: ").strip()
        quantity = input("Quantity: ").strip()
        amount = input("Amount: ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Row {i} skipped: invalid Date '{date}'")
            i += 1
            continue

        if not product:
            print(f"Row {i} skipped: invalid Product '{product}'")
            i += 1
            continue

        if not region:
            print(f"Row {i} skipped: invalid Region '{region}'")
            i += 1
            continue

        try:
            quantity_value = int(quantity)
            if quantity_value <= 0:
                raise ValueError
        except ValueError:
            print(f"Row {i} skipped: invalid Quantity '{quantity}'")
            i += 1
            continue

        try:
            amount_value = float(amount)
            if amount_value < 0:
                raise ValueError
        except ValueError:
            print(f"Row {i} skipped: invalid Amount '{amount}'")
            i += 1
            continue

        record = {
            "Date": date,
            "Product": product,
            "Region": region,
            "Quantity": quantity_value,
            "Amount": amount_value
        }

        record_key = tuple(record[col] for col in COLUMNS)

        if record_key in seen_records:
            print(f"Row {i} skipped: Duplicate record")
            i += 1
            continue

        seen_records.add(record_key)
        records.append(record)
        i += 1

    return pd.DataFrame(records, columns=COLUMNS)


# 2. Select Number of Rows
def choose_rows(df):
    if df.empty:
        print("\nNo valid sales data available.")
        return df

    while True:
        choice = input(
            "\nEnter number of rows to analyze "
            "(Press Enter for all rows): "
        ).strip()

        if choice == "":
            return df

        try:
            count = int(choice)

            if count <= 0:
                print("Enter a number greater than 0.")
            elif count > len(df):
                print(f"Only {len(df)} valid rows are available.")
            else:
                return df.head(count)

        except ValueError:
            print("Please enter a valid whole number.")


# 3. Best Selling Product
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


# 4. Sales Summary
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

    best_selling_product(df)


# 5. Group Analysis
def group_analysis(df):
    if df.empty:
        print("\nNo valid sales data available.")
        return

    print("\n--- Sales by Product ---")
    product_sales = df.groupby("Product")["Amount"].sum()
    print(product_sales)

    print("\n--- Sales by Region ---")
    region_sales = df.groupby("Region")["Amount"].sum()
    print(region_sales)

    print("\n--- Product and Region Analysis ---")
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


# 6. Main Menu
def main():
    print("================================")
    print("       SALES DATA ANALYZER")
    print("================================")

    df = get_sales_data()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Sales Summary")
        print("2. Group by Product and Region")
        print("3. Enter New Sales Data")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            selected_df = choose_rows(df)
            sales_summary(selected_df)

        elif choice == "2":
            selected_df = choose_rows(df)
            group_analysis(selected_df)

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


if __name__ == "__main__":
    main()
