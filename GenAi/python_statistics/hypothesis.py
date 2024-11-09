import numpy as np
import pandas as pd
from scipy import stats

# Sample agricultural data for crop yields
# Assume these are crop yields (in tons) for fields with and without fertilizer
data = {
    'With_Fertilizer': [30.1, 31.2, 32.0, 29.8, 34.5, 33.2, 35.0, 33.8, 34.0, 32.9],
    'Without_Fertilizer': [28.9, 29.5, 30.0, 29.3, 28.8, 29.0, 30.2, 30.1, 29.7, 30.0]
}

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the mean and standard deviation for each group
mean_with_fertilizer = np.mean(df['With_Fertilizer'])
mean_without_fertilizer = np.mean(df['Without_Fertilizer'])
std_with_fertilizer = np.std(df['With_Fertilizer'], ddof=1)  # sample std deviation
std_without_fertilizer = np.std(df['Without_Fertilizer'], ddof=1)

print(f"Mean Yield with Fertilizer: {mean_with_fertilizer:.2f}")
print(f"Mean Yield without Fertilizer: {mean_without_fertilizer:.2f}")
print(f"Standard Deviation with Fertilizer: {std_with_fertilizer:.2f}")
print(f"Standard Deviation without Fertilizer: {std_without_fertilizer:.2f}")

# Perform a one-tailed independent t-test (assuming unequal variances)
t_stat, p_value = stats.ttest_ind(df['With_Fertilizer'], df['Without_Fertilizer'], alternative='greater')

# Choose a significance level (alpha)
alpha = 0.05

print(f"\nT-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Determine whether to reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis (H0). The fertilizer increases crop yield.")
else:
    print("Fail to reject the null hypothesis (H0). There's no significant evidence that the fertilizer increases yield.")
