# Author: Michael Cooter
# Purpose: script to check CORS configurations for potential security issues

# Function to check CORS configuration
def check_cors(url):
    # Send an HTTP request to the URL with a custom 'Origin' header set to a test value
    headers = {'Origin': 'http://example.com'}
    response = requests.get(url, headers=headers)
    
    # Check for the presence of 'Access-Control-Allow-Origin' in the response headers
    if 'Access-Control-Allow-Origin' in response.headers:
        # Fetch the value of the 'Access-Control-Allow-Origin' header
        allowed_origin = response.headers['Access-Control-Allow-Origin']
        # Check if the 'Access-Control-Allow-Origin' header allows all domains ('*')
        if allowed_origin == '*':
            print(f"Vulnerable to CORS attack: Any origin can read resources from {url}")
        # Check if the 'Access-Control-Allow-Origin' header specifically allows the test origin
        elif allowed_origin == 'http://example.com':
            print(f"Vulnerable to CORS attack: Specifically allows http://example.com to access resources")
        else:
            print("Not vulnerable: CORS policy is restrictive")
    else:
        print("Not vulnerable: No CORS 'Access-Control-Allow-Origin' header is present")

# Main function to drive the program
def main():
    # Prompt the user to input a website URL
    url = input("Enter the website URL to check for CORS misconfiguration: ")
    
    # Call the function to check CORS configuration for the provided URL
    check_cors(url)

# Conditional to ensure this script runs directly (not imported)
if __name__ == "__main__":
    main()

