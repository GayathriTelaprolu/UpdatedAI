import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('apple_updated_dataset.csv')  # Replace 'apple_data.csv' with your actual file path

# Display the first few rows of the dataset (optional, for validation)
print(df.head())

# Categorize the price into Low, Medium, and High
def categorize_price(price):
    if price < 7.0:
        return 'Low'
    elif 7.0 <= price <= 8.49:
        return 'Medium'
    else:
        return 'High'

# Apply the categorization function to the Price column
df['Price Category'] = df['Price'].apply(categorize_price)

# Features (Weight, Sweetness, Crunchiness, Juiciness) and target (Price Category)
X = df[['Weight', 'Sweetness', 'Crunchiness', 'Juiciness']]  # Features from the CSV file
y = df['Price Category']  # Target (Actual Price Category)

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Store the actual and predicted categories
X_test['Actual Price Category'] = y_test.values  # Actual values
X_test['Predicted Price Category'] = y_pred      # Predicted values

# Save the actual and predicted categories to a new CSV file
output_csv_path = 'new_dataset.csv'  # Output file name
X_test.to_csv(output_csv_path, index=False)

print(f"Results saved to {output_csv_path}")

# Predict the price category for a new apple
new_apple = [[6, 7, 8, 6]]  # Example: Weight = 6, Sweetness = 7, Crunchiness = 8, Juiciness = 6
predicted_category = model.predict(new_apple)

print(f"Predicted price category for the new apple: {predicted_category[0]}")
predicted_df = pd.DataFrame(y_pred, columns=['Predicted Price Category'])  # Changed 'predictions' to 'y_pred'

# Group by predicted price category and count occurrences
grouped_data = predicted_df['Predicted Price Category'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Predicted Price Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()
