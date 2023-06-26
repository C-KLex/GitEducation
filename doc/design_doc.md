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

>- First it takes a user choiced function name as an input, and then with the specific function name, call the corresponding function.

>- If the input string is ***day***, call the ***number_of_days*** function;  
If the input string is ***week***, call the ***get_week_of_day*** function;  
If the input string is ***year***, call the ***number_of_leap_years*** function;  
If the input string is none of the above, return ***Wrong instuction, please try again.***.

>- Inside each time function, there needs to be a input to ***Log*** function to record the activity.


### 1.2 Log:

>- If this function is called with an ***"number_of_days"*** input, record the user login datetime, the username, and the activity as ***"number_of_days"***

>- If this function is called with an ***"get_week_of_day"*** input, record the user login datetime, the username, and the activity as ***"get_week_of_day"***

>- If this function is called with an ***"number_of_leap_years"*** input, record the user login datetime, the username, and the activity as ***"number_of_leap_years"***


### 1.3 Main:  

>- Take the user name as the first input, and then ask for the function the user wants to call. There will be three functions for user to choose: ***day***, ***week***, ***year***. After the user choose it, call the ***Calender*** function.


## 🖼️ 2. UI UX

---
The UI UX will have three different lines:

### 2.1:
```bash
Welcome! Please tell us your name:
```

### 2.2:
```bash
Which tool you want to use today? (day, week, year)
```

### 2.3:
```bash
Here is the information you want to know: 

```

## 🔍 3. How does each module look like

---

>We are going to build three different modules under the same directory, and then import them all into the main function to make the code looks tidier.

>**We will each commit and push the finished part on github and will merge them back to main branch to finish this product._**

### 3.1 Calender module:   

```python
# File calender
calender(username, function_name):
    username: string, function_name: string
    return: int # return the number in the called function.
    Purpose of this function: call the specific functions to return the value that user wants.

# File functions
number_of_days(username):
    username: string
    input(Year: ): int
    input(Month: ): int
    return: int
    Purpose of this function: The function will return the total days in a specific month of the year. 
    
    We will build a python module leveraging _calendar.monthrange(year, month)_ to accomplish this requirement.

number_of_leap_years(username):
    username: string
    input(Year1: ): int
    input(Year2: ): int
    # We will do mathematical calculation like this:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return: int
    Purpose of this function: The function will return the number of leap years between year1, and year2, including year1 and year2 if there are also leap years.

get_week_of_day(username):
    username: string
    input(Year: ): int
    input(Month: ): int
    input(Day: ): int
    return: int
    Purpose of this function: The function will return what week the date is with the year. E.g., 01/08/2023 is week-2 of 2023, so the function will return 2.
```

### 3.2 Log module:

```python
# File log
log(username, status):
    username: string, status: string
    Purpose of this function: After intaking the status , combine the datetime, user's name, and activities into a string, and then open the log file and write them in.
```

### 3.3 Main module:

```python
# File main
main():
    username = input(Welcome! Please tell us your name): string
    function_name = input("Which tool you want to use today? (day, week, year)"): string
    return calender(username, function_name): int
    Purpose of this function: connect the other three modules and make this project work.
```
