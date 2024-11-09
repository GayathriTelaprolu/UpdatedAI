import string
import random

def generate_password(min_length=10, max_length=20):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(characters) for _ in range(length))

def meets_case2(password):
    return (
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$" for c in password)
    )

# Generate a large set of passwords
num_passwords = 1000
passwords = [generate_password() for _ in range(num_passwords)]

# Set A: Passwords with odd lengths between 10 and 20
set_A = set(password for password in passwords if len(password) % 2 != 0)

# Set B: Passwords that meet case 2 (complexity requirements)
set_B = set(password for password in set_A if meets_case2(password))

# Calculate the probability
p_b_given_a = len(set_B) / len(set_A)

print(f"Total passwords generated: {num_passwords}")
print(f"Passwords meeting case 1 (odd length between 10 and 20): {len(set_A)}")
print(f"Passwords meeting both cases: {len(set_B)}")
print(f"Probability of case 2 given case 1: {p_b_given_a:.4f}")

# Additional analysis: Break down by length


