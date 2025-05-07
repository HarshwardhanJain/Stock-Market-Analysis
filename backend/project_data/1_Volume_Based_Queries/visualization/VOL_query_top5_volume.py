import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV using a relative path
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOL_query_top5_volume.csv')
df = pd.read_csv(csv_path)

# Rename columns based on Hive query
df.columns = ['symbol', 'total_volume']

# Sort to ensure correct order (just in case)
df_sorted = df.sort_values(by='total_volume', ascending=False)

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(data=df_sorted, x='symbol', y='total_volume', palette='viridis')

plt.title('Top 5 Stocks by Total Trading Volume')
plt.xlabel('Stock Symbol')
plt.ylabel('Total Volume')
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(__file__), 'VOL_query_top5_volume.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
