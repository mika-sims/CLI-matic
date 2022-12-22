# Import requests module and exceptions from api_call module
from api_call import requests, HTTPError, ConnectionError

# Import gzip library to decompress gzip files
import gzip

# Import json library to parse JSON string and convert it into dictionary
import json

URL = "http://bulk.openweathermap.org/sample/city.list.json.gz"
CITY_LIST_GZ = "city.list.json.gz"

def download_cities_file():
    """
    Downloads gzip file with all cities in it
    """
    with open(CITY_LIST_GZ, 'wb') as bf:
        try:
            response = requests.get(URL)

        # Return an HTTPError if an error has occurred during the process
        # If the response was successful, no Exception will be raised
            response.raise_for_status()
            for block in response.iter_content():
                bf.write(block)
        except HTTPError as http_e:
            print(f"An HTTP error occurred: {http_e}")
        except ConnectionError as connection_e:
            print(f"A Connection error occurred: {connection_e}")

