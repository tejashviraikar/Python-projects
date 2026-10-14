# Build a program that analyzes and extracts information from a given URL
# Import required modules
import requests  # For HTTP requests
from urllib.parse import urlparse, parse_qs  # For URL parsing

# Function to analyze a given URL
def analyze_url(url):
    # Parse URL to extract components
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme.upper()  # Extract and convert protocol to uppercase
    domain = parsed_url.netloc  # Extract domain
    path = parsed_url.path  # Extract path
    query = parse_qs(parsed_url.query)  # Parse query parameters into a dictionary

    # Make a request to the URL to get status and HTML content
    try:
        response = requests.get(url)
        status_code = response.status_code  # Extract HTTP status code
        html_content = response.text  # Get HTML content of the page

        # Extract page title and meta description if available
        page_title = extract_meta(html_content, "", "")
        meta_description = extract_meta(html_content, 'name="description" content="', '"')
        
        # Display the results
        print("Analysis results:")
        print(f"- Domain: {domain}")
        print(f"- Protocol: {protocol}")
        print(f"- Path: {path}")
        print(f"- Query parameters: {query if query else 'None'}")
        print(f"- HTTP status: {status_code}")
        print(f"- Page title: {page_title}")
        print(f"- Meta description: {meta_description if meta_description else 'None'}")

    except requests.RequestException as e:
        print(f"Error analyzing URL: {e}")

# Helper function to extract metadata from HTML content
def extract_meta(html, start_tag, end_tag):
    start_index = html.find(start_tag)
    if start_index == -1:
        return None
    start_index += len(start_tag)
    end_index = html.find(end_tag, start_index)
    return html[start_index:end_index].strip()

# Example usage
analyze_url("https://www.w3resource.com/")
#analyze_url("https://www.w3resource.com/privacy/")
