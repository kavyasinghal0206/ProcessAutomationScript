import pandas as pd
from datetime import datetime

# Load data
df = pd.read_excel("data/transactions.xlsx")

# Clean data
df.drop_duplicates(inplace=True)
df = df[df['Amount'] > 0]  # Keep only positive amounts
df.dropna(inplace=True)

# Anomaly detection example: flag large transactions (> 1500)
anomalies = df[df['Amount'] > 1500]

# Summarize amounts by Status
summary = df.groupby("Status")["Amount"].sum().reset_index()

# Save output to Excel with timestamp
output_file = f"output/processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    anomalies.to_excel(writer, sheet_name="Anomalies", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

print(f"Process completed. Output saved to {output_file}")
