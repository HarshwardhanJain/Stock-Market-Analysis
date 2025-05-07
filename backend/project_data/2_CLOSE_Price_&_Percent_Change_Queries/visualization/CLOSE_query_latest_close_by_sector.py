import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Construct relative path to the CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'CLOSE_query_latest_close_by_sector.csv')

# Load the CSV and rename columns
df = pd.read_csv(csv_path)
df.columns = ['sp.symbol', 'sc.sector', 'sc.security', 'sp.dt', 'sp.close']

# Sort by close price within each sector
df_sorted = df.sort_values(by=['sc.sector', 'sp.close'], ascending=[True, False])

# Optional: limit to top 10 per sector for readability
top_n_per_sector = df_sorted.groupby('sc.sector').head(10)

# Plot using seaborn's facet grid
g = sns.FacetGrid(top_n_per_sector, col="sc.sector", col_wrap=3, height=4, sharex=False)
g.map_dataframe(sns.barplot, x="sp.close", y="sp.symbol", palette="viridis")
g.set_titles(col_template="{col_name}")
g.set_axis_labels("Close Price", "Symbol")

plt.tight_layout()
output_path = os.path.join(os.path.dirname(__file__), 'CLOSE_query_latest_close_by_sector.png')
plt.savefig(output_path)
plt.close()

print(f"✅ Visualization saved to: {output_path}")
