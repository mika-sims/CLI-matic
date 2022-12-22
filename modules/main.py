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
    
    Returns:
        str: Users current location
    """

    clear()
    blank_lines()
    yellow_text("Please enter the name of the city you live in.")
    print()
    while True:
        user_location = input("".center(35)).title()
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
    return user_location


def main_menu_user_input():
    """
    Provides input to the user

    Returns:
        _type_: _description_
    """
    while True:
        print()
        user_input = input("".center(35))
        if user_input not in ["1","2","3"]:
            print()
            main_menu()
            print()
            warning_text("Invalid input! Please try again.")
        else:
            break
    if user_input == "1":
        forecast_menu()
        forecast_menu_user_input()
        set_geolocation_url(get_user_location())
    if user_input == "2":
        forecast_menu()
        forecast_menu_user_input()
        set_geolocation_url(get_target_location())
    if user_input == "3":
        clear()
        main_menu()

def forecast_menu_user_input():
    """
    Gets input from user for weather forecast type
    """

    while True:
        print()
        forecast_type = input("".center(35))
        if forecast_type not in ["1", "2", "3"]:
            clear()
            forecast_menu()
            print()
            warning_text("Invalid input! Please try again.")
            continue
        else:
            break

    forecast_type = int(forecast_type)

    if forecast_type == 1:
        pass
    if forecast_type == 2:
        pass
    if forecast_type == 3:
        main_menu()


def get_target_location():
    """
    Asks the user for which city the forecast will be displayed
    """
    clear()
    blank_lines()
    while True:
        white_text("Which city would you like to display the forecast for?")
        print()
        green_text("Please enter a city name.")
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


def set_geolocation_url(target_location):
    """
    Sets the URL of the API call to find the coordinates
    of the target location

    Args:
        target_location (int): The return value of the
                                get_target_location function 
    """

    city = target_location
    base_url = "http://api.openweathermap.org/geo/1.0/direct?"
    geolocation_url = f"{base_url}q={city}&limit=3&appid={OWM_API_KEY}"

    return geolocation_url


def run():
    banner()

# def get_geolocation_data(url):
#     """
#     Returns location coordinates data as a JSON object

#     Args:
#         url (str): The URL of the API call to be made for the location
#                     to get the coordinates
#     """
#     geolocation_data = api_call(url)
#     print(geolocation_data)


if __name__ == '__main__':
    run()
    main_menu_user_input()