# Given values
radius = 84  # in meters
pi = 3.14
water_per_square_meter = 1.4  # in liters

# Step 1: Calculate the area of the pond
area = pi * (radius ** 2)

# Step 2: Calculate the total amount of water
total_water = area * water_per_square_meter

# Step 3: Print the total amount of water without any decimal point
print(f"The area of the pond is: {int(area)} square meters")
print(f"The total amount of water in the pond is: {int(total_water)} liters")
