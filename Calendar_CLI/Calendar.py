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
