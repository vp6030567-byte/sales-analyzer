# Sales Data Analyzer

A Python command-line project that collects sales records from the user, analyzes the entered data, and displays charts.

## Features

- Enter any positive number of sales records interactively.
- Capture date, product, region, quantity, and amount for each record.
- Validate dates, product/region names, quantities, and amounts.
- Remove duplicate records from the entered dataset.
- Choose how many records to analyze, or press Enter to use the complete dataset.
- Calculate total revenue, transaction count, and total units sold.
- Display the top five products by quantity sold.
- Group sales by product, region, and product-region combination.
- Display bar and line charts using Matplotlib.
- Enter a new dataset without restarting the program.

## Project structure

```text
Sales-Data-Analyzer/
├── main.py
├── README.md
└── summary.md
```

## Requirements

- Python 3.9 or later recommended
- pandas
- matplotlib

## Installation

Open a terminal in this project folder and run:

```bash
python -m pip install pandas matplotlib
```

## Run the project

```bash
python main.py
```

The program asks how many sales records you want to enter. For each record, enter:

1. Date in `YYYY-MM-DD` format
2. Product name
3. Region
4. Quantity (positive whole number)
5. Amount (zero or greater)

After entering the records, choose an option from the main menu. For each analysis, enter the number of rows to analyze. Press Enter without typing a number to analyze all entered records.

## Example data

You can enter these sample records manually:

| Date | Product | Region | Quantity | Amount |
|---|---|---|---:|---:|
| 2026-11-01 | Laptop | North | 2 | 100000 |
| 2026-11-02 | Mouse | South | 10 | 5000 |
| 2026-11-03 | Keyboard | East | 5 | 7500 |

## Notes

- This version takes input directly from the user; it does not require a CSV file.
- The row limit selects the first N valid, unique records from the current data-entry session.
- Charts open in separate Matplotlib windows.
