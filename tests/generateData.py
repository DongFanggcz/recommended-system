import uuid
import os
import json
from datetime import datetime, timedelta

# Create a folder path
folder_path = "tests/documents"

# Get the current working directory
current_directory = os.getcwd()
current_directory = os.path.join(current_directory, folder_path)

# Function to create test data
def generate_test_data(user_uuid, document_uuid, upload_date):
    return {
        "username": "df123",
        "user_uuid": str(user_uuid),
        "upload_date": upload_date,
        "document_name": "markdown.md",
        "public": True,
        "document_uuid": str(document_uuid)
    }

# Function to generate a single test JSON file
def generate_json_for_user(user_uuid, num_documents=5):
    # Create the user's folder path (using UUID as the folder name)
    user_folder_path = os.path.join(current_directory, str(user_uuid))

    # If the folder does not exist, create the folder
    if not os.path.exists(user_folder_path):
        os.makedirs(user_folder_path)
        print(f"Folder '{user_folder_path}' has been created!")
    else:
        print(f"Folder '{user_folder_path}' already exists.")

    # Generate multiple documents for this user
    for i in range(num_documents):
        document_uuid = uuid.uuid4()  # Generate a new document UUID
        # Generate a random upload date, offset by `i` days from a starting point
        upload_date = (datetime(2021, 1, 1) + timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
        
        # Create the data to be written to the JSON file
        data = generate_test_data(user_uuid, document_uuid, upload_date)
        
        # Construct the JSON file path (using document UUID)
        json_file_path = os.path.join(user_folder_path, f"{document_uuid}.json")
        
        # Write the data to the JSON file
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"JSON file has been generated! File path: {json_file_path}")

# Function to generate test data for multiple users
def generate_multiple_users(num_users=3, num_documents=5):
    for _ in range(num_users):
        user_uuid = uuid.uuid4()  # Generate a random user UUID
        generate_json_for_user(user_uuid, num_documents)

# Generate test data for multiple users
generate_multiple_users(num_users=3, num_documents=5)
