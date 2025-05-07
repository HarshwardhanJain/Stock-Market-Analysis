# backend/project_data/3_GAIN_Gainers_&_Losers/visualization/GAIN_query_monthly_sector_percent_change.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'GAIN_query_monthly_sector_percent_change.csv')
df = pd.read_csv(csv_path)
df.columns = ['sp.dt', 'sc.sector', 'avg_percent_change']

# Parse dates using auto format
df['sp.dt'] = pd.to_datetime(df['sp.dt'], errors='coerce')

# Drop rows with invalid/missing dates
df = df.dropna(subset=['sp.dt'])

# Grouped line chart by sector
plt.figure(figsize=(12, 6))
for sector in df['sc.sector'].unique():
    sector_df = df[df['sc.sector'] == sector]
    plt.plot(sector_df['sp.dt'], sector_df['avg_percent_change'], label=sector)

plt.title('Monthly Average Percent Change by Sector')
plt.xlabel('Month')
plt.ylabel('Average % Change')
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save image
out_path = os.path.join(os.path.dirname(__file__), 'GAIN_query_monthly_sector_percent_change.png')
plt.savefig(out_path)
plt.close()

print(f"✅ Visualization saved to: {out_path}")
