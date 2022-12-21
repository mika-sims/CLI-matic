# Import requests library
import requests
from requests.exceptions import HTTPError, ConnectionError


def api_call(url):
    """
    Returns the response of the API call as JSON data

    Args:
        url (str): URL to make the API call

    Returns:
        object: JSON object
    """    
    try:
        # Returns a JSON object of the result
        response = requests.get(url)

        # Return an HTTPError if an error has occurred during the process
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        data = response.json()
        return data
    except HTTPError as http_e:
        print(f"An HTTP error occurred: {http_e}")
    except ConnectionError as connection_e:
        print(f"A Connection error occurred: {connection_e}")