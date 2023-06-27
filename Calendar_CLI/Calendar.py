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
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 10):
        return 31
    else:
        return 30