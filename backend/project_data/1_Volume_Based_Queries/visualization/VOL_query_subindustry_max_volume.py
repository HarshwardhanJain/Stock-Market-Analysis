import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV using a relative path
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOL_query_subindustry_max_volume.csv')
df = pd.read_csv(csv_path)

# Rename columns to match Hive query
df.columns = ['sc.sub_industry', 'sp.symbol', 'max_volume']

# Sort for better visualization
df_sorted = df.sort_values(by='max_volume', ascending=False).head(30)  # show top 30 for clarity

# Set the plot style
plt.figure(figsize=(12, 8))
sns.barplot(
    data=df_sorted,
    y='sp.symbol',
    x='max_volume',
    hue='sc.sub_industry',
    dodge=False,
    palette='tab20'
)

plt.title('Top 30 Stocks by Max Volume Grouped by Sub-Industry')
plt.xlabel('Max Volume')
plt.ylabel('Stock Symbol')
plt.legend(title='Sub-Industry', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(__file__), 'VOL_query_subindustry_max_volume.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
