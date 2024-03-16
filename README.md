# Photo Location Finder

This Python script is designed to classify images using the Picarta AI API and then display the location of the classified images on OpenStreetMap.

## Features

- Prompts the user to enter a folder directory containing JPEG images.
- Iterates over the files in the specified folder and checks if each file is a JPEG image.
- Reads the JPEG image file, encodes it in base64 format, and sends a POST request to the Picarta AI API with the encoded image data and the API token.
- If the API request is successful, the script extracts the latitude and longitude coordinates from the API response and constructs an OpenStreetMap URL with the coordinates.
- Opens the OpenStreetMap URL in the default web browser, allowing the user to see the location of the classified image on a map.
- Handles errors gracefully, printing error messages if the API request fails or the necessary keys are not present in the API response.
- Skips non-JPEG files in the folder.

## Prerequisites

- Python 3.x
- Required libraries:
  - `requests`
  - `json`
  - `base64`
  - `os`
  - `webbrowser`

## Usage

1. Replace `"YOUR API TOKEN"` in the script with your actual Picarta AI API token.
2. Run the script.
3. When prompted, enter the folder directory containing the JPEG images you want to classify.
4. The script will process each JPEG file in the folder, send a request to the Picarta AI API, and open the location of the classified image on OpenStreetMap.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
