# Image Classification using Picarta API

This code utilizes the Picarta AI service to classify images in a given folder directory. It iterates over each file in the folder, checks if it is a JPEG file (.jpg or .jpeg extension), and then sends a POST request to the Picarta API with the image data encoded in base64 format.

## Prerequisites

- Python 3.x
- requests library
- json library
- base64 library

## How to Use

1. Obtain an API token from the Picarta website and replace the `api_token` variable with your actual API token.
2. Run the code and provide a folder directory when prompted.
3. The code will iterate over the files in the folder, find JPEG images, read the image file, encode it in base64 format, and send a request to the Picarta API.
4. If the request is successful (status code 200), the API response will be printed.
5. If the request fails, the status code will be displayed.

Note: Ensure that you have an active internet connection for the API requests to work.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
