import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_avg_close_by_sector.csv')
df = pd.read_csv(csv_path)

# Assign column names from Hive query
df.columns = ['sc.sector', 'avg_close_price']

# Sort data
df_sorted = df.sort_values(by='avg_close_price', ascending=False)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=df_sorted, x='sc.sector', y='avg_close_price', palette='Blues_d')

plt.title('Average Closing Price by Sector')
plt.xlabel('Sector')
plt.ylabel('Avg Close Price')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_avg_close_by_sector.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
