import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('AP_Industrial_Policy_Dataset.csv')

# Group by 'Year' and 'Industry Name', counting occurrences
grouped_data = data.groupby(['Year', 'Industry Name']).size().unstack(fill_value=0)

# Plotting
grouped_data.plot(kind='pie', subplots=True, figsize=(12, 12), legend=False, autopct='%1.1f%%', layout=(3, 2))
plt.title('Industry Count by Year')
plt.xlabel('Year')
plt.ylabel('Count of Industries')
plt.tight_layout()
plt.show()
