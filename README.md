# CLI-matic

![Banner](assets/images/banner.png)

CLI-matic is a Python command line tool for displaying weather forecasts. It requests data by making an API call to the [Open Weather Map](https://openweathermap.org/api) service provider using Python's [requests](https://requests.readthedocs.io/en/latest/) library. The interface is very simple. The user is navigated by specific and simple instructions. Weather forecasts are also displayed in a table using Python's [rich](https://rich.readthedocs.io/en/stable/introduction.html#:~:text=Rich%20is%20a%20Python%20library,in%20a%20more%20readable%20way.) library.

## Contents

- [CLI-matic](#cli-matic)
  - [Contents](#contents)
  - [Objective](#objective)
  - [User Experience](#user-experience)
  - [Data Model](#data-model)
  - [Design](#design)
    - [ASCII Art](#ascii-art)
    - [Colors](#colors)
  - [Existing Features](#existing-features)
    - [Home screen](#home-screen)
    - [Main Menu](#main-menu)
    - [Forecast Menu](#forecast-menu)
    - [City Entry](#city-entry)
    - [Select City](#select-city)
    - [Current Weather Forecast](#current-weather-forecast)
    - [Daily Weather Forecasts at 3-hour Intervals](#daily-weather-forecasts-at-3-hour-intervals)
    - [Exit](#exit)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Python Libraries](#python-libraries)
  - [Testing](#testing)
    - [PEP8 Validation](#pep8-validation)

## Objective

The primary goal of the project is to develop a simple mock terminal application using the Python programming language. In addition, one of the most important purposes of the application is to request data from service providers using API and to display this data on the screen in a format that the user can read.

You can view the live site here - [CLI-matic](https://cli-matic.herokuapp.com/)

[Back to top](<#contents>)

## User Experience

The repository used to develop the application is a Node.js mock terminal application prepared by Code Institute. Since this project was developed as part of the Code Institute education, no changes were necessary to the appearance of the application in the browser. But to make the terminal look a little more user friendly, some Python libraries/modules are used for coloring texts, creating tables and presenting content.

Here are some user experience criteria that were considered while developing the application:

- As a user, I would like to see a simple interface.
- As a user, I don't want to read too much content.
- As a user, I would like to see the weather forecast of the city I am looking for in a proper format.
- As a user, I would like to see clear navigation.
- As a user, I don't want to enter too many inputs to use the app.

The application has been developed considering the above criteria.

[Back to top](<#contents>)

## Data Model

CLI-matic requests all data from the Open Weather Map service provider. Data requests are made in 3 different ways.

- Request for gzip file with city names
- Requesting city coordinates with the Geolocation API
- Requesting current weather data and 3 hourly daily weather data with the OWM API

There is no need to make an API call to request data with city names. In order to receive this data, an HTTPS request was made with the Python request library. Since the requested data is in gzip format, the data was first saved as a gzip file. Then, with the 'with' statement and open() function, the city name was taken from the data and appended to the city list variable. The city name entered by the user is checked from this list and its validity is determined.

After the city name is validated, the name of the city is passed to the URL of the Geocoding API and the data about this city is requested with an API call. The latitude and longitude of the city were taken from the requested data and assigned to the latitude and longitude variables globally. Since the latitude and longitude fetched after the Geocoding API call, this data will be used to request weather forecast data and these variables will be called from another function, so the variables are globalized.

Finally, the fetched latitude and longitude data are passed to the URL that will be used in the API call from which weather forecast data will be requested. The data fetched from weather forecast API call is filtered with a very simple 'Weather' class, and the data to be displayed is presented in a table using the rich library.

Below is a simple flowchart showing the data flow.

<details><summary>CLI-matic Flowchart</summary>

![flowchart](assets/images/flowchart.drawio.png)
</details>

[Back to top](<#contents>)

## Design

Since this is a command line tool, what can be done in terms of design is very limited. Therefore, ASCII characters were created and the text content was colored.

### ASCII Art

The ASCII characters seen on the screens at the beginning of the application and after the program is exited are created using the [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) library.

### Colors

The [termcolor](https://pypi.org/project/termcolor/) library was used to color the contents.

[Back to top](<#contents>)

## Existing Features

### Home screen

It is the first screen that the user sees when the application is opened. On this screen, the name of the application is printed as a banner with ASCII characters and the user is asked to press ENTER to continue.

<details><summary>Home Screen Screenshot</summary>

![flowchart](assets/images/banner.png)
</details><br/>

[Back to top](<#contents>)

### Main Menu

On this screen, the user is greeted and a brief information about the application is given. In addition, the user is presented with options for navigation.

<details><summary>Main Menu Screenshot</summary>

![flowchart](assets/images/greeting_and_main_menu.png)
</details><br/>

[Back to top](<#contents>)

### Forecast Menu

On this screen, the user is presented with 3 different options. Two of them are what type of weather forecast the user wants to display, and the last one is whether the user wants to return to the main menu.

<details><summary>Forecast Menu Screenshot</summary>

![flowchart](assets/images/forecast_type_menu.png)
</details><br/>

[Back to top](<#contents>)

### City Entry

On this screen, the user is asked to enter the name of the city for which the user wants to see the weather forecasts.

<details><summary>City Entry Screenshot</summary>

![flowchart](assets/images/enter_city_name_section.png)
</details><br/>

[Back to top](<#contents>)

### Select City

More than 1 result can be fetched for the desired city name. (for instance, London in the UK and London in the US). In such a case, the user is asked which city the user wants data to be displayed. The data is displayed in line with the answer given by the user.

<details><summary>Select City Screenshot</summary>

![flowchart](assets/images/city_list_options.png)
</details><br/>

[Back to top](<#contents>)

### Current Weather Forecast

On this screen, the current weather forecasts for the asked city are displayed in a table. Below the table, 3 different navigation options are presented to the user. According to the user's selection, the relevant screen is returned.

<details><summary>Current Weather Forecast Screenshot</summary>

![flowchart](assets/images/current_weather_table.png)
</details><br/>

[Back to top](<#contents>)

### Daily Weather Forecasts at 3-hour Intervals

On this screen, daily weather forecasts are displayed at 3-hour intervals. As in the current weather forecasts screen, 3 different navigation options are presented to the user here, too.

<details><summary>Daily Weather Forecasts at 3-hour Intervals Screenshot</summary>

![flowchart](assets/images/3_hour_step_forecast_table.png)
</details><br/>

[Back to top](<#contents>)

### Exit

This is the screen where the program is terminated. On this screen, the user is greeted and given the necessary information to re-run the application.

<details><summary>Exit Screenshot</summary>

![flowchart](assets/images/exit.png)
</details><br/>

[Back to top](<#contents>)

## Future Features


- It will be an effective and useful option to determine the location of the user using the application and quickly show the weather forecasts for the location of the user.

- The application uses the free option of OWM. Therefore, a limited number of options are offered. Offering more comprehensive weather forecasts will increase user diversity.

- Showing images/emojis according to the weather conditions on the screen where the weather forecasts are displayed can make the application more attractive.

[Back to top](<#contents>)

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML) - Used for structuring and presenting content on the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Used for styling the website.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Used to provide the functionality of the application.
- [VSCode](https://code.visualstudio.com/) - Used to create and edit the application.
- [Git](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Used as version control system to track changes in development process.
- [GitHub](https://github.com/) - Used to host the project's files and folders.
- [Heroku](https://www.heroku.com/) - Used to deploy the project
- [Draw.io](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) - Used to make flowchart of the application.

[Back to top](<#contents>)

## Python Libraries

The following Python libraries were used in the development of the project.

- [requests](https://requests.readthedocs.io/en/latest/) - Used to request data.
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - Used to create ASCII texts.
- [termcolor](https://pypi.org/project/termcolor/) - Used to color text.
- [rich](https://rich.readthedocs.io/en/stable/introduction.html#:~:text=Rich%20is%20a%20Python%20library,in%20a%20more%20readable%20way.) - Used to display weather forecasts in a table.
- [country-converter](https://pypi.org/project/country-converter/0.3.1/) - Used to convert country codes into names.
- [os](https://docs.python.org/3/library/os.html) - Used to provide a way to use OS dependent functionality (e.g; cleaning the terminal screen).
- [json](https://docs.python.org/3/library/json.html) - Used to convert file object to JSON object.
- [datetime](https://docs.python.org/3/library/datetime.html) - Used to convert timestamp to human-readable/formatted string.
- [gzip](https://docs.python.org/3/library/gzip.html) - Used to decompress gzip file.

[Back to top](<#contents>)

## Testing

### PEP8 Validation

Validation tests were performed using the [CI Python Linter](https://pep8ci.herokuapp.com/) provided by the Code Institute. Errors that emerged as a result of the tests have been corrected and screenshots of the error free testing have been taken. 

<details><summary>run.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/run.py-validation.png)
</details><br/>

<details><summary>main.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/main.py-validation.png)
</details><br/>

<details><summary>print.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/print.py-validation.png)
</details><br/>

<details><summary>cities.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/cities.py-validation.png)
</details><br/>

<details><summary>api_call.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/api_call.py-validation.png)
</details><br/>

<details><summary>weather.py Testing Screenshot</summary>

![flowchart](assets/pep8-validation-images/weather.py-validation.png)
</details><br/>

[Back to top](<#contents>)