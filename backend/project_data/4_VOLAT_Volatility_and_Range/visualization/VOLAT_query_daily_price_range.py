# backend/project_data/4_VOLAT_Volatility_and_Range/visualization/VOLAT_query_daily_price_range.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV with Hive-style column names
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'VOLAT_query_daily_price_range.csv')
df = pd.read_csv(csv_path)
df.columns = ['dt', 'symbol', 'price_range']

# Convert date
df['dt'] = pd.to_datetime(df['dt'])

# Get top 10 entries with highest price range
top_df = df.sort_values('price_range', ascending=False).head(10)

# Create labels with both date and symbol for clarity
top_df['label'] = top_df['symbol'] + '\n' + top_df['dt'].dt.strftime('%Y-%m-%d')

# Plot
plt.figure(figsize=(12, 6))
bars = plt.bar(top_df['label'], top_df['price_range'], color='darkorange')
plt.ylabel('Price Range ($)')
plt.title('Top 10 Highest Daily Price Ranges')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Annotate values
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f"{bar.get_height():.2f}", ha='center', fontsize=9)

# Save output
output_path = os.path.join(os.path.dirname(__file__), 'VOLAT_query_daily_price_range.png')
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
