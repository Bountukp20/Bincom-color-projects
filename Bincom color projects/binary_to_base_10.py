import random

# Generate a random 4-digit binary number
binary_number = ''.join([random.choice(['0', '1']) for _ in range(4)])

# Convert the binary number to decimal (base 10)
decimal_number = int(binary_number, 2)

print(f"Generated Binary Number: {binary_number}")
print(f"Converted Decimal Number: {decimal_number}")