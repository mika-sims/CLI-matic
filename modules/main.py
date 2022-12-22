# Import json library
import json

# Import country converter library
import country_converter as coco

# Import console and table from rich library to print data to console
from rich.console import Console
from rich.table import Table

# Import datetime to convert timestamp to datetime
from datetime import datetime

# Import functions from print.py module
from print import main_menu, forecast_menu, exit
from print import warning_text, clear, blank_lines, banner, green_text
from print import yellow_text, white_text

# Import api_call function from api_call module
from api_call import api_call

# Import cities list from cities module
from cities import cities_list

# Import Weather object from weather module
from weather import Weather

console = Console()

CITY_LIST = cities_list()

# Reads creds file and asigns api keys to variables
with open("creds.json","r") as credentials:
    api_keys = json.load(credentials)
    API_KEY = api_keys["api_key"]


def main_menu_user_input():
    """
    Provides input to the user

    Returns:
        _type_: _description_
    """
    while True:
        print()
        user_input = input("".center(35))
        if user_input not in ["1","2"]:
            print()
            clear()
            blank_lines()
            main_menu()
            print()
            warning_text("Invalid input! Please try again.")
        else:
            break
    if user_input == "1":
        forecast_menu()
        forecast_menu_user_input()
        
    if user_input == "2":
        exit()


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
        set_geolocation_url(get_target_location())
        current_weather_data(latitude, longitude)
    if forecast_type == 2:
        set_geolocation_url(get_target_location())
        hourly_weather_forecast_data(latitude, longitude)
    if forecast_type == 3:
        clear()
        blank_lines()
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
    geolocation_url = f"{base_url}q={city}&limit=3&appid={API_KEY}"

    geolocation_data(geolocation_url)


def geolocation_data(url):
    """
    Returns geolocation data as latitude and longitude

    Args:
        url (str): URL to get data
    """
    
    data = api_call(url)
    if len(data) > 1:
        clear()
        blank_lines()
        yellow_text("More than 1 result found for the searched city.")
        options = "Please select an option from the list below.\n".center(80)
        print()
        for i, option in enumerate(data):
            # Convert country code to country name
            country = coco.convert(names=option["country"], to="name")
            city_name = option["name"]
            options += f"\n \
                -Enter {str(i + 1)} for: {city_name},{country}"
        print(options)
        print()
        
        # Validate the user input
        while True:
            dict_index = input("".center(40))
            if dict_index not in ["1", "2", "3"]:
                clear()
                blank_lines()
                warning_text("No valid option selected! Please try again")
                print()
                print(options)
                print()
                continue
            else:
                break
    dict_index = int(dict_index)
    target_city_dict = data[dict_index - 1]
    global latitude
    latitude = target_city_dict["lat"]
    global longitude
    longitude = target_city_dict["lon"]
    return {latitude, longitude}


def current_weather_data(latitude, longitude):
    """
    Returns the current weather data as JSON object

    Args:
        latitude (float): Latitude of the city to get the weather forecast
        longitude (float): Longitude of the city to get the weather forecast
    """
    
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    weather_url = base_url + "lat=" + str(latitude) + "&lon=" + \
                str(longitude) + "&appid=" + API_KEY + "&units=metric"
    
    data = api_call(weather_url)
    display_current_weather(data)


def hourly_weather_forecast_data(latitude, longitude):
    """
    Returns the 3-hour interval weather forecasts data as JSON object

    Args:
        latitude (float): Latitude of the city to get the weather forecast
        longitude (float): Longitude of the city to get the weather forecast
    """
    
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    forecast_url = base_url + "lat=" + str(latitude) + "&lon=" + \
                str(longitude) + "&cnt=8&appid=" + API_KEY + "&units=metric"
    
    data = api_call(forecast_url)
    display_hourly_weather_forecast(data)
    
def display_current_weather(data):
    """
    Displays the current weather forecast in table format

    Args:
        data (list): Nested JSON object
    """
    
    # Call Weather object
    current_weather_obj = Weather(data)
    
    country = coco.convert(names=current_weather_obj.sys.country, to="name")
    
    day = datetime.utcfromtimestamp(current_weather_obj.dt).strftime("%a %d %b")
    time = datetime.utcfromtimestamp(current_weather_obj.dt).strftime("%H:%M")
    temperature = current_weather_obj.main.temp
    feels_like = current_weather_obj.main.feels_like
    min_temperature = current_weather_obj.main.temp_min
    max_temperature = current_weather_obj.main.temp_max
    humidity = current_weather_obj.main.humidity
    description = current_weather_obj.weather[0].description
    wind_speed = current_weather_obj.wind.speed
    location = current_weather_obj.name

    table = Table(
        show_header=True,
        header_style="bold blue",
        title=f"\n{location}, {country} current weather forecast for {day}",
    )
    
    table.add_column("Time", justify="center")
    table.add_column("Temperature", justify="center")
    table.add_column("Feels like", justify="center")
    table.add_column("Min Temperature", justify="center")
    table.add_column("Max Temperature", justify="center")
    table.add_column("Humidity", justify="center")
    table.add_column("Wind Speed", justify="center")
    table.add_column("Description", justify="center")

    table.add_row(
        str(time),
        str(temperature) + " °C",
        str(feels_like) + " °C",
        str(min_temperature) + " °C",
        str(max_temperature) + " °C",
        str(humidity) + " %",
        str(wind_speed) + " m/s",
        description.title(),
    )
    clear()
    console.print(table)
    print()
    navigation_menu()

def display_hourly_weather_forecast(data):
    """
    Prints the forecast in 3-hour intervals
    """
    # Call Weather object
    weather_obj = Weather(data)

    times = ""
    temperatures = ""
    feels = ""
    min_temperatures = ""
    max_temperatures = ""
    humidities = ""
    descriptions = ""
    city = weather_obj.city.name
    
    weather_obj_list = weather_obj.list
    for i in range(len(weather_obj_list)):

        day = datetime.utcfromtimestamp(weather_obj_list[i].dt) \
            .strftime("%a %d %b")
        time = datetime.utcfromtimestamp(weather_obj_list[i].dt) \
            .strftime("%H:%M")
        temperature = weather_obj_list[i].main.temp
        feels_like = weather_obj_list[i].main.feels_like
        min_temperature = weather_obj_list[i].main.temp_min
        max_temperature = weather_obj_list[i].main.temp_max
        humidity = weather_obj_list[i].main.humidity
        description = weather_obj_list[i].weather[0].description

        times += time + "\n"
        temperatures += str(temperature) + " °C" + "\n"
        feels += str(feels_like) + " °C" + "\n"
        min_temperatures += str(min_temperature) + " °C" + "\n"
        max_temperatures += str(max_temperature) + " °C" + "\n"
        humidities += str(humidity) + " %" + "\n"
        descriptions += description + "\n"

    table = Table(
        show_header=True,
        header_style="bold blue",
        title=f"{city} daily weather forecasts in 3-hour intervals for {day}",
    )

    table.add_column("Time", justify="center")
    table.add_column("Temp.", justify="center")
    table.add_column("Feels like", justify="center")
    table.add_column("Min Temp.", justify="center")
    table.add_column("Max Temp.", justify="center")
    table.add_column("Humidity", justify="center")
    table.add_column("Description", justify="center")

    table.add_row(
        times,
        temperatures,
        feels,
        min_temperatures,
        max_temperatures,
        humidities,
        descriptions.title(),
    )
    clear()
    console.print(table)    


def navigation_menu():
    """
    Provides navigation to the user
    """
    white_text("Please select an option from the menu below and press ENTER.")
    print()
    yellow_text("Type 1 to search for another city.")
    yellow_text("Type 2 to restart the app.")
    yellow_text("Type 3 to exit the app")
    
    while True:
        print()
        user_input = input("".center(35))
        if user_input not in ["1", "2", "3"]:
            print()
            warning_text("Invalid input! Please try again.")
            continue
        else:
            break
    if user_input == "1":
        clear()
        blank_lines()
        main_menu()
        main_menu_user_input()
    if user_input == "2":
        banner()
    if user_input == "3":
        exit()


def run():
    banner()
    main_menu_user_input()

if __name__ == '__main__':
    run()
    main_menu_user_input()