import pandas as pd
'''
# Load the dataset
df = pd.read_csv('apple_quality.csv')

# Drop rows with missing values
df_cleaned = df.dropna()

# Convert 'Acidity' to numeric, handling errors
df_cleaned['Acidity'] = pd.to_numeric(df_cleaned['Acidity'], errors='coerce')

# Drop rows where 'Acidity' could not be converted
df_cleaned = df_cleaned.dropna(subset=['Acidity'])




#
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')

# Remove rows where 'Size' or 'Weight' are negative
df_cleaned = df[(df['Size'] >= 0) & (df['Weight'] >= 0)]

# List of columns where negative values should be replaced with 0
columns_to_replace = ['Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']

# Convert columns to numeric and replace negative values with 0
for col in columns_to_replace:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')  # Convert to numeric, set errors as NaN
    df_cleaned.loc[df_cleaned[col] < 0, col] = 0 
# Ensure 'A_id' column values are integers
df_cleaned['A_id'] = df_cleaned['A_id'].astype(int)

# Round all float columns to 2 decimal places
float_columns = df_cleaned.select_dtypes(include=['float64']).columns
df_cleaned[float_columns] = df_cleaned[float_columns].round(2)


# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_fruit_data.csv', index=False)

print("The cleaned dataset has been saved to 'cleaned_fruit_data.csv'.")

'''
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load dataset (replace 'your_dataset.csv' with the actual dataset file)
df = pd.read_csv('cleaned_fruit_data.csv')

# Display first few rows of the dataset
print("Dataset Head:\n", df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Drop any rows with missing values (optional, if needed)
df.dropna(inplace=True)

# 1. Calculate the Price based on a formula (example formula, modify as needed)
# Example: price = (weight * 0.3) + (sweetness * 0.2) + (juiciness * 0.2) + (crunchiness * 0.1) + (size * 0.2)
df['Price'] = ((df['Weight'] * 0.3) + (df['Sweetness'] * 0.2) + (df['Juiciness'] * 0.2) + (df['Crunchiness'] * 0.1) + (df['Size'] * 0.2)).round(2)

# Display the updated dataset with the calculated Price column
print("\nDataset with Price:\n", df.head())

# 2. Drop the 'Quality' column for correlation analysis
df_without_quality = df.drop(columns=['Quality','A_id'])

# 3. Correlation Analysis - Check how each factor (excluding quality) is correlated with price
correlation_matrix = df_without_quality.corr()
print("\nCorrelation Matrix (Excluding Quality,A_id):\n", correlation_matrix['Price'])


# Check for NaN values
if df[['Sweetness', 'Price']].isnull().any().any():
    print("There are NaN values in the dataset. Please clean the data.")
else:
    # Split data into two groups based on Sweetness
    mean_sweetness = df['Sweetness'].mean()
    high_sweetness = df[df['Sweetness'] >= mean_sweetness]['Price']
    low_sweetness = df[df['Sweetness'] < mean_sweetness]['Price']
    
    # Check if both groups have sufficient data
    if len(high_sweetness) == 0 or len(low_sweetness) == 0:
        print("One of the groups is empty. Please check the Sweetness values.")
    else:
        # Perform T-Test
        t_stat, p_value = stats.ttest_ind(high_sweetness, low_sweetness)
        print(f"\nT-Test Results:\nT-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")

 
alpha = 0.05  # significance level
if p_value < alpha:
    print("Reject the null hypothesis for Sweetness: It significantly affects price.")
else:
    print("Fail to reject the null hypothesis for Sweetness: No significant effect on price.")


# Visualizing Correlation with Price
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix[['Price']], annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Price and Features (Excluding Quality,A_id)')
plt.show()
df.to_csv('updated_dataset_with_price.csv', index=False)


'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Load dataset (replace 'your_dataset_with_price.csv' with the actual dataset)
try:
    df = pd.read_csv('updated_dataset_with_price.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The dataset file could not be found.")
except pd.errors.EmptyDataError:
    print("Error: The dataset file is empty.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")

# Check if necessary columns are present (conditional statement)
required_columns = ['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Price']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing columns in the dataset: {missing_columns}")

# Handle missing or invalid data (conditional statements)
if df.isnull().sum().sum() > 0:
    print("Dataset contains missing values. Filling missing values with the mean.")
    df.fillna(df.mean(), inplace=True)

# Define the features (X) and target (y)
X = df[['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness']]
y = df['Price']

# Split the dataset into training and testing sets
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
except ValueError as ve:
    print(f"Error in splitting data: {ve}")
    raise

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
try:
    model.fit(X_train, y_train)
    print("Model training completed successfully.")
except Exception as e:
    print(f"Error during model training: {e}")
    raise

# Predict on the test set
try:
    y_pred = model.predict(X_test)
except Exception as e:
    print(f"Error during prediction: {e}")
    raise

# Evaluate the model
try:
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared Score: {r2}")
except Exception as e:
    print(f"Error in evaluation: {e}")



# Scatter Plot: Actual Price vs Predicted Price
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
plt.title('Scatter Plot of Actual Price vs Predicted Price')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()


