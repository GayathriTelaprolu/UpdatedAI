This code provides a complete workflow for cleaning, analyzing, and modeling a dataset related to apple quality. It follows these key steps:

Data Cleaning: The initial dataset (apple_quality.csv) is cleaned by removing rows with missing values, converting relevant columns to numeric data types, and handling negative values by setting them to zero where appropriate. The cleaned data is saved as cleaned_fruit_data.csv.

Feature Engineering and Analysis: After loading the cleaned dataset, a formula-based Price column is calculated based on selected features (e.g., Weight, Sweetness, Juiciness, Crunchiness, Size). The code performs correlation analysis and visualizes the relationship between Price and other features through a heatmap. A T-test examines the significance of Sweetness in affecting Price.

Linear Regression Modeling: The dataset (updated_dataset_with_price.csv) is split into training and test sets to train a linear regression model with features (Size, Weight, Sweetness, Crunchiness, Juiciness) predicting Price. Model evaluation includes Mean Squared Error (MSE) and R-squared metrics, with a scatter plot comparing actual and predicted Price values to assess model performance visually.

The entire code ensures error handling during data loading, training, and evaluation, making it robust for practical applications. The final processed dataset with predicted prices is saved for future use.