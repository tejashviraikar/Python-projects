def is_palindrome(text):
    """Check if the given text is a palindrome."""
    # Convert text to lowercase to make the check case-insensitive
    text = text.lower()
    
    # Remove non-alphanumeric characters from the text
    filtered_text = ''.join(char for char in text if char.isalnum())
    
    # Check if the filtered text is the same forwards and backwards
    return filtered_text == filtered_text[::-1]

def main():
    """Main function to interact with the user and check for palindrome."""
    # Get user input
    user_input = input("Enter a word or phrase: ")
    
    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

# Run the palindrome checker
main() 
