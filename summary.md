# Project Summary — Sales Data Analyzer

## 1. Overview

Sales Data Analyzer is a Python project that accepts sales information directly from the user and performs basic sales analysis. It uses Pandas for tabular data processing and Matplotlib for charts.

Each sales record contains:
- Date
- Product
- Region
- Quantity
- Amount

## 2. Main features

1. Interactive data entry for multiple sales records.
2. Input validation for date, product, region, quantity, and amount.
3. Duplicate-record removal.
4. User-selected analysis size: enter a row count or press Enter for the complete dataset.
5. Sales summary: total revenue, number of transactions, and total units sold.
6. Top five products based on quantity sold.
7. Product-wise, region-wise, and product-region sales grouping.
8. Bar and line charts.
9. Option to enter a new dataset during the same run.

## 3. Test cases

The following are suggested test cases. Run them in the program and record the actual output from your computer.

| Case | Input / action | Expected behavior |
|---|---|---|
| 1. Normal data entry | Enter 3 valid records with different products and regions | All 3 records are displayed and can be analyzed |
| 2. Selected row count | At the analysis prompt, enter `2` | Analysis uses the first 2 valid unique records |
| 3. Complete dataset | At the analysis prompt, press Enter without typing | Analysis uses all valid unique records in the current session |
| 4. Invalid row count | Enter `abc`, `0`, or a negative number | Program displays an error and asks for the row count again |
| 5. Invalid quantity | Enter text or a quantity less than or equal to zero | Program asks for quantity again |
| 6. Invalid amount | Enter text or a negative amount | Program asks for amount again |
| 7. Invalid date | Enter a date that cannot be parsed | Program asks for the date again |
| 8. Duplicate record | Enter the same complete record twice | Duplicate row is removed from the analysis dataset |
| 9. New data session | Select menu option 3 | Program asks for a new set of sales records |
| 10. Exit | Select menu option 4 | Program exits with a thank-you message |

## 4. Screenshots

Add your own screenshots after running the project. Suggested screenshots:

- **Screenshot 1 — Data entry:** terminal showing the number of records and entered sales fields.
- **Screenshot 2 — Main menu:** menu showing Sales Summary, Group by Product and Region, Enter New Sales Data, and Exit.
- **Screenshot 3 — Sales summary:** output showing revenue, transactions, units sold, and top products.
- **Screenshot 4 — Product and region analysis:** grouped output and chart windows.
- **Screenshot 5 — Full dataset option:** row-count prompt with Enter pressed to analyze all records.
- **Screenshot 6 — Validation:** an invalid input being rejected and requested again.

Paste the screenshots below this section in your final submission. No screenshots are included in this starter repository because none were supplied with the project request.

## 5. Difficulties faced while making the project

The following are project-development issues encountered or relevant to the implementation:

1. **Python library setup:** Pandas and Matplotlib must be installed in the same Python environment used to run the program.
2. **Windows DLL/import issue:** A Windows Application Control policy may block a compiled dependency used by Pandas. This is an environment/security-policy issue, not necessarily a mistake in the Python source code.
3. **CSV file path confusion:** An earlier version loaded `sales.csv`, which caused a file-not-found error when the file was not in the expected folder. The current version avoids this issue by taking data directly from the user.
4. **Input validation:** The program needs to reject invalid dates, non-numeric quantities or amounts, empty product/region names, and invalid row counts.
5. **Choosing analysis size:** The row-count option must support both a selected number of records and the complete dataset when the user presses Enter.
6. **Chart display:** Matplotlib charts open in separate windows, so the user must close a chart window to return to the terminal and continue.

## 6. Technologies used

- Python
- Pandas
- Matplotlib

## 7. Conclusion

The project demonstrates basic data collection, validation, cleaning, grouping, aggregation, and visualization in Python. It allows the user to enter sales data, choose the number of records to analyze, and view numerical summaries and charts.
