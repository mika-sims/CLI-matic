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

    banner = pyfiglet.figlet_format("CLI - matic", justify="center")
    print(colored(banner, "yellow"))

def greeting():
    """
    Prints a welcome message to the screen
    """
    greeting = pyfiglet.figlet_format("WELCOME", justify="center")
    print(colored(greeting, "green"))
    banner()
    print("Display weather forecasts for over 200,000 cities".center(80))
    print(colored("Press Enter to start", "green").center(90))
    input("".center(40))