"""
Test case

Author: Kyle
Date: 20230627
"""
import subprocess
import csv
import time 

from Calendar_CLI.Calendar import number_of_leap_years, number_of_days, get_week_of_day
from Calendar_CLI.Log import write_log

LOG_PATH_FROM_MAIN = 'Calendar_CLI/Log.csv'

class Test_Backend:

    def create_log(self):
        subprocess.run(["touch", LOG_PATH_FROM_MAIN])
        with open(LOG_PATH_FROM_MAIN, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["DATETIME", "NAME", "ACTIVITY"])
            f.close()
        return 

    def rm_log(self):
        subprocess.run(["rm", LOG_PATH_FROM_MAIN])
        return   

    def read_log(self):
        content = []
        with open(LOG_PATH_FROM_MAIN, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                content.append(line)
        return content
            

    def test_num_of_leap_year(self):
        assert number_of_leap_years(2016, 2020) == 2 
        assert number_of_leap_years(2015, 2017) == 1 
        assert number_of_leap_years(1700, 1701) == 0 
        assert number_of_leap_years(2100, 2104) == 1 

    def test_num_of_days(self):
        assert number_of_days(2023, 1) == 31 
        assert number_of_days(2000, 7) == 31 
        assert number_of_days(1998, 8) == 31 
        assert number_of_days(2023, 9) == 30 

        assert number_of_days(1900, 2) == 28
        assert number_of_days(2000, 2) == 29 
        assert number_of_days(2004, 2) == 29 
        assert number_of_days(2023, 2) == 28 

    def test_week_of_year(self):
        assert get_week_of_day(2023, 1, 3) == 1 
        assert get_week_of_day(2023, 1, 8) == 2 
        assert get_week_of_day(2023, 2, 4) == 5 
        assert get_week_of_day(2023, 12, 31) == 53 
        assert get_week_of_day(2024, 1, 1) == 1 
        assert get_week_of_day(2024, 2, 29) == 9

    def test_write_log(self):
        self.rm_log()
        self.create_log()

        rows = 100 

        for _ in range(rows):
            time.sleep(0.001)
            write_log("foo", "bar")

        content = self.read_log()
        times = [row[0] for row in content]

        assert content[0][1] == "foo"
        assert content[0][2] == "bar"
        assert len(content) == rows
        assert len(set(times)) == rows 

        self.rm_log()
        self.create_log() 
