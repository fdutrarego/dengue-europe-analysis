import pandas as pd
import matplotlib.pyplot as plt

#Load
dengue = pd.read_csv('dengue.csv')

#Standardize column names
dengue.columns = (dengue.columns.str.strip().str.lower().str.replace(' ', '_'))

# Convert to numeric (invalid values become NaN)
dengue['time'] = pd.to_numeric(dengue['time'], errors='coerce')
dengue['numvalue'] = pd.to_numeric(dengue['numvalue'], errors='coerce')

# Remove rows with missing key fields (including after numeric conversion)
dengue = dengue.dropna(subset= ['unit', 'time', 'regioncode', 'regionname', 'numvalue'])

## Remove EU/EEA aggregate entries (keep only countries)
regions_to_remove = ["EU/EEA (with UK until 2019)", "EU (with UK until 2019)", "EU/EEA (without UK)", "EU (without UK)"]
dengue = dengue[~dengue['regionname'].isin(regions_to_remove)]

# Top 10 countries by average incidence (numvalue)
top_regions = dengue.groupby('regionname')['numvalue'].mean().sort_values(ascending = False).head(10)
dengue_highest = dengue[dengue['regionname'].isin(top_regions.index)]

# Aggregate (country, year) in case multiple entries exist per year
series = (dengue_highest.groupby(['regionname', 'time'])['numvalue'].mean().reset_index().sort_values(['regionname', 'time']))

#plot
plt.figure(figsize=(10, 6))

for country in series['regionname'].unique():
    d = series[series['regionname'] == country]
    plt.plot(d['time'], d['numvalue'], marker='o', label=country)

plt.xlabel("Year")
plt.ylabel("Dengue cases per 100,000 inhabitants")  # ajuste se numvalue for casos absolutos
plt.title("Dengue over time in European countries (top 10 by average incidence)")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("dengue_trends.png", dpi=300, bbox_inches="tight")
