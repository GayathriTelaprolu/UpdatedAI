import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
df=pd.read_csv(r'C:\Users\HP\Python_module\project\Metro_Interstate_Traffic_Volume.csv')

print(df.head())
pd.set_option('display.max_columns',None)
print(df.describe())
# Initialize the LabelEncoder
label_encoder = LabelEncoder()
# Apply label encoding to the 'holiday' column
df['holiday'] = label_encoder.fit_transform(df['holiday'])

# Apply label encoding to the 'weather_main' column
df['weather_main'] = label_encoder.fit_transform(df['weather_main'])

# Display the updated DataFrame

df['date_time']=pd.to_datetime(df['date_time'],format='mixed')
df['day'] = df['date_time'].dt.day_name()
df['month'] = df['date_time'].dt.month
df['year'] = df['date_time'].dt.year
df['hour'] = df['date_time'].dt.hour
#df['date'] = df['date_time'].dt.date

df.drop('date_time',axis=1,inplace = True)
df.head()

df['temp'] = df['temp'] - 273.15 
pd.set_option('display.max_columns',None)
print(df.describe())

 # Convert Kelvin to Celsius

# Plotting traffic_volume against Temperature_Celsius using a scatter plot
plt.scatter(df['temp'], df['traffic_volume'], marker='o')
plt.title('Traffic Volume vs Temperature in Celsius')
plt.xlabel('Temperature (°C)')
plt.ylabel('Traffic Volume')

plt.show()

plt.boxplot(x=df['temp'])
plt.show()

# Exclude the 'weather_description' column and keep label-encoded 'holiday'
df_filtered = df.drop(columns=['weather_description', 'day'])  # Exclude only non-numeric columns

# Calculate the correlation matrix
correlation_matrix = df_filtered.corr()

# Get the correlation of 'traffic_volume' with other variables
traffic_volume_correlation = correlation_matrix['traffic_volume']

print(traffic_volume_correlation)

# Create a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))  # Set the figure size
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap')
plt.show()

# Prepare the data
X = df_filtered.drop(columns=['traffic_volume'])  # Features
y = df_filtered['traffic_volume']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get the coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

print("Coefficients:", coefficients)
print("Intercept:", intercept)

# Plotting predicted vs actual traffic volume
plt.scatter(y_test, model.predict(X_test), marker='o')
plt.title('Predicted vs Actual Traffic Volume')
plt.xlabel('Actual Traffic Volume')
plt.ylabel('Predicted Traffic Volume')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Line for perfect prediction
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df['hour'], df['traffic_volume'], marker='o', linestyle='-', color='b')
plt.title('Traffic Volume by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Traffic Volume')
plt.xticks(range(0, 24))  # Set x-ticks for each hour
plt.grid()
plt.show()

