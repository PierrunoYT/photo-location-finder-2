import requests
import json
import base64
import os
import webbrowser

url = "https://picarta.ai/classify"
api_token = "YOUR API TOKEN"  # Replace with your actual API token
headers = {"Content-Type": "application/json"}

# Prompt the user to enter a folder directory
folder_path = input("Enter a folder directory: ")

# Get the absolute path of the folder
absolute_path = os.path.abspath(folder_path)

# Iterate over the files in the folder
for file_name in os.listdir(absolute_path):
    # Check if the file is a JPEG file
    if file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
        # Get the absolute path of the JPEG file
        file_path = os.path.join(absolute_path, file_name)

        # Read the image file
        with open(file_path, "rb") as image_file:
            img_data = base64.b64encode(image_file.read()).decode('utf-8')

        # Prepare the payload
        payload = {"TOKEN": api_token, "IMAGE": img_data}

        # Send the POST request with the payload as JSON data
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            print(result)

            # Check if "ai_lat" and "ai_lon" keys exist in the result dictionary
            if "ai_lat" in result and "ai_lon" in result:
                # Convert the latitude and longitude coordinates
                lat = result["ai_lat"]
                lon = result["ai_lon"]

                # Construct the OpenStreetMap URL with the coordinates
                osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=15"

                # Open the OpenStreetMap URL in the web browser
                webbrowser.open(osm_url)
            else:
                print("The keys 'ai_lat' and/or 'ai_lon' do not exist in the result dictionary.")
        else:
            print("Request failed with status code:", response.status_code)

    else:
        print(f"Skipping file: {file_name}")
