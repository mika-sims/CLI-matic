from print import main_menu
from print import warning_text,clear, blank_lines

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
    return target_location

get_target_location()