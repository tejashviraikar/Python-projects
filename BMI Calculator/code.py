def calculate_bmi(weight, height):
    """Calculate the BMI based on weight and height."""
    # Calculate BMI using the formula: BMI = weight / (height * height)
    bmi = weight / (height ** 2)
    return bmi

def determine_bmi_category(bmi):
    """Determine the BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to get user input, calculate BMI, and display the result."""
    # Get user input for weight and height
    weight = float(input("Enter weight (in kilograms): "))
    height = float(input("Enter height (in meters): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Determine the BMI category
    category = determine_bmi_category(bmi)

    # Display the results
    print(f"BMI: {bmi:.1f}")
    print(f"Category: {category}")

# Start the BMI Calculator
main()
