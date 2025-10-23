# ProcessAutomationScript
Python script to automate financial transaction processing
--> Process Automation Script

This Python script automates cleaning, validating, and summarizing financial transaction data.

Features:
- Removes duplicates and invalid data
- Flags anomalies (large transactions)
- Generates summary reports in Excel

How to run:
1. Install dependencies: `pip install pandas openpyxl`
2. Run script: `python automation_script.py`

Input:
- Place your transaction data in `data/transactions.xlsx`

Output:
- Results saved in the `output` folder with timestamped Excel files.
