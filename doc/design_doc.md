# 💻 Software Design

- Author: Jordan, Hsuan, Viet, Ziqi
- Reviewer: Kyle

## 🎯 Overview

---

- The main target of this project is to **design a calendar-related command line interface (CLI).**

## 📗 Context

---

We are going to build four different modules in four different files under the same directory, and then import them all into the main function to make the code looks tidier.

**_We will each commit and push the finished part on github and will merge them back to main branch to finish this product._**

**Four modules:**

1.  `number_of_days(year, month)`

    **_Description:_** The function will return the total days in a specific month of the year.

    **_Solution:_** We will build a python module leveraging _calendar.monthrange(year, month)_ to accomplish this requirement.

2.  `number_of_leap_years(year1, year2)`

    **_Description:_** The function will return the number of leap years between year1, and year2, including year1 and year2 if there are also leap years.

    **_Solution:_** We will build a python module taking year1 and year2 as input and do mathematical calculation like this:

```python
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

3.  `get_week_of_day(year, month, day)`

    **_Description:_** The function will return what week the date is with the year. E.g., 01/08/2023 is week-2 of 2023, so the function will return 2.

    **_Solution:_** We will use _datetime_ in python to transform the date in the year to the week of the year.

    ```python
    date = datetime.strptime(date_string, "%d/%m/%Y")
    week_number = date.strftime("%W")
    year = date.strftime("%Y")
    ```

4.  log

    **_Description:_** The log file will track the datetime, user's name, and activities, and all the logs should be written in inverse chronological order. The file can be simply a `log` file, `.txt`, `.csv`, etc.

    | DATETIME  | NAME | ACTIVITY      |
    | --------- | ---- | ------------- |
    | DateTime1 | Mike | Command1(...) |
    | DateTIme2 | Mike | Command2(...) |
    | DateTime3 | Jack | Command3(...) |

    **_Solution:_** Write a function that will combine the datetime, user's name, and activities into a string, and then open the log file and write them in.
