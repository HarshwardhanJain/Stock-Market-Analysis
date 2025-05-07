# backend/project_data/3_GAIN_Gainers_&_Losers/visualization/GAIN_query_healthcare_top_gains.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# Construct path to the CSV output file
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'GAIN_query_healthcare_top_gains.csv')

# Load the CSV
df = pd.read_csv(csv_path)

# Set column names as per Hive query
df.columns = ['sp.dt', 'sp.symbol', 'sc.security', 'percent_gain']

# Convert date column
df['sp.dt'] = pd.to_datetime(df['sp.dt'])

# Plot
plt.figure(figsize=(12, 6))
plt.barh(df['sc.security'], df['percent_gain'], color='seagreen')
plt.xlabel('Percent Gain (%)')
plt.title('Top 10 Percent Gainers in Health Care Sector')
plt.gca().invert_yaxis()  # highest at the top
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(__file__), 'GAIN_query_healthcare_top_gains.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
