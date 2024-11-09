# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /loan_default

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory (with your app.py) into the container
COPY . .

# Run the Python file when the container starts
CMD ["python", "loan_default.py"]
