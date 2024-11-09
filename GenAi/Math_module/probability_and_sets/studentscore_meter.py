import os
from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

# Function to calculate conditional probability and plot gauge
def calculate_and_plot_gauge(student_id, course_name, week, df):
    # Filter the dataframe based on inputs
    filtered_df = df[(df['student_id'] == int(student_id)) & 
                     (df['course_title'] == course_name) & 
                     (df['week'] == int(week))]
    
    # Check if any data was found for the given inputs
    if filtered_df.empty:
        return None
    
    # Get the expected and completed modules for the specific week
    expected_modules = set(filtered_df['expected_modules'].iloc[0].split(','))
    completed_modules = set(filtered_df['completed_modules'].iloc[0].split(','))
    
    # Calculate P(A ∩ B): Number of modules that are both completed and expected
    intersection = len(expected_modules.intersection(completed_modules))
    
    # Calculate P(B): Number of expected modules
    total_expected = len(expected_modules)
    
    # Calculate conditional probability P(A|B)
    conditional_probability = intersection / total_expected if total_expected > 0 else 0.0
    
    # Plot the gauge based on the calculated probability
    plot_gauge(conditional_probability)
    return conditional_probability

# Function to plot the semi-circular gauge meter
def plot_gauge(probability):
    # Set up the gauge meter figure
    fig, ax = plt.subplots(figsize=(6, 3))

    # Create the semi-circle
    theta = np.linspace(np.pi, 0, 100)
    r = np.ones(100)
    ax.plot(r * np.cos(theta), r * np.sin(theta), color='black', lw=3)

    # Create ticks for the gauge (0 to 1)
    for tick in np.linspace(0, 1, 11):
        angle = np.pi * (1 - tick)  # convert value to angle
        ax.text(np.cos(angle) * 1.1, np.sin(angle) * 1.1, f'{tick:.1f}', ha='center', va='center', fontsize=10)

    # Hide the axis and background
    ax.set_axis_off()

    # Set limits for the plot
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.5)

    # Plot the needle
    needle_angle = np.pi * (1 - probability)
    needle_color = 'red' if probability <= 0.5 else 'green'

    ax.arrow(0, 0, np.cos(needle_angle), np.sin(needle_angle), 
             head_width=0.05, head_length=0.1, fc=needle_color, ec=needle_color, lw=2)

    # Save the figure
    gauge_image_path = os.path.join('static', 'gauge_progress.png')
    plt.savefig(gauge_image_path)
    plt.close()

@app.route('/')
def home():
    return "Welcome to the Course Progress App"

@app.route('/course/<int:student_id>/<course_name>/<int:week>')
def course_page(student_id, course_name, week):
    # Load CSV file
    csv_file_path = "student_course_progress.csv"
    df = pd.read_csv(csv_file_path, usecols=['student_id', 'course_title', 'week', 'expected_modules', 'completed_modules'])

    # Calculate progress and generate gauge
    probability = calculate_and_plot_gauge(student_id, course_name, week, df)

    if probability is None:
        return "No data found for the given course."

    # Render the course page with the gauge
    return render_template('course_page.html', student_id=student_id, course_name=course_name, week=week, probability=probability)

@app.route('/gauge_image')
def gauge_image():
    gauge_image_path = os.path.join('static', 'gauge_progress.png')
    return send_file(gauge_image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
