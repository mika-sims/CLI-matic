# Import os library
import os

# Import pyfiglet to create the app banner
import pyfiglet

# Import colored modul from termcolor for colored output
from termcolor import colored

def banner():
    """
    Prints application's banner.
    """
    clear()
    blank_lines()
    print("Display weather forecasts for over 200,000 cities".center(80))
    banner = pyfiglet.figlet_format("CLI - matic", justify="center")
    print(colored(banner, "yellow"))
    green_text("Press ENTER to continue")
    print()
    input("".center(35))
    clear()
    blank_lines()
    greeting()
    main_menu()


def greeting():
    yellow_text(f"Welcome to the CLI-matic.")
    print()
    white_text("With CLI-matic you can display the weather forecast")
    white_text("for your current location or for another location.")
    print()  

def main_menu():
    """
    Displays the main menu to the user.
    """

    yellow_text("Please choose an option from the menu below and press ENTER.")
    print()
    green_text("-For your current location type 1")
    green_text("-For another location type 2")
    green_text("-To exit the application type 3")

def forecast_menu():
    """
    Provides the user weather forecasts type
    """
    clear()
    blank_lines()
    white_text("CLI-matic provides 2 types of weather forecasts.")
    print()
    yellow_text("-For current weather forecasts type 1")
    yellow_text("-For weather forecasts with 3-hour step type 2")
    yellow_text("-To return to the main menu type 3")
    

def clear():
    """
    Cleans terminal to present content more cleanly
    """

    os.system("cls" if os.name == "nt" else "clear")

def blank_lines():
    """
    Prints blank lines to align content to the center of the terminal
    """
    print()
    print()
    print()
    print()


def warning_text(text):
    """
    Displays red warning text for invalid entries

    Args:
        text (str): Warning text to be displayed
    """
    print(colored(text, "red").center(80))

def green_text(text):
    """
    Prints green text

    Args:
        text (str): Text to be displayed
    """
    print(colored(text, "green").center(80))

def yellow_text(text):
    """
    Prints yellow text

    Args:
        text (str): Text to be displayed
    """
    print(colored(text, "yellow").center(80))

def white_text(text):
    """
    Prints white text

    Args:
        text (str): Text to be displayed
    """
    print(colored(text, "white").center(80))