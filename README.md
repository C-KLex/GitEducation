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

## 👩‍🎨Design Document

Since this is a team assignment, you are supposed to design the overall product and write it down. Here are some key topics a team should discuss firsthand.

* Software Design

    It's the blueprint of the software to make all the developers on the same page. The goal is to achieve the client's requirements.

* Coding Style Guideline

    If everyone codes in their way individually, it will be a disaster, it's hard to read other's code. Create a coding style guideline to make all the contributors follow the same style principle.

* Naming Convention

    Make sure everyone has the same naming convention, including variable, class, function, script, file name, etc.

* Documentation Guideline

    Discuss how to write commit, function description, script description, module description, package description, etc.

* Guideline Example: <https://github.com/C-KLex/GymBro/blob/main/GuideLines.md>

## 💬Git Commit Guideline

* Commit Message:

    ```bash
    git commit -m "label: this is a commit summary" -m "this is a commit description (optional)"
    ```

  * Commit Message Style: **all lowercase letters**

  * Label Reference:

    ![image](https://github.com/C-KLex/GitEducation/assets/87312700/e1965358-a970-4116-a260-86d98150ce26)

  * Reference: <https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/>

* Commit Principle: More Commits but Tiny Changes.

    Each commit should represent a specific little change. Don't add too many changes in only one commit because it will make the commit FAT, making it harder to track the history.

## 🌲Branching Guideline

* General Branch Naming:

    ```bash
    git branch name/whatYouWantToDo
    git branch kyle/addNewButton
    ```

* Branch Name Style: `name` in lowercase, `whatYouWantToDO` in camelCase

    ```bash
    git branch lowercase/camelCase
    ```

## 🦮PR Guideline

* Clear Task

    One PR is only for one task, don't mix multiple tasks into one PR, which will make reviewers hard to review and hard to trace back. For example, let's say PR1 is about `Adding Login Button` and PR1 also contains the changes about `Connecting Login Button with Backend`; then, PR1 is not simple anymore due to the mixture of multiple tasks.

* Small PR

    Some tasks can be enormous, meaning that a lot of code changes would be done at the same time. In this case, it's better to separate the tasks into pieces and PR each of them individually. For example, I need to do a `login module`. I can't simply finish all the code and make it into a single PR, it would be very hard to review. Therefore, I decompose the main tasks into `login page UI`, `login page UX link`, and `login page backend`. Then, I PR one small progress every time I've done a feature.

* Fix Conflict

    Before opening the PR, always check the potential merge conflict first. For example, I want to PR `feature` branch into `main` branch. Before opening the PR, I should always merge `main` into `feature` to see if there is any conflict existing, and if so, I should solve the conflict carefully without ruining other's work from `main`. Therefore, a good merge conflict-solving skill is required, and it takes experience to ace the skill!

## 📜Pull Request Template

* Title, Summary, Detail, Screenshots

    These four components are useful in a PR Report. They are all optional, and you can add more or decide not to use any. For example, you may not be able to provide screenshots in some cases.

* Example: <https://github.com/C-KLex/GymBro/pull/18>

    ![image](https://github.com/C-KLex/GitEducation/assets/87312700/08cee987-dbf1-41e6-9c28-860ed20dd6b6)

## 🌊Git Reminder

Here are some key tips to have a better git experience.

* Know Which Branch You Are In

* Know Which Branch You Want To Merge In

* Know How to Solver Merge Conflict Carefully

* Understand How Much Your Work

* Know When to Stop to Create a Commit

* Know When Should Touch the Main and When Shouldn't
