# Given values
distance = 490  # in meters
time_minutes = 7
time_seconds = time_minutes * 60  # Convert time to seconds

# Step 2: Calculate speed in meters per second
speed = distance // time_seconds  # Use integer division to get rid of decimal points

# Print the speed without any decimal point
print(f"Your speed is: {speed} meters per second")
