import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("apple_quality_with_prices.csv")
print(df.columns)
# Clean up negative values
columns_to_clean = ['Acidity', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness']
for col in columns_to_clean:
    df[col] = df[col].apply(lambda x: 0 if x < 0 else x)

# Remove rows with negative values in Size and Weight
numeric_columns = ['Size', 'Weight']
df_cleaned = df[df[numeric_columns].ge(0).all(axis=1)].round(2)

# Add price column
df_cleaned['Price'] = np.random.uniform(5, 10, size=len(df_cleaned))
df_cleaned['Price'] = df_cleaned['Price'].round(2)

# Save the updated DataFrame back to CSV
df_cleaned.to_csv('apple_quality_with_prices.csv', index=False)

print(df_cleaned)
print("Price column added successfully!")

# Drop 'Quality' and 'A_id' columns
df_cleaned = df_cleaned.drop(['Quality', 'A_id'], axis=1)
print(df_cleaned.columns)

# Compute the correlation matrix
correlation_matrix = df_cleaned.corr()

# Plot the heatmap
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix between Apple Characteristics and Price')
plt.tight_layout()  # This ensures the entire plot is visible
plt.show()
