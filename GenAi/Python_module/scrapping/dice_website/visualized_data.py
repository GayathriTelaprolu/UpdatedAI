import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a Pandas DataFrame
df = pd.read_csv('job_listings_all_pages_corrected.csv')
df['City'] = df['Location'].apply(lambda x: x.split(',')[0].strip())

# Step 2: Group and count the occurrences of each job type
job_type_counts = df['Job Type'].value_counts()
city_job_counts = df['City'].value_counts()

# Step 3: Plot the data
plt.figure(figsize=(8, 5))  # Set the figure size
job_type_counts.plot(kind='bar', color=['skyblue', 'salmon'])

# Add titles and labels
plt.title('Job Type Distribution', fontsize=14)
plt.xlabel('Job Type', fontsize=12)
plt.ylabel('Number of Jobs', fontsize=12)

# Show the value counts on top of the bars
for i, count in enumerate(job_type_counts):
    plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''

plt.figure(figsize=(8, 8))
plt.pie(city_job_counts, labels=city_job_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Job Distribution by City')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
'''

plt.figure(figsize=(10, 6))
city_job_counts.plot(kind='bar', color='skyblue')
plt.title('Job Distribution by City (Bar Graph)')
plt.xlabel('City')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  