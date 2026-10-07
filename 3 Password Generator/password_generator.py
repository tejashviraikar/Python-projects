import random
import string


# ----------------------------
# Generate Password
# ----------------------------
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


# ----------------------------
# Main Program
# ----------------------------
def main():
    print("=" * 40)
    print("      PYTHON PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

        print("\nInclude the following characters? (y/n)")

        upper = input("Uppercase Letters (A-Z): ").lower() == "y"
        lower = input("Lowercase Letters (a-z): ").lower() == "y"
        digits = input("Numbers (0-9): ").lower() == "y"
        symbols = input("Special Characters (!@#$...): ").lower() == "y"

        password = generate_password(length, upper, lower, digits, symbols)

        if password:
            print("\nGenerated Password:")
            print(password)
        else:
            print("\nPlease select at least one character type.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()