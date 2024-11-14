import json

def extract_keys(data, parent_key=''):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            keys.append(key)  # Collect each key
            # Recurse into nested dictionaries/lists
            keys.extend(extract_keys(value, key))
    elif isinstance(data, list):
        for item in data:
            keys.extend(extract_keys(item, parent_key))
    return keys

def find_matching_keys(json_data, string_list):
    # Extract all keys in the JSON structure
    all_keys = extract_keys(json_data)
    string_set = set(s.lower() for s in string_list)  # Convert string_list to lowercase set

    # Find matches where any part of the string in `string_set` matches a key
    matching_keys = [key for key in all_keys if any(substring in key.lower() for substring in string_set)]
    return matching_keys

# Load JSON data from a file
json_file_path = 'data.json'  # Replace with the path to your JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# List of strings to compare with JSON keys
string_list = ['example', 'test', 'key']  # Replace with your list of strings

# Find and print matching keys
matching_keys = find_matching_keys(json_data, string_list)
print("Matching keys:", matching_keys)
