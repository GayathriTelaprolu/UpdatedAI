import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("crop_Recommendation.csv")

# Print basic information about the dataset
print(df.shape)
print(df.isnull().sum())
print(df.dtypes)
print(df.describe())

# Count the number of lands for each crop
crop_land_counts = df['Crop'].value_counts()
print(crop_land_counts)

# Create a bar plot
plt.figure(figsize=(14, 8))
crop_land_counts.plot(kind='bar')
plt.title('Number of Lands Growing Each Crop Type')
plt.xlabel('Crop')
plt.ylabel('Number of Lands')
#plt.xticks(rotation=90)
plt.tight_layout()

# Add value labels on top of each bar
for i, v in enumerate(crop_land_counts):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()

# If you want to see the percentage distribution, you can use a pie chart
plt.figure(figsize=(12, 12))
plt.pie(crop_land_counts.values, labels=crop_land_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage Distribution of Lands by Crop Type')
plt.axis('equal')

plt.show()




