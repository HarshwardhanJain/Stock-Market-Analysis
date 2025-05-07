import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_avg_close_price.csv')
df = pd.read_csv(csv_path)

# Assign column names from Hive query
df.columns = ['symbol', 'avg_close']

# Sort and keep top 20 for visibility
df_top = df.sort_values(by='avg_close', ascending=False).head(20)

# Plot
plt.figure(figsize=(10, 8))
sns.barplot(data=df_top, y='symbol', x='avg_close', palette='coolwarm')

plt.title('Top 20 Stocks by Average Closing Price')
plt.xlabel('Avg Close Price')
plt.ylabel('Stock Symbol')
plt.tight_layout()

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_avg_close_price.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
