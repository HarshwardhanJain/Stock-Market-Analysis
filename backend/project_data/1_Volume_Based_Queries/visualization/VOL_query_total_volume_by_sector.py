import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV using a relative path
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOL_query_total_volume_by_sector.csv')
df = pd.read_csv(csv_path)

# Rename columns based on Hive query
df.columns = ['sc.sector', 'total_volume']

# Sort by total_volume descending
df_sorted = df.sort_values(by='total_volume', ascending=True)  # ascending for horizontal bar chart

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df_sorted, x='total_volume', y='sc.sector', palette='crest')

plt.title('Total Trading Volume by Sector')
plt.xlabel('Total Volume')
plt.ylabel('Sector')
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(__file__), 'VOL_query_total_volume_by_sector.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
