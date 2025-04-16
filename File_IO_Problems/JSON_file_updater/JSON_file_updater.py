'''
7. JSON File Updater
Given a JSON file with a dictionary, update a specific key’s value and save the updated dictionary back to the file.
'''

import json

def update_json_file(file_path, key, new_value):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if key in data:
        data[key] = new_value
    else:
        print(f"Key '{key}' not found in the JSON file.")
        return

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Updated the key '{key}' with the new value.")

file_path = r"File_IO_Problems\JSON_file_updater\data.json"

key_to_update = "username"
new_value = "new_user123"

update_json_file(file_path, key_to_update, new_value)