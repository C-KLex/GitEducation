# File log

import datetime
import pandas as pd


def write_log(username: str, function_name: str) -> None():
    """
    Track the datetime, user's name, and activities.
    All the logs should be written in inverse chronological order.
    """

    # parse existing file
    df = pd.read_csv('log.csv')

    # add new row on the top of dataframe
    time = datetime.datetime.now()
    newrow = pd.Series([time, username, function_name], index = df.columns)
    df = pd.concat([newrow, df]).reset_index(drop=True)

    return 