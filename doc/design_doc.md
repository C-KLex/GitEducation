# 💻 Software Design

- Author: Jordan, Hsuan, Viet, Ziqi
- Reviewer: Kyle

## 🎯 Overview

---

- The main target of this project is to **design a calendar-related command line interface (CLI).**

## 📗 1. How this CLI works

---
There will be *three* modules for the CLI to work, whose names are *Calender*, *Log*, and *Main*.  

### 1.1 Calender:

>- There will be three functions for the user to call: ***"number_of_days"***, ***"number_of_leap_years"***, ***"get_week_of_day"***.  

>- Each function takes the necessary time factors as an input, and then return the number the user wants to know.

### 1.2 Log:

>- If this function is called with an ***"number_of_days"*** input, record the user login datetime, the username, and the activity as ***"number_of_days"***

>- If this function is called with an ***"get_week_of_day"*** input, record the user login datetime, the username, and the activity as ***"get_week_of_day"***

>- If this function is called with an ***"number_of_leap_years"*** input, record the user login datetime, the username, and the activity as ***"number_of_leap_years"***


### 1.3 Main:  

>- Take the user name as the first input, and then ask for the function the user wants to call. There will be three functions for user to choose: ***day***, ***week***, ***year***. 

>- If the input string is ***day***, ask the user to give the *year* and *month* as input and feed them to the ***number_of_days*** function from *Calender* module, and then call the *Log* module;

>- If the input string is ***week***, ask the user to give the *year*, *month*, and *day* as input and feed them to the ***get_week_of_day*** function from *Calender* module, and then call the *Log* module; 

>- If the input string is ***year***, ask the user to give the *year1* and *year2* as input and feed them to  the ***number_of_leap_years*** function from *Calender* module, and then call the *Log* module;  

>- If the input string is none of the above, return ***Wrong instuction, please try again.***


## 🖼️ 2. UI UX

---
The UI UX will have three different lines:

### 2.1:
```console
Welcome! Please tell us your name:
```

### 2.2:
```console
Which tool you want to use today? (day, week, year)
```

### 2.3:
```console
Here is the information you want to know: 
```

## 🔍 3. How does each module look like

---

>We are going to build three different modules under the same directory, and then import them all into the main function to make the code looks tidier.

>**We will each commit and push the finished part on github and will merge them back to main branch to finish this product._**

### 3.1 Calender module

```python
def number_of_days(year: int, month: int) -> int():
    """
    Return number of days in the sepecifc year month.
    """

    # code 

    return: int

def number_of_leap_years(year1: int, year2: int) -> int():
    """
    Return the number of leap years between year1, and year2, including year1 and year2 if there are also leap years.
    """
    # We will do mathematical calculation like this:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # code 

    return: int

def get_week_of_day(year: int, month: int, day: int) -> int():
    """
    Return what week the date is with the year. E.g., 01/08/2023 is week-2 of 2023, so the function will return 2.
    """

    # code 

    return: int
```

### 3.2 Log module

```python
# File log
def write_log(username: str, function_name: str) -> None():
    """
    Track the datetime, user's name, and activities.
    All the logs should be written in inverse chronological order.
    """
    return 
```

### 3.3 Main module

```python
# File main
def main() -> int():
    """
    Connect the other two modules and make this project work.
    """
    username = input(Welcome! Please tell us your name): string
    function_name = input("Which tool you want to use today? (day, week, year)"): string

    if function_name == "day":
        year = input(Year)
        month = input(Month)
        number_of_days(year: int, month: int)
        log(username, function_name)
    elif function_name == "week":
        year = input(Year: )
        month = input(Month: )
        day = input(Day: )
        number_of_days(year: int, month: int, day: int)
        log(username, function_name)
    elif function_name == "year":
        year1 = input(Year1: )
        year2 = input(Year2: )
        number_of_leap_years(year1: int, year2: int)
        log(username, function_name)
    else:
        return "Wrong instuction, please try again."
```
