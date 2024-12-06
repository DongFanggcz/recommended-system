import uuid
import os
import json

# Create a folder path
folder_path = "tests\generatedData"

# Generate a random UUID using uuid4()
random_user_uuid = uuid.uuid4()
random_document_uuid = uuid.uuid4()

# Get the current working directory
current_directory = os.getcwd()
current_directory = os.path.join(current_directory, folder_path)

# Construct the new folder path (using UUID as the folder name)
folder_path = os.path.join(current_directory, str(random_user_uuid))

# If the folder does not exist, create the folder
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' has been created!")
else:
    print(f"Folder '{folder_path}' already exists.")

# Create the data to be written to the JSON file
data = {
    "username": "df123",
    "user_uuid": str(random_user_uuid),
    "upload_date": "2021-01-01 12:00:00",
    "document_name": "markdown.md",
    "public": True,
    "document_uuid": str(random_document_uuid)
}

# Construct the JSON file path
json_file_path = os.path.join(folder_path, "data.json")

# Write the data to the JSON file
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON file has been generated! File path: {json_file_path}")
