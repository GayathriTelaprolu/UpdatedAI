import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Simulating dataset with Fertilizer A and B across different farms
np.random.seed(42)

# Creating random data for 100 farms
data = {
    'Farm_ID': np.arange(1, 101),
    'Fertilizer_Type': np.random.choice(['A', 'B'], size=100),
    'Soil_Type': np.random.choice(['Clay', 'Sandy', 'Loamy'], size=100),
    'Rainfall': np.random.uniform(50, 150, size=100),  # mm
    'Irrigation': np.random.uniform(200, 800, size=100),  # Liters per hectare
    'Yield': np.random.uniform(2000, 4000, size=100)  # kg per hectare
}

# Create a DataFrame
df = pd.DataFrame(data)

# Simulate Fertilizer effect on Yield
df.loc[df['Fertilizer_Type'] == 'A', 'Yield'] += np.random.uniform(0, 200, size=len(df[df['Fertilizer_Type'] == 'A']))
df.loc[df['Fertilizer_Type'] == 'B', 'Yield'] += np.random.uniform(100, 300, size=len(df[df['Fertilizer_Type'] == 'B']))

# Correlation calculation
corr_matrix = df[['Yield', 'Rainfall', 'Irrigation']].corr()

# Plotting correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt='.2f', vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# Scatter plots for correlation between Yield and Rainfall/Irrigation
plt.figure(figsize=(12, 6))

# Scatter plot for Yield vs Rainfall
plt.subplot(1, 2, 1)
sns.scatterplot(x=df['Rainfall'], y=df['Yield'], hue=df['Fertilizer_Type'], palette='coolwarm')
plt.title("Scatter plot of Yield vs Rainfall")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Yield (kg/hectare)")

# Scatter plot for Yield vs Irrigation
plt.subplot(1, 2, 2)
sns.scatterplot(x=df['Irrigation'], y=df['Yield'], hue=df['Fertilizer_Type'], palette='coolwarm')
plt.title("Scatter plot of Yield vs Irrigation")
plt.xlabel("Irrigation (Liters/hectare)")
plt.ylabel("Yield (kg/hectare)")

plt.tight_layout()
plt.show()
