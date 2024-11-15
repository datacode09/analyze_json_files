import json
import os

def search_keys_in_json_files(key_list, json_files, output_file):
    output_data = []

    # Loop through each JSON file
    for json_file in json_files:
        with open(json_file, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Skipping {json_file}: Not a valid JSON file.")
                continue

        # Search for each key in the current JSON file
        matched_data = {key: data[key] for key in key_list if key in data}

        # If there are matched keys, append to output_data with the filename
        if matched_data:
            matched_data['filename'] = os.path.basename(json_file)
            output_data.append(matched_data)

    # Write the output data to the output JSON file
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

    print(f"Output saved to {output_file}")

# Example usage
key_list = ['key1', 'key2', 'key3']  # Keys to search for
json_files = ['file1.json', 'file2.json', 'file3.json']  # List of JSON files to search
output_file = 'output.json'  # Output file to store the matched data

search_keys_in_json_files(key_list, json_files, output_file)
