# Create a program that converts temperatures between Fahrenheit and Celsius

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Apply the conversion formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Apply the conversion formula: (C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Get the temperature from the user
temperature = float(input("Enter temperature: "))

# Ask the user for the conversion type
conversion_type = input("Select a conversion type (1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit): ")

# Perform the conversion based on user selection
if conversion_type == '1':
    # Convert Fahrenheit to Celsius
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"Converted temperature: {converted_temperature:.1f}°C")
elif conversion_type == '2':
    # Convert Celsius to Fahrenheit
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"Converted temperature: {converted_temperature:.1f}°F")
else:
    # Handle invalid conversion type selection
    print("Invalid selection. Please choose 1 or 2.")
