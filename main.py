
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

COLUMNS = ["Date", "Product", "Region", "Quantity", "Amount"]


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

        # Validate date
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Row {i} skipped: invalid Date '{date}'")
            continue

        # Validate product
        if not product:
            print(f"Row {i} skipped: invalid Product '{product}'")
            continue

        # Validate region
        if not region:
            print(f"Row {i} skipped: invalid Region '{region}'")
            continue

        # Validate quantity
        try:
            quantity_value = int(quantity)
            if quantity_value <= 0:
                print(f"Row {i} skipped: invalid Quantity '{quantity}'")
                continue
        except ValueError:
            print(f"Row {i} skipped: invalid Quantity '{quantity}'")
            continue

        # Validate amount
        try:
            amount_value = float(amount)
            if amount_value < 0:
                print(f"Row {i} skipped: invalid Amount '{amount}'")
                continue
        except ValueError:
            print(f"Row {i} skipped: invalid Amount '{amount}'")
            continue

        record = {
            "Date": date,
            "Product": product,
            "Region": region,
            "Quantity": quantity_value,
            "Amount": amount_value
        }

        # Check duplicate records
        record_key = tuple(record[col] for col in COLUMNS)

        if record_key in seen_records:
            print(f"Row {i} skipped: Duplicate record")
            continue

        seen_records.add(record_key)
        records.append(record)

    return pd.DataFrame(records, columns=COLUMNS)


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


def sales_summary(df):
    if df.empty:
        print("\nNo valid sales data available.")
        return

    total_revenue = df["Amount"].sum()
    transactions = len(df)

    print(
        f"\nTotal Revenue: {total_revenue:g} "
        f"| Transactions: {transactions}"
    )

    print(f"Total Units Sold: {df['Quantity'].sum()}")


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

    # Product sales chart
    product_sales.plot(kind="bar", title="Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

    # Region sales chart
    region_sales.plot(
        kind="bar",
        title="Revenue by Region"
    )
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()


def main():
    print("================================")
    print("       SALES DATA ANALYZER")
    print("================================")

    # Enter initial data before the main menu
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

            print("\nNew data entry completed.")

        elif choice == "4":
            print("\nThank you for using Sales Data Analyzer!")
            break

        else:
            print("\nInvalid choice. Please select 1 to 4.")


if __name__ == "__main__":
    main()
