import os
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV using relative path
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_max_min_close.csv')
df = pd.read_csv(csv_path)
df.columns = ['symbol', 'max_close', 'min_close']

# Sort by max_close for better presentation
df = df.sort_values(by='max_close', ascending=False)

# Optional: Limit to top 15 symbols for clarity
df_top = df.head(15)

# Plot
x = range(len(df_top))
plt.figure(figsize=(14, 6))
bar_width = 0.4

plt.bar(x, df_top['max_close'], width=bar_width, label='Max Close', color='green')
plt.bar([i + bar_width for i in x], df_top['min_close'], width=bar_width, label='Min Close', color='red')

plt.xlabel('Symbol')
plt.ylabel('Close Price')
plt.title('Max vs Min Close Price by Symbol')
plt.xticks([i + bar_width / 2 for i in x], df_top['symbol'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_max_min_close.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
