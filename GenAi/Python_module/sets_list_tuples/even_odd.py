# List of crops planted on the farm
crops = ['wheat', 'corn', 'soybeans']

# Tuple of possible crop types (fixed data)
crop_types = ('wheat', 'corn', 'soybeans', 'rice', 'potatoes')

# Crop details (String manipulation)
crop_details = {
    'wheat': 'Wheat is grown in the north field.',
    'corn': 'Corn is planted in the east field.',
    'soybeans': 'Soybeans are in the south field.'
}

# Display crop details
for crop in crops:
    print(f"Crop: {crop}, Details: {crop_details[crop]}")
    # List of workers
workers = ['John', 'Alice', 'Bob']

# Set of tasks (ensuring no duplicates)
tasks = {'watering', 'harvesting', 'pest control'}

# Dictionary to assign tasks to workers
worker_tasks = {}

# Assign workers to tasks
worker_tasks['John'] = 'watering'
worker_tasks['Alice'] = 'harvesting'
worker_tasks['Bob'] = 'pest control'

# Ensure no duplicate tasks for the day
assigned_tasks = set(worker_tasks.values())
print(assigned_tasks)  # Output: {'watering', 'harvesting', 'pest control'}

# Resources used in farming (liters or kilograms)
resource_usage = {
    'water': 150,  # liters
    'fertilizer': 30,  # kg
    'pesticide': 10  # liters
}

# Update resource usage for the day
def update_resource(resource, amount):
    if resource in resource_usage:
        resource_usage[resource] += amount
    else:
        resource_usage[resource] = amount

# Update today's usage
update_resource('water', 50)  # Adding 50 liters of water used
update_resource('fertilizer', 10)  # Adding 10 kg of fertilizer used

# Show total resource usage
print(resource_usage)
# Output: {'water': 200, 'fertilizer': 40, 'pesticide': 10}

