def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Number of odd numbers
m = 50

# Set A: Prime numbers up to the 50th odd number
max_odd = 2 * m - 1
set_A = set(num for num in range(2, max_odd + 1) if is_prime(num))

# Set B: First 50 odd numbers
set_B = set(range(1, max_odd + 1, 2))

# Find the intersection of the two sets
intersection = set_A.intersection(set_B)

# Calculate P(A|B)
p_a_given_b = len(intersection) / len(set_B)

# Print the results
print(f"Number of odd numbers: {m}")
print(f"Number of elements in Set A (Primes up to {max_odd}): {len(set_A)}")
print(f"Number of elements in Set B (First {m} odd numbers): {len(set_B)}")
print(f"Number of elements in A ∩ B: {len(intersection)}")
print(f"P(A|B) = {p_a_given_b:.4f}")

print("\nSet A (Primes up to 99):")
# print(sorted(set_A))

print("\nSet B (First 50 odd numbers):")
# print(sorted(set_B))

print("\nIntersection (Odd primes up to 99):")
# print(sorted(intersection))