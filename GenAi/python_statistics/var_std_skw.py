
import numpy as np
'''
from scipy.stats import skew

# Sample dataset of 10 numbers
data = []
for i in range(1,11):
    data.append(i)

# Calculate variance
mean=np.mean(data)
median=np.median(data)
variance = np.var(data)

# Calculate standard deviation
std_deviation = np.std(data)

# Calculate skewness
skewness = skew(data)

# Print results
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Skewness: {skewness}")
print(f"mean:{mean}")
print(f"median:{median}")
'''
# Probability of drawing a black king (P(A))
P_black_king = 2 / 52

# Probability of drawing a black card (P(B))
P_black_card = 26 / 52

# Probability of drawing a black card given that it is a black king (P(B|A)) = 1
P_black_card_given_black_king = 1

# Using Bayes' Theorem to calculate P(Black King | Black Card)
P_black_king_given_black_card = (P_black_card_given_black_king * P_black_king) / P_black_card

# Output the result
print(f"The probability of drawing a black King given that the card is black is: {P_black_king_given_black_card:.4f}")


data=np.random.normal(25,8,20)
print(data)
m=np.mean(data)
sd=np.std(data)
print(m)
print(sd)
