# Input values:
# User provides a long URL to be shortened.

# Output value:
# Shortened URL generated and associated with the provided long URL.

import hashlib  # Import hashlib to generate a hash for the long URL

# Dictionary to store the mapping between long URLs and short URLs
url_mapping = {}

def shorten_url(long_url):
    """Generate a short URL by hashing the long URL."""
    # Generate a unique hash using SHA-256 and take the first 6 characters for short URL
    short_url_hash = hashlib.sha256(long_url.encode()).hexdigest()[:6]
    short_url = f"https://short.url/{short_url_hash}"
    
    # Store the mapping in the dictionary
    url_mapping[short_url] = long_url
    
    return short_url

def main():
    """Main function to interact with the user."""
    # Get user input for the long URL
    long_url = input("Input the long URL to be shortened: ")
    
    # Generate a shortened URL
    short_url = shorten_url(long_url)
    
    # Display the shortened URL
    print(f"Short URL: {short_url}")

# Run the URL Shortener
main() 
