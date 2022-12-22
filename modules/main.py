# Import json library
import json

# Import functions from print.py module
from print import main_menu, forecast_menu
from print import warning_text, clear, blank_lines, banner, green_text
from print import yellow_text, white_text

# Import api_call function from api_call module
from api_call import api_call

# Import cities list from cities module
from cities import cities_list

CITY_LIST = cities_list()

# Reads creds file and asigns api keys to variables
with open("creds.json","r") as credentials:
    api_keys = json.load(credentials)
    IPDATA_API_KEY = api_keys["ipdata_api_key"]
    OWM_API_KEY = api_keys["owm_api_key"]


def get_user_location():
    """
    Gets the current location of the user
    """
    clear()
    banner()
    print()
    clear()
    blank_lines()
    white_text(f"Welcome to the CLI-matic.")
    print()
    white_text("Before moving on to the next step,")
    white_text("I will ask you for one last piece of information.")
    print()
    yellow_text("Please enter the name of the city you live in.")
    print()
    while True:
        user_location = input("".center(40)).title()
        if user_location not in CITY_LIST or len(user_location) < 1 or \
            user_location.isspace() or user_location == "" or \
            user_location.isdigit():

            clear()
            blank_lines()
            warning_text("There is no data for the city name you entered.")
            print()
            yellow_text("Please write the city name in English.")
            print()
            continue
        else:
            break
    main_menu()
    main_menu_user_input()


def main_menu_user_input():
    """
    Provides input to the user

    Returns:
        _type_: _description_
    """
    while True:
        user_input = input("".center(40))
        print()
        if user_input not in ["1","2","3"]:
            print()
            main_menu()
            print()
            warning_text("Invalid input! Please try again.")
        else:
            break
    if user_input == "1":
        forecast_menu()
    if user_input == "2":
        clear()
        blank_lines()
        get_target_location()
        forecast_menu()
    if user_input == "3":
        clear()
        main_menu()



def get_target_location():
    """
    Asks the user for which city the forecast will be displayed
    """
    
    while True:
        white_text("Which city would you like to display the forecast for?")
        white_text("Please enter a city name.")
        print()
        target_location = input("".center(40)).title()
        print()
        if target_location not in CITY_LIST:
            
            clear()
            blank_lines()
            warning_text("Invalid entry! Please try again.")
            print()
            continue
        else:
            break
    return target_location

get_user_location()

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


