"""
GitEducation/Calendar_CLI/Log.py

Module for any log module operations. 

Author: Ziqi, Kyle
Date: 20230626
"""

import datetime
import pandas as pd

df = pd.read_csv('Calendar_CLI/Log.csv', header = 'infer')
df_new = pd.DataFrame([1, 2, 3]).T
df_new.columns = df.columns
df = pd.concat([df_new, df], axis=0, ignore_index=True)
print(df)

def write_log(username: str, function_name: str):
    """
    Track the datetime, user's name, and activities.
    All the logs should be written in inverse chronological order.

    Parameters:
        username(str): name of user
        function_name(str): name of user's activity 
    """
    # parse existing file
    df = pd.read_csv('Calendar_CLI/Log.csv', header = 'infer')

    # create new row
    time = datetime.datetime.now()
    df_new = pd.DataFrame([time, username, function_name]).T
    df_new.columns = df.columns

    # add new row to the data frame
    df = pd.concat([df_new, df], axis=0, ignore_index=True)

    # export dataframe to csv
    df.to_csv('Calendar_CLI/Log.csv')

    return 