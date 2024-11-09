import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Creating a synthetic dataset with 1000 records
np.random.seed(42)

# Creating synthetic data
n = 1000
data = {
    'Income': np.random.randint(30000, 150000, size=n),
    'Loan_Amount': np.random.randint(5000, 50000, size=n),
    'Credit_Score': np.random.randint(300, 850, size=n),  # FICO scores range from 300 to 850
    'Debt_to_Income_Ratio': np.random.uniform(0.1, 0.6, size=n),
    'Education_Level': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], size=n),
    'Default': np.random.choice([0, 1], size=n, p=[0.7, 0.3])  # 70% no default, 30% default
}

df = pd.DataFrame(data)

# WOE Transformation (manually, for simplicity, let's assume for education levels)
df['WOE_Education_Level'] = df['Education_Level'].map({
    'High School': -0.2, 'Bachelors': 0.1, 'Masters': 0.3, 'PhD': 0.5
})

# Selecting feature columns (this includes WOE transformed features)
X = df[['Income', 'Loan_Amount', 'Credit_Score', 'Debt_to_Income_Ratio', 'WOE_Education_Level']]
y = df['Default']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardizing the features (especially important for solvers like liblinear and saga)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression with 'liblinear' solver
logreg = LogisticRegression(solver='liblinear', max_iter=500)  # 'liblinear' handles small datasets and avoids convergence issues
logreg.fit(X_train_scaled, y_train)

# Predicting on the test data
y_pred = logreg.predict(X_test_scaled)

# Accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Checking for multicollinearity using Variance Inflation Factor (VIF)
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

print("\nVIF before addressing multicollinearity:")
print(vif_data)

# Displaying the logistic regression coefficients
print("\nCoefficients of the model:")
print(logreg.coef_)
