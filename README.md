# Dengue in Europe — Data Cleaning & Exploratory Analysis

This mini-project demonstrates a complete data analysis workflow using Python and Pandas, applied to a public dataset of dengue incidence in Europe.

The project focuses on data cleaning, transformation, aggregation, and visualization, with the goal of exploring temporal trends at the country level.

---

## Project objectives

- Clean and standardize raw epidemiological data
- Convert key variables to appropriate numeric types
- Remove supranational EU/EEA aggregate entries to ensure country-level analysis
- Identify countries with the highest dengue incidence
- Analyze temporal trends in dengue incidence over time
- Visualize results using line plots

---

## Data overview

- **Time variable:** `time` (year of report)
- **Geographic variable:** `regionname` (country)
- **Metric analyzed:** `numvalue` (dengue cases per 100,000 inhabitants)

EU/EEA aggregate rows were excluded to avoid mixing country-level data with regional summaries.

---

## Methods

The analysis follows these main steps:

1. Load and inspect the dataset
2. Standardize column names
3. Handle missing values in key fields
4. Convert time and incidence variables to numeric formats
5. Filter out EU/EEA aggregate entries
6. Select the top 10 countries by average dengue incidence
7. Aggregate data by country and year
8. Visualize dengue trends over time

---

## Technologies used

- Python
- Pandas
- Matplotlib

---

## How to run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pandas matplotlib

