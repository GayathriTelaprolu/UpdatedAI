import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

 # Import LabelEncoder
from sklearn.metrics import accuracy_score

df=pd.read_csv('Loan_default.csv')

print(df.info())
pd.set_option('display.max_columns',None)
print(df.describe())

# Ensure 'default' is numeric; if it's categorical, convert it to numeric
df['Default'] = pd.to_numeric(df['Default'], errors='coerce')

# Calculate the correlation matrix including only numeric variables
correlation_matrix = df.select_dtypes(include='number').corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".3f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix Heatmap')
plt.show()

X = df[['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed', 'NumCreditLines']]
y = df['Default']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fit the logistic regression model with increased max_iter
model = LogisticRegression(max_iter=200)  # Increase max_iter
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
