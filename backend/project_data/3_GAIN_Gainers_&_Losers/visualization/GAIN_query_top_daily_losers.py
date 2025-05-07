# backend/project_data/3_GAIN_Gainers_&_Losers/visualization/GAIN_query_top_daily_losers.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# Construct relative path to CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'GAIN_query_top_daily_losers.csv')

# Read CSV and assign Hive column names
df = pd.read_csv(csv_path)
df.columns = ['dt', 'symbol', 'percent_loss']

# Convert date column
df['dt'] = pd.to_datetime(df['dt'])

# Plot as horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(df['symbol'], df['percent_loss'], color='crimson')
plt.xlabel('Percent Loss (%)')
plt.title('Top 10 Daily Losers')
plt.gca().invert_yaxis()  # Show biggest loss on top
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Add labels
for bar in bars:
    plt.text(bar.get_width() - 1.5, bar.get_y() + bar.get_height()/2,
             f"{bar.get_width():.2f}%", va='center', ha='right', color='white', fontsize=9)

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'GAIN_query_top_daily_losers.png')
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
