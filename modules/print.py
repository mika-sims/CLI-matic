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

    blank_lines()
    print("Display weather forecasts for over 200,000 cities".center(80))
    banner = pyfiglet.figlet_format("CLI - matic", justify="center")
    print(colored(banner, "yellow"))


def main_menu():
    """
    Displays the main menu to the user.
    """
    
    clear()
    blank_lines()
    print("CLI-matic displays weather forecasts for current"
        "location or another location.".center(80))
    print()
    print()
    print(colored("Type 1 to display the weather forecast"
                " for the current location", "yellow").center(80))
    print()
    print()
    print(colored("Type 2 to display the weather forecast"
                " for a specific location", "yellow").center(80))

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