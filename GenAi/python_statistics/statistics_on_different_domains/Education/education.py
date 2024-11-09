import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv(r'C:\Users\HP\Python_module\project\Student_performance_data _.csv')
print(df.info())
pd.set_option('display.max_columns',None)
print(df.describe())


# Create subplots for each column
columns = ['StudyTimeWeekly', 'Absences', 'ParentalSupport']

# Generate separate boxplots for each column
for i, col in enumerate(columns, 1):
    plt.subplot(3, 2, i)  # Change to 3 rows, 2 columns
    sns.boxplot(data=df, y=col, color='lightblue')
    plt.title(f'Boxplot for {col}')
    plt.ylabel(col)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

average_gpa = df.groupby('ParentalSupport')['GPA'].mean().reset_index()

# Create a bar graph for parental support and average GPA
plt.figure(figsize=(10, 6))
plt.bar(average_gpa['ParentalSupport'], average_gpa['GPA'], color='skyblue')
plt.title('Average GPA by Parental Support')
plt.xlabel('Parental Support')
plt.ylabel('Average GPA')
plt.xticks(rotation=45)  # Rotate x-ticks for better readability
plt.grid(axis='y')
plt.show()


# Assuming 'ParentalSupport' is a categorical variable and 'GPA' is a numeric column in your DataFrame
# Group by 'ParentalSupport' and calculate the mean GPA

# Assuming 'Gender' is encoded as 0 and 1 and 'GPA' is a numeric column
# Group by 'Gender' and calculate the mean GPA
average_gpa_by_gender = df.groupby('Gender')['GPA'].mean().reset_index()

# Map gender labels for better readability
average_gpa_by_gender['Gender'] = average_gpa_by_gender['Gender'].map({0: 'Female', 1: 'Male'})  # Adjust labels as needed

# Create a bar graph for gender and average GPA
plt.figure(figsize=(10, 6))
plt.bar(average_gpa_by_gender['Gender'], average_gpa_by_gender['GPA'], color='lightgreen')
plt.title('Average GPA by Gender')
plt.xlabel('Gender')
plt.ylabel('Average GPA')
plt.xticks(rotation=45)  # Rotate x-ticks for better readability
plt.grid(axis='y')
plt.show()
import seaborn as sns

# ... existing code ...

# Exclude 'Student ID' and 'Grade Class' columns
df_filtered = df.drop(columns=['StudentID', 'GradeClass'])

# Calculate the correlation matrix
correlation_matrix = df_filtered.corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Prepare the data for linear regression
X = df_filtered.drop(columns=['GPA'])  # Features
y = df_filtered['GPA']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the GPA for the test set
y_pred = model.predict(X_test)

# Scatter plot of predicted vs actual GPA
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, marker='o')
plt.title('Predicted vs Actual GPA')
plt.xlabel('Actual GPA')
plt.ylabel('Predicted GPA')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Line for perfect prediction

plt.show()

# Get the coefficients and intercept
coefficients = model.coef_  # Coefficients of the features
intercept = model.intercept_  # Intercept of the model

# Print the coefficients and intercept
print("Coefficients:", coefficients)
print("Intercept:", intercept)




