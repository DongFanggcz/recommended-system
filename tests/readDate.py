import os
import json

# Specify the directory path where generateddata is stored
base_directory = r'tests\generateddata'  # Make sure to modify it to your actual path

# Iterate through all UUID subdirectories in base_directory
for uuid_folder in os.listdir(base_directory):
    # Construct the full path of the UUID subdirectory
    uuid_folder_path = os.path.join(base_directory, uuid_folder)
    
    # Check if the path is a valid directory
    if os.path.isdir(uuid_folder_path):
        # Construct the path of the data.json file within the directory
        data_file_path = os.path.join(uuid_folder_path, 'data.json')
        
        # Check if the data.json file exists
        if os.path.exists(data_file_path):
            try:
                # Open and read the data.json file
                with open(data_file_path, 'r') as file:
                    data = json.load(file)  # Parse the JSON data
                    
                    # Output the contents of the data.json file for the current UUID
                    print(f"Data from {uuid_folder}/data.json:")
                    print(data)
                    print('-' * 40)
            except Exception as e:
                print(f"Error reading {data_file_path}: {e}")
        else:
            print(f"File {data_file_path} does not exist.")
