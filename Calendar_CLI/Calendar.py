"""
GitEducation/Calendar_CLI/Calendar.py

The essential module containing the calendar related function. 

Author: Kyle, Hsuan, Viet, Jordan
Date: 20230626
"""
import datetime

def number_of_days(year, month):
    """
    This function returns the total days in a specific month of the year.

    args:
        year: posittive or negative integer (corresponding to BC and AD)
        month: integer between 1 and 12
    """

    # Returns the number of days in the month depending on the year and month. 
    if (month == 2):
        if (year > 0):
            if ((year % 4 == 0) and (year % 100 != 100)) or ((year % 100 == 0) and (year % 400 == 0)):
                return 29
            else:
                return 28
        elif (year < 0):
            if (((abs(year) - 1) % 4 == 0) and ((abs(year) - 1) % 100 != 100)) or (((abs(year) - 1) % 100 == 0) and ((abs(year) - 1) % 400 == 0)):
                return 29
            else:
                return 28
        else: 
            raise ValueError("0 is not a valid year. Please enter either a positive or negative number, corresponding to BC or AD.")
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    else:
        return 30

def number_of_leap_years(year1: int, year2: int) -> int():
    """
    Return the number of leap years between year1, and year2, including year1 and year2 if there are also leap years.

    Args:
        year1 (int): the year to start counting leap year.  
        year2 (int): the year to stop counting leap year.  
    
    Returns:
        int: return the number of leap years appeared in this time interval.
    """
    count = 0
    for year in range(year1, year2 + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            count += 1
    return count


def get_week_of_day(year: int, month: int, day: int) -> int():
    """
    Return what week the date is with the year. Every 1/1 to 1/7 of the year will be considered as week 1.
    args:
        year: postive integer(AD only)
        month: from 1 to 12
        days: depends on month and leap year, from 1 to {28,29,30,31}
    """
    try:
        date = datetime.date(year, month, day)
        first_day_of_year = datetime.date(year, 1, 1)

        # Calculate the number of days between the provided date and the first day of the year
        delta = date - first_day_of_year
        week_number = delta.days // 7 + 1
        return week_number

    except ValueError:
        return "Error: Invalid Date "
