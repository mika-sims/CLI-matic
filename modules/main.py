# Import json library
import json

# Import functions from print.py module
from print import main_menu
from print import warning_text, clear, blank_lines

# Import api_call function from api_call module
from api_call import api_call


# Reads creds file and asigns api keys to variables
with open("creds.json","r") as credentials:
    api_keys = json.load(credentials)
    IPDATA_API_KEY = api_keys["ipdata_api_key"]
    OWM_API_KEY = api_keys["owm_api_key"]

def get_target_location():
    """
    Asks the user for which city the forecast will be displayed
    """
    
    while True:
        try:
            main_menu()
            target_location = int(input("".center(40)))
        except ValueError:
            clear()
            blank_lines()
            warning_text("Invalid entry!")
            warning_text("Please try again.")
            continue
        if target_location not in [1, 2]:
            clear()
            blank_lines()
            warning_text("Invalid entry!")
            warning_text("Please try again.")
            continue
        else:
            break
    set_geolocation_url(target_location)


def set_geolocation_url(target_location):
    """
    Sets the URL of the API call to find the coordinates
    of the target location

    Args:
        target_location (int): The return value of the
                                get_target_location function 
    """
    
    if target_location == 1:
        geolocation_url = f"https://api.ipdata.co?api-key={IPDATA_API_KEY}"
    elif target_location == 2:
        city = get_target_city_name()
        geolocation_url = f"http://api.openweathermap.org/geo/1.0/direct?q= \
                            {city}&limit=3&appid={OWM_API_KEY}"

    get_geolocation_data(geolocation_url)

def get_target_city_name():
    """
    Gets parameters for target city from user
    """
    while True:
        try:
            print("Please enter a city name.".center(80))
            city = input("".center(40))
        except ValueError:
            print("Invalid city name!")
            continue
        if len(city) == 0:
            print("City name can't be empty! Please try again.".center(80))
            continue
        elif any(char.isdigit() for char in city):
            print("City name can't contain number. Please try again." \
                .center(80))
        else:
            break
    return city

def get_geolocation_data(url):
    """
    Returns location coordinates data as a JSON object

    Args:
        url (str): The URL of the API call to be made for the location
                    to get the coordinates
    """
    geolocation_data = api_call(url)
    print(geolocation_data)


get_target_location()