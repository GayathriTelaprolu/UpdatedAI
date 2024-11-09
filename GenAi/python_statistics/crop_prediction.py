import pandas as pd

# Expanded dataset with multiple features
data = {
    'Symptoms': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Fungal Disease': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No'],
    'Temperature': ['High', 'Moderate', 'High', 'Low', 'Moderate', 'Low', 'High', 'Low'],
    'Humidity': ['High', 'Moderate', 'High', 'Low', 'High', 'Low', 'Moderate', 'Low'],
    'Rainfall': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Soil Moisture': ['High', 'Low', 'High', 'Low', 'Moderate', 'Low', 'Moderate', 'Low']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 1: Calculate prior probabilities
P_fungal_disease = len(df[df['Fungal Disease'] == 'Yes']) / len(df)
P_no_disease = len(df[df['Fungal Disease'] == 'No']) / len(df)

# Step 2: Calculate likelihoods for each feature

# Likelihoods for Symptoms given Fungal Disease
P_spots_given_fungal = len(df[(df['Symptoms'] == 'Yes') & (df['Fungal Disease'] == 'Yes')]) / len(df[df['Fungal Disease'] == 'Yes'])
P_spots_given_no_disease = len(df[(df['Symptoms'] == 'Yes') & (df['Fungal Disease'] == 'No')]) / len(df[df['Fungal Disease'] == 'No'])

# Likelihoods for Temperature
P_high_temp_given_fungal = len(df[(df['Temperature'] == 'High') & (df['Fungal Disease'] == 'Yes')]) / len(df[df['Fungal Disease'] == 'Yes'])
P_high_temp_given_no_disease = len(df[(df['Temperature'] == 'High') & (df['Fungal Disease'] == 'No')]) / len(df[df['Fungal Disease'] == 'No'])

# Likelihoods for Humidity
P_high_humidity_given_fungal = len(df[(df['Humidity'] == 'High') & (df['Fungal Disease'] == 'Yes')]) / len(df[df['Fungal Disease'] == 'Yes'])
P_high_humidity_given_no_disease = len(df[(df['Humidity'] == 'High') & (df['Fungal Disease'] == 'No')]) / len(df[df['Fungal Disease'] == 'No'])

# Likelihoods for Rainfall
P_rainfall_given_fungal = len(df[(df['Rainfall'] == 'Yes') & (df['Fungal Disease'] == 'Yes')]) / len(df[df['Fungal Disease'] == 'Yes'])
P_rainfall_given_no_disease = len(df[(df['Rainfall'] == 'Yes') & (df['Fungal Disease'] == 'No')]) / len(df[df['Fungal Disease'] == 'No'])

# Likelihoods for Soil Moisture
P_high_moisture_given_fungal = len(df[(df['Soil Moisture'] == 'High') & (df['Fungal Disease'] == 'Yes')]) / len(df[df['Fungal Disease'] == 'Yes'])
P_high_moisture_given_no_disease = len(df[(df['Soil Moisture'] == 'High') & (df['Fungal Disease'] == 'No')]) / len(df[df['Fungal Disease'] == 'No'])

# Step 3: Calculate total probability of these conditions (P(Conditions))
P_conditions = (P_spots_given_fungal * P_high_temp_given_fungal * P_high_humidity_given_fungal * P_rainfall_given_fungal * P_high_moisture_given_fungal * P_fungal_disease) + \
               (P_spots_given_no_disease * P_high_temp_given_no_disease * P_high_humidity_given_no_disease * P_rainfall_given_no_disease * P_high_moisture_given_no_disease * P_no_disease)

# Step 4: Apply Bayes' Theorem for P(fungal disease | conditions)
P_fungal_given_conditions = (P_spots_given_fungal * P_high_temp_given_fungal * P_high_humidity_given_fungal * P_rainfall_given_fungal * P_high_moisture_given_fungal * P_fungal_disease) / P_conditions

# Display the result
print(f"The probability of fungal disease given the observed conditions: {P_fungal_given_conditions:.2%}")
