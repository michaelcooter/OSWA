import re
import sys

def search_js_file(file_path):
    # Define the patterns to search for
    patterns = [
        r'setRequestHeader',
        r'send\(',
        r'\.headers',
        r'onreadystatechange',
        r'\bvar\b',
        r'getParameter\(\)',
        r'\.theirdomain\.com',
        r'apiKey',
        r'postMessage',
        r'messageListener',
        r'\.innerHTML',
        r'document\.write\(',
        r'document\.cookie',
        r'location\.href',
        r'redirectUrl',
        r'window\.hash',
        r'api\b',
        r'api/',
        r'internal',
        r'url:',
        r'var\s*=',
        r'//.*',  # Single-line comments
        r'/\*[\s\S]*?\*/',  # Multi-line comments
        r'http://',
        r'https://',
        r'company\.com',
        r'location\.search',
        r'parameter',
        r'pathname',
        r'POST',
        r'GET'
    ]
    
    # Compile the patterns into a single regular expression
    combined_pattern = re.compile('|'.join(patterns))

    # Open the JavaScript file and the output file
    with open(file_path, 'r') as js_file, open('extracted_info.txt', 'w') as output_file:
        # Read the contents of the JavaScript file
        contents = js_file.read()
        
        # Find all matches of the patterns
        matches = combined_pattern.findall(contents)
        
        # Write the matches to the output file
        for match in matches:
            output_file.write(match + '\n')

if __name__ == '__main__':
    # Check if a file path was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python jsAnalyzer.py <path_to_js_file>")
        sys.exit(1)
    
    # Get the file path from the arguments
    js_file_path = sys.argv[1]
    
    # Run the search function
    search_js_file(js_file_path)

