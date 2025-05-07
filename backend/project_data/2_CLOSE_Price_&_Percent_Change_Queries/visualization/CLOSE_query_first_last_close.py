import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_first_last_close.csv')
df = pd.read_csv(csv_path)

# Assign column names
df.columns = ['symbol', 'first_close', 'last_close']

# Take top 15 stocks by last_close for clearer plot
df_top = df.sort_values(by='last_close', ascending=False).head(15)

# Melt for grouped bar plot
df_melted = df_top.melt(id_vars='symbol', value_vars=['first_close', 'last_close'],
                        var_name='Close Type', value_name='Price')

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=df_melted, x='symbol', y='Price', hue='Close Type', palette='Set2')

plt.title('First vs Last Closing Price per Stock')
plt.xlabel('Stock Symbol')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_first_last_close.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
