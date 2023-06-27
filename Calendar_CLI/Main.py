"""
GitEducation/Calendar_CLI/Main.py

Main run file for the CLI.

Author: Jordan, Kyle
Date: 20230626
"""

from Calendar_CLI.Calendar import number_of_days, number_of_leap_years, get_week_of_day
from Calendar_CLI.Log import write_log


def main():
    """
    Connect the other two modules and make this project work.
    """
    username = input("Welcome! Please tell us your name: ")
    function_name = input("Which tool you want to use today? (day, week, year)")

    if function_name == "day":
        year = input("Year: ")
        month = input("Month: ")
        print(number_of_days(year, month))
        write_log(username, function_name)
    elif function_name == "week":
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        print(get_week_of_day(year, month, day))
        write_log(username, function_name)
    elif function_name == "year":
        year1 = input("Year1: ")
        year2 = input("Year2: ")
        print(number_of_leap_years(year1, year2))
        write_log(username, function_name)
    else:
        return "Wrong instuction, please try again."
