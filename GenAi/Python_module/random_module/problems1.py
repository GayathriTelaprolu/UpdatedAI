''' "Generate Random Discounts" – Generate discount codes for customers and calculate their total price after applying the discount and tax.'''

import random
import math

# Function to generate a random discount percentage (5%, 10%, 15%, etc.)
def generate_discount():
    discounts = [5, 10, 15, 20, 25]  # Available discount percentages
    return random.choice(discounts)

# Function to calculate the final price after applying the discount
def calculate_final_price(price, discount_percentage, tax_rate=5):
    discount_amount = (discount_percentage / 100) * price
    price_after_discount = price - discount_amount
    
    # Adding tax to the discounted price
    tax_amount = (tax_rate / 100) * price_after_discount
    final_price = price_after_discount + tax_amount
    
    # Using math.ceil to round up the final price to the nearest integer
    return math.ceil(final_price)

# Simulate processing for a customer
def process_customer_purchase(customer_name, purchase_history):
    total_purchase = sum(purchase_history)  # Sum of all purchases
    discount = generate_discount()
    final_price = calculate_final_price(total_purchase, discount)
    
    print(f"Customer: {customer_name}")
    print(f"Total Purchase: ${total_purchase:.2f}")
    print(f"Discount Applied: {discount}%")
    print(f"Final Price after Discount and Tax: ${final_price}")
    print()

# Example customer purchases
customer_data = [
    {"name": "Alice", "purchase_history": [100, 150, 250]},
    {"name": "Bob", "purchase_history": [80, 60, 100]},
    {"name": "Charlie", "purchase_history": [200, 300, 400]}
]

# Process each customer
for customer in customer_data:
    process_customer_purchase(customer["name"], customer["purchase_history"])
    



