# Photo Location Finder

This code utilizes the Picarta AI service to find the location of images in a given folder directory. It iterates over each file in the folder, checks if it is a JPEG file (.jpg or .jpeg extension), and then sends a POST request to the Picarta API with the image data encoded in base64 format. The API response includes the latitude and longitude coordinates of the image location.

## Prerequisites

- Python 3.x
- requests library
- json library
- base64 library

## How to Use

1. Obtain an API token from the Picarta website and replace the `api_token` variable with your actual API token.
2. Run the code and provide a folder directory when prompted.
3. The code will iterate over the files in the folder, find JPEG images, read the image file, encode it in base64 format, and send a request to the Picarta API.
4. If the request is successful (status code 200), the latitude and longitude coordinates of the image location will be used to open the location on OpenStreetMap.
5. If the request fails, the status code will be displayed.

Note: Ensure that you have an active internet connection for the API requests to work.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
