import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
data = sns.load_dataset('titanic')
#print(data)
# Count missing values in each column
missing_values = data.isnull().sum()
print(missing_values)

# Calculate the mode for 'Age' and 'Cabin'
age_mode = data['age'].mode()[0]  # mode() returns a Series, so we take the first element


# Replace missing values with the mode
data['age'] = data['age'].fillna(age_mode)  # Assign the result back to the column
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])  # Assign the result back to the column


# Verify if missing values have been filled
print(data[['age','embarked']].isnull().sum())
#print(data['age','embarked_town'])
# Encode categorical features (Sex and Embarked)
label_encoder = LabelEncoder()
data['sex'] = label_encoder.fit_transform(data['sex'])
data['embarked'] = label_encoder.fit_transform(data['embarked'])
# Display data types of each column
print(data.dtypes)
# Select features and target

X = data[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]
y = data['survived']

# Create a Logistic Regression model
model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))

# Apply 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)

# Display the cross-validation scores and the average score
print("Cross-validation scores for each fold:", cv_scores)
print("Average cross-validation score:", cv_scores.mean())
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
