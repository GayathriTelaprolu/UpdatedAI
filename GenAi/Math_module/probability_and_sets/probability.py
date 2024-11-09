import random

def calculate_probabilities(seeds):
    total_seeds = sum(seeds.values())
    
    # 1. Chance of getting cotton seed
    cotton_prob = seeds['cotton'] / total_seeds
    
    # 2. Chance of getting either cotton or paddy seed
    cotton_paddy_prob = (seeds['cotton'] + seeds['paddy']) / total_seeds
    
    # 3. Chance of getting cotton seed if mirchi seed is taken out
    remaining_seeds = total_seeds - seeds['mirchi']
    cotton_prob_without_mirchi = seeds['cotton'] / remaining_seeds
    
    return cotton_prob, cotton_paddy_prob, cotton_prob_without_mirchi

def main():
    seeds = {
        'cotton': 30,
        'paddy': 50,
        'mirchi': 20
    }
    
    cotton_prob, cotton_paddy_prob, cotton_prob_without_mirchi = calculate_probabilities(seeds)
    
    print(f"1. Chance of getting cotton seed: {cotton_prob:.2%}")
    print(f"2. Chance of getting either cotton or paddy seed: {cotton_paddy_prob:.2%}")
    print(f"3. Chance of getting cotton seed if mirchi seed is taken out: {cotton_prob_without_mirchi:.2%}")

if __name__ == "__main__":
    main()
