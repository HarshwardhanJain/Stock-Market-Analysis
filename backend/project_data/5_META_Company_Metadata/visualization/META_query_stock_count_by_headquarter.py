import os
import pandas as pd
import matplotlib.pyplot as plt

# Construct relative path to CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'META_query_stock_count_by_headquarter.csv')

# Read CSV and assign Hive column names
df = pd.read_csv(csv_path)
df.columns = ['headquarter', 'stock_count']

# Sort and take top 10 for better readability
top_df = df.sort_values(by='stock_count', ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.barh(top_df['headquarter'], top_df['stock_count'], color='steelblue')
plt.xlabel('Stock Count')
plt.title('Top 10 Headquarters by Number of Stocks')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Add data labels
for bar in bars:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width())}", va='center')

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'META_query_stock_count_by_headquarter.png')
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
