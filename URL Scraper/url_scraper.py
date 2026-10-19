# Build a program that extracts URLs from a given webpage.

import requests  # Import requests to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

def extract_urls(webpage_url):
    """Extracts all URLs from a given webpage."""
    try:
        # Send a GET request to the webpage
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags with href attribute
        anchor_tags = soup.find_all('a', href=True)
        
        # Extract URLs from the anchor tags
        urls = [tag['href'] for tag in anchor_tags if tag['href'].startswith('http')]
        
        # Print the extracted URLs
        print(f"URLs extracted from {webpage_url}:")
        for idx, url in enumerate(urls, 1):
            print(f"{idx}. {url}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")

# Input: Get URL from user
webpage_url = input("Enter the URL of the webpage: ")
extract_urls(webpage_url)  # Call the function to extract URLs 
