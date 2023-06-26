# 📚GitEducation

## 📃Summary

In this project, you will learn how to collaborate with other developers with Git technology. To achieve the training goal, the team will design a calendar-related command line interface (CLI). The requirements of the CLI will be discussed in the following section. Designed by @cheniwei.

## 🔰Canlendar CLI

### Introduction

The client wants to build a CLI for three useful commands, `number_of_days`, `number_of_leap_years`, and `get_week_of_day`. Moreover, the CLI will provide a log file to track the user's name and the user's activities.

### Requirements

* `number_of_days(year, month)`

    The function will return the total days in a specific month of the year.

* `number_of_leap_years(year1, year2)`

    The function will return the number of leap years between year1, and year2, including year1 and year2 if there are also leap years.

* `get_week_of_day(year, month, day)`

    The function will return what week the date is with the year. E.g., 01/08/2023 is week-2 of 2023, so the function will return 2.

* log

    The log file will track the datetime, user's name, and activities, and all the logs should be written in inverse chronological order. The file can be simply a `log` file, `.txt`, `.csv`, etc.

    | DATETIME | NAME | ACTIVITY |
    |---|---|---|
    | DateTime1 | Mike | Command1(...) |
    | DateTIme2 | Mike | Command2(...) |
    | DateTime3 | Jack | Command3(...) |

