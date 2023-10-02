# mean, median, mode
from statistics import median, mode



color_rgb = {
'green': (0, 255, 0),  # Green
'yellow': (255, 255, 0),  # Yellow
'brown': (139, 69, 19),  # Brown
'blue': (0, 0, 255),  # Blue
'pink': (255, 192, 203),  # Pink
'orange': (255, 165, 0),  # Orange
'cream': (255, 253, 208),  # Cream
'red': (255, 0, 0),  # Red
'white': (255, 255, 255),  # White
'ash': (169, 169, 169),  # Ash
'black': (0, 0, 0)  # Black
}

color_quantities = {
    'green': 10,
    'yellow': 5,
    'brown': 6,
    'blue': 31,
    'pink': 5,
    'orange': 9,
    'cream': 2,
    'red': 8,
    'white': 16,
    'ash': 1,
    'black': 1
}

# Calculate the weighted mean color
total_pixels = sum(color_quantities.values())
mean_color = [0, 0, 0]  # Initialize mean color as [0, 0, 0]

# Iterate through each color and calculate weighted RGB values
for color, quantity in color_quantities.items():
    rgb = color_rgb[color]
    weight = quantity / total_pixels  # Weight based on quantity
    # Accumulate weighted RGB values
    mean_color[0] += rgb[0] * weight
    mean_color[1] += rgb[1] * weight
    mean_color[2] += rgb[2] * weight

# Round the mean color RGB values
mean_color = tuple(round(value) for value in mean_color)

print('Mean Color (R, G, B):', mean_color)


# Assign numerical values to colors (arbitrary)
color_values = {
    'green': 1,
    'yellow': 2,
    'brown': 3,
    'blue': 4,
    'pink': 5,
    'orange': 6,
    'cream': 7,
    'red': 8,
    'white': 9,
    'ash': 10,
    'black': 11
}

# Flatten the color quantities to match the numerical values
flattened_color_quantities = []
for color, quantity in color_quantities.items():
    flattened_color_quantities.extend([color_values[color]] * quantity)

# Calculate the median
median_color = median(flattened_color_quantities)

# Calculate the mode
mode_color = mode(flattened_color_quantities)

# Convert numerical values back to color names
median_color_name = [k for k, v in color_values.items() if v == median_color][0]
mode_color_name = [k for k, v in color_values.items() if v == mode_color][0]

print('Median Color:', median_color_name)
print('Mode Color:', mode_color_name)    


# Calculate the mean (average)
mean_quantity = sum(color_quantities.values()) / len(color_quantities)

# Calculate the variance
variance = sum((quantity - mean_quantity) ** 2 for quantity in color_quantities.values()) / len(color_quantities)

print('Variance:', variance)

# Calculate the probability
total_quantity = sum(color_quantities.values())

# Calculate the probability for each color
color_probabilities = {color: quantity / total_quantity for color, quantity in color_quantities.items()}

# Print the probabilities for each color
for color, probability in color_probabilities.items():
    print(f'Probability of {color}: {probability:.2%}')