import pandas as pd
import matplotlib.pyplot as plt

#Load
dengue = pd.read_csv('dengue.csv')
print(dengue.columns.tolist())

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

#Units to remove
dengue_10k = dengue[dengue['unit'] == "N/100000"]
print(dengue_10k.head())

#Select notification rate
notif_rate = dengue_10k[dengue_10k['indicator'] == 'Notification rate']
print(notif_rate.head())

#Top 10 countries per year
notif_rate_sorted = notif_rate.sort_values(by=['time', 'numvalue'], ascending=[True, False])
top10_each_year = notif_rate_sorted.groupby('time').head(10).reset_index(drop=True)
top_countries = (top10_each_year['regionname'].value_counts().head(5).index)
dengue_highest = top10_each_year[top10_each_year['regionname'].isin(top_countries)]

#plot
plt.figure(figsize=(10, 6))

for country in dengue_highest['regionname'].unique():
    d = dengue_highest[dengue_highest['regionname'] == country]
    plt.plot(d['time'], d['numvalue'], marker='o', label=country)

plt.xlabel("Year")
plt.ylabel("Dengue cases per 100,000 inhabitants")
plt.title("Autochthonous dengue incidence over time in selected European countries")
plt.legend(title="Country")
plt.grid(True)
plt.show()

