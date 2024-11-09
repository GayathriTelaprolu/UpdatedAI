import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Prompt the user for the file name and column name
file_name = input("Enter the name of your CSV file (including .csv extension): ")
column_name = input("Enter the name of the column containing the scores: ")

try:
    # Read the CSV file
    df = pd.read_csv(file_name)
    
    # Check if the specified column exists
    if column_name not in df.columns:
        raise KeyError(f"Column '{column_name}' not found in the CSV file.")
    
    # Get the scores from the specified column
    scores = df[column_name]
    
    # Calculate mean, median, and mode
    mean = scores.mean()
    median = scores.median()
    mode = scores.mode().iloc[0]  # Get the first mode if there are multiple
    std_dev = scores.std()
    
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    
    # Create the normal distribution curve
    plt.figure(figsize=(12, 6))
    
    # Generate points for x-axis
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
    
    # Create the normal distribution curve
    y = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, y, 'b-', linewidth=2, label='Normal Distribution')
    
    # Fill the area under the curve
    plt.fill_between(x, y, color='lightblue', alpha=0.5)
    
    # Mark mean, median, and mode
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean ({mean:.2f})')
    plt.axvline(median, color='green', linestyle='dashed', linewidth=2, label=f'Median ({median:.2f})')
    plt.axvline(mode, color='purple', linestyle='dashed', linewidth=2, label=f'Mode ({mode:.2f})')
    
    # Add labels and title
    plt.title(f'Normal Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Probability Density')
    plt.legend()
    
    # Add text annotations for mean, median, mode
    plt.text(mean, plt.ylim()[1], 'Mean', horizontalalignment='center', verticalalignment='bottom')
    plt.text(median, plt.ylim()[1]*0.95, 'Median', horizontalalignment='center', verticalalignment='bottom')
    plt.text(mode, plt.ylim()[1]*0.90, 'Mode', horizontalalignment='center', verticalalignment='bottom')
    
    # Show standard deviation ranges
    for i in range(1, 4):
        plt.axvline(mean + i*std_dev, color='gray', linestyle=':', alpha=0.5)
        plt.axvline(mean - i*std_dev, color='gray', linestyle=':', alpha=0.5)
        plt.text(mean + i*std_dev, plt.ylim()[1]*0.1, f'+{i}σ', horizontalalignment='center')
        plt.text(mean - i*std_dev, plt.ylim()[1]*0.1, f'-{i}σ', horizontalalignment='center')
    
    plt.grid(True, alpha=0.3)
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please make sure the file exists in the current directory.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_name}' is empty.")
except pd.errors.ParserError:
    print(f"Error: Unable to parse '{file_name}'. Please make sure it's a valid CSV file.")
except KeyError as e:
    print(f"Error: {str(e)} Please check your data format and column name.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")