# CLI-matic

![Banner](assets/images/banner.png)

CLI-matic is a Python command line tool for displaying weather forecasts. It requests data by making an API call to the [Open Weather Map](https://openweathermap.org/api) service provider using Python's [requests](https://requests.readthedocs.io/en/latest/) library. The interface is very simple. The user is navigated by specific and simple instructions. Weather forecasts are also displayed in a table using Python's [rich](https://rich.readthedocs.io/en/stable/introduction.html#:~:text=Rich%20is%20a%20Python%20library,in%20a%20more%20readable%20way.) library.

## Contents

- [CLI-matic](#cli-matic)
  - [Contents](#contents)
  - [Objective](#objective)
  - [User Experience](#user-experience)
  - [Data Model](#data-model)

## Objective

The primary goal of the project is to develop a simple mock terminal application using the Python programming language. In addition, one of the most important purposes of the application is to request data from service providers using API and to display this data on the screen in a format that the user can read.

You can view the live site here - [CLI-matic](https://cli-matic.herokuapp.com/)

## User Experience

The repository used to develop the application is a Node.js mock terminal application prepared by Code Institute. Since this project was developed as part of the Code Institute education, no changes were necessary to the appearance of the application in the browser. But to make the terminal look a little more user friendly, some Python libraries/modules are used for coloring texts, creating tables and presenting content.

Here are some user experience criteria that were considered while developing the application:

- As a user, I would like to see a simple interface.
- As a user, I don't want to read too much content.
- As a user, I would like to see the weather forecast of the city I am looking for in a proper format.
- As a user, I would like to see clear navigation.
- As a user, I don't want to enter too many inputs to use the app.

The application has been developed considering the above criteria.

## Data Model

CLI-matic requests all data from the Open Weather Map service provider. Data requests are made in 3 different ways.

- Request for gzip file with city names
- Requesting city coordinates with the Geolocation API
- Requesting current weather data and 3 hourly daily weather data with the OWM API

There is no need to make an API call to request data with city names. In order to receive this data, an HTTPS request was made with the Python request library. Since the requested data is in gzip format, the data was first saved as a gzip file. Then, with the 'with' statement and open() function, the city name was taken from the data and appended to the city list variable. The city name entered by the user is checked from this list and its validity is determined.

After the city name is validated, the name of the city is passed to the URL of the Geocoding API and the data about this city is requested with an API call. The latitude and longitude of the city were taken from the requested data and assigned to the latitude and longitude variables globally. Since the latitude and longitude fetched after the Geocoding API call, this data will be used to request weather forecast data and these variables will be called from another function, so the variables are globalized.

Finally, the fetched latitude and longitude data are passed to the URL that will be used in the API call from which weather forecast data will be requested. The data fetched from weather forecast API call is filtered with a very simple 'Weather' class, and the data to be displayed is presented in a table using the rich library.

Below is a simple flowchart showing the data flow.

<details><summary><b>CLI-matic Flowchart</b></summary>

![flowchart](assets/images/flowchart.drawio.png)
</details><br />