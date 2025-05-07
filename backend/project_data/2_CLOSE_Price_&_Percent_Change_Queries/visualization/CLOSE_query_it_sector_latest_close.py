import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Construct CSV path
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_it_sector_latest_close.csv')

# Load and assign column names
df = pd.read_csv(csv_path)
df.columns = ['sp.symbol', 'sp.close', 'sc.sector', 'sp.dt']

# Sort by close price
df_sorted = df.sort_values(by='sp.close', ascending=True)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df_sorted, x='sp.close', y='sp.symbol', palette='Blues_r')

plt.title('Latest Closing Prices - Information Technology Sector')
plt.xlabel('Closing Price')
plt.ylabel('Stock Symbol')
plt.tight_layout()

# Save figure
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_it_sector_latest_close.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
