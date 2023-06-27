def number_of_days(year, month):
    """
    This function returns the total days in a specific month of the year.
    
    args:
        year: integer
        month: integer between 1 and 12
    """

    # Returns the number of days in the month depending on the year and month. 
    if (month == 2) and (((year%4 == 0) and (year%100 != 100)) or ((year%100 == 0) and (year%400 == 0))):
        return 29
    elif (month == 2):
        return 28
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 10):
        return 31
    else:
        return 30