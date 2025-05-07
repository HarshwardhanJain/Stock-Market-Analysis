# backend/project_data/3_GAIN_Gainers_&_Losers/visualization/GAIN_query_top_daily_gainers.py

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Construct relative path to CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'GAIN_query_top_daily_gainers.csv')

# Read CSV and assign Hive column names
df = pd.read_csv(csv_path)
df.columns = ['dt', 'symbol', 'percent_gain']

# Convert date
df['dt'] = pd.to_datetime(df['dt'])

# Sort for clean bar order
df = df.sort_values(by='percent_gain', ascending=True)

# Plot using seaborn
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

ax = sns.barplot(x='percent_gain', y='symbol', data=df, palette='Greens_d')
ax.set_title("📈 Top 10 Daily Gainers", fontsize=16, fontweight='bold')
ax.set_xlabel("Percent Gain (%)", fontsize=12)
ax.set_ylabel("Symbol", fontsize=12)

# Label each bar with the exact value
for i, v in enumerate(df['percent_gain']):
    ax.text(v + 0.5, i, f"{v:.2f}%", va='center', fontsize=10)

# Save figure
output_path = os.path.join(os.path.dirname(__file__), 'GAIN_query_top_daily_gainers.png')
plt.tight_layout()
plt.savefig(output_path, dpi=120)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
