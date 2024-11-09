import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv(r'C:\Users\HP\Python_module\project\filtered_data_month_1 (1).csv')
print(df.info())
pd.set_option('display.max_columns',None)
print(df.describe())

# Adjust layout to prevent overlap
numeric_cols = ['trip_distance', 'fare_amount', 'tip_amount', 'tolls_amount', 'trip_duration']

plt.figure(figsize=(16, 10))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    sns.scatterplot(x=df[col], y=df['total_amount'], alpha=0.5)
    plt.title(f'Total Amount vs {col}')
    plt.xlabel(col)
    plt.ylabel('Total Amount')

plt.tight_layout()
plt.show()


# Calculate the correlation matrix
correlation_matrix = df.corr()

# Generate a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Prepare the data for linear regression
X = df[['trip_distance', 'fare_amount', 'tip_amount', 'tolls_amount', 'trip_duration']]  # Features
y = df['total_amount']  # Target variable

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the intercept and coefficients
intercept = model.intercept_
coefficients = model.coef_

print(f'Intercept: {intercept}')
print(f'Coefficients: {coefficients}')

# Predict total amount using the model
y_pred = model.predict(X)

# Plotting the actual vs predicted values
plt.figure(figsize=(12, 6))
plt.scatter(y, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')  # Diagonal line
plt.title('Actual vs Predicted Total Amount')
plt.xlabel('Actual Total Amount')
plt.ylabel('Predicted Total Amount')
plt.show()

#


