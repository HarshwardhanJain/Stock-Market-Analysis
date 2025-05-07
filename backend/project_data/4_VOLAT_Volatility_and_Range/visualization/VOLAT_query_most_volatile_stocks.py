# backend/project_data/4_VOLAT_Volatility_and_Range/visualization/VOLAT_query_most_volatile_stocks.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOLAT_query_most_volatile_stocks.csv')

# Load CSV and set column names as per Hive query
df = pd.read_csv(csv_path)
df.columns = ['symbol', 'avg_daily_range']

# Sort for better visual layout
df = df.sort_values(by='avg_daily_range')

# Plot
plt.figure(figsize=(10, 6))
bars = plt.barh(df['symbol'], df['avg_daily_range'], color='orange')
plt.xlabel('Average Daily Range ($)')
plt.title('Top 10 Most Volatile Stocks')
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Annotate each bar with its value
for bar in bars:
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             f"{bar.get_width():.2f}", va='center')

# Save the figure
output_path = os.path.join(os.path.dirname(__file__), 'VOLAT_query_most_volatile_stocks.png')
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
