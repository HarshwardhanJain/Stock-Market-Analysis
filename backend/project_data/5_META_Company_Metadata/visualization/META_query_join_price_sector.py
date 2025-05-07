import os
import pandas as pd
import matplotlib.pyplot as plt

# Relative path to the CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'META_query_join_price_sector.csv')

# Load CSV and assign column names
df = pd.read_csv(csv_path)
df.columns = ['sp.dt', 'sp.symbol', 'sc.sector', 'sp.open', 'sp.close', 'sp.volume']

# Convert date column
df['sp.dt'] = pd.to_datetime(df['sp.dt'])

# Group by date and sector to compute average close price
avg_close = df.groupby(['sp.dt', 'sc.sector'])['sp.close'].mean().reset_index()

# Plot: Average closing price per sector over time
plt.figure(figsize=(12, 6))
for sector in avg_close['sc.sector'].unique():
    sector_df = avg_close[avg_close['sc.sector'] == sector]
    plt.plot(sector_df['sp.dt'], sector_df['sp.close'], label=sector)

plt.title('Average Closing Price by Sector Over Time')
plt.xlabel('Date')
plt.ylabel('Avg Closing Price ($)')
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(__file__), 'META_query_join_price_sector.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
