"""
GitEducation/Calendar_CLI/Log.py

Module for any log module operations. 

Author: Ziqi, Kyle
Date: 20230626
"""

import datetime
import pandas as pd

def write_log(username: str, function_name: str) -> None():
    """
    Track the datetime, user's name, and activities.
    All the logs should be written in inverse chronological order.

    Parameters:
        username(str): name of user
        function_name(str): name of user's activity 
    """
    # parse existing file
    df = pd.read_csv('log.csv', header = 'infer')

    # add new row on the top of dataframe
    time = datetime.datetime.now()
    newrow = pd.Series([time, username, function_name], index = df.columns)
    df = pd.concat([newrow, df]).reset_index(drop = True)

    # export dataframe to csv
    df.to_csv('log.csv')

    return 