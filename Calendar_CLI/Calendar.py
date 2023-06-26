import datetime

def get_week_of_day(year: int, month: int, day: int) -> int:
    """
    Return what week the date is with the year. Every 1/1 to 1/7 of the year will be considered as week 1.
    args:
        year: postive integer(AD only)
        month: from 1 to 12
        day: from 1 to 31(except for Feb, Apr, June, Sep, Nov)
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