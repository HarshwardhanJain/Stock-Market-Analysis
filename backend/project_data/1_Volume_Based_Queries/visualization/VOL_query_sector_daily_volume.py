import os
import pandas as pd
import matplotlib.pyplot as plt

# Construct relative path to the CSV output file
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOL_query_sector_daily_volume.csv')

# Read the output CSV
df = pd.read_csv(csv_path)

# Set column names based on Hive query
df.columns = ['sp.dt', 'sc.sector', 'total_volume']

# Convert date column
df['sp.dt'] = pd.to_datetime(df['sp.dt'])

# Plot
plt.figure(figsize=(12, 6))
for sector in df['sc.sector'].unique():
    sector_df = df[df['sc.sector'] == sector]
    plt.plot(sector_df['sp.dt'], sector_df['total_volume'], label=sector)

plt.title('Daily Trading Volume by Sector')
plt.xlabel('Date')
plt.ylabel('Total Volume')
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save plot next to script
output_path = os.path.join(os.path.dirname(__file__), 'VOL_query_sector_daily_volume.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
