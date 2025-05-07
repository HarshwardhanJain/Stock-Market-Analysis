import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to Hive output
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_monthly_avg_close.csv')
df = pd.read_csv(csv_path)

# Set expected column names
df.columns = ['month', 'symbol', 'avg_close']

# Try flexible datetime parsing
df['month'] = pd.to_datetime(df['month'], format='mixed', errors='coerce')

# Drop rows where date parsing failed
df = df.dropna(subset=['month'])

# Filter top 5 most frequent symbols for clarity
top_symbols = df['symbol'].value_counts().nlargest(5).index
df_filtered = df[df['symbol'].isin(top_symbols)]

# Plot
plt.figure(figsize=(12, 6))
for symbol in top_symbols:
    symbol_df = df_filtered[df_filtered['symbol'] == symbol]
    plt.plot(symbol_df['month'], symbol_df['avg_close'], label=symbol)

plt.title('Monthly Average Close Price per Symbol')
plt.xlabel('Month')
plt.ylabel('Average Close Price')
plt.legend(title='Symbol', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save graph
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_monthly_avg_close.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
