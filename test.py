import json

# Path to the JSON file
file_path = 'MSASL_test.json'

# Function to extract URLs
def extract_urls_from_json(file_path):
    # Open and load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the first 10 URLs
    urls = [entry['url'] for entry in data[:10]]
    
    return urls

# Call the function and print the URLs
video_urls = extract_urls_from_json(file_path)
for url in video_urls:
    print(url)
