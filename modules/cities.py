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


def cities_list(target_city):
    """
    Creates a list of city names from the downloaded file

    Args:
        target_city (str): Name of target city for weather forecast

    Returns:
        str: Target city
    """    
    
    download_cities_file()

    target_city = target_city.title()
    all_cities = []

    with gzip.open(CITY_LIST_GZ, "rb", "utf-8") as f:
        cities = json.loads(f.read())
        for city_dict in cities:
            all_cities.append(city_dict["name"])

        if target_city not in all_cities:
            print(f"No data found for {target_city}".center(80))
            return None
        else:
            return target_city