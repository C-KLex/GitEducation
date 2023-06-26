from Calendar import number_of_days, number_of_leap_years, get_week_of_day
from Log import log


def main() -> int():
    """
    Connect the other two modules and make this project work.
    """
    username = input("Welcome! Please tell us your name: ")
    function_name = input("Which tool you want to use today? (day, week, year)")

    if function_name == "day":
        year = input("Year: ")
        month = input("Month: ")
        number_of_days(year, month)
        log(username, function_name)
    elif function_name == "week":
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        number_of_days(year, month, day)
        log(username, function_name)
    elif function_name == "year":
        year1 = input("Year1: ")
        year2 = input("Year2: ")
        number_of_leap_years(year1, year2)
        log(username, function_name)
    else:
        return "Wrong instuction, please try again."
