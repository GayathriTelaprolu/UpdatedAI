import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv(r'C:\Users\HP\Python_module\project\cleaned_dailyActivity.csv')  # Changed readcsv to read_csv and used raw string
pd.set_option('display.max_columns',None)
print(df.describe())

# Calculate the correlation matrix excluding 'Id'
correlation_matrix = df.drop(columns=['Id','ActivityDate']).corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Prepare data for linear regression
X = df.drop(columns=['Id', 'Calories','ActivityDate'])  # Independent variables
y = df['Calories']  # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform linear regression
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Create a scatter plot of actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Line for perfect prediction
plt.title('Actual vs Predicted Total Active Minutes')
plt.xlabel('Actual Total Active Minutes')
plt.ylabel('Predicted Total Active Minutes')
plt.show()

# Print the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Optionally, you can evaluate the model on the test set
score = model.score(X_test, y_test)
print("Model R^2 score:", score)
