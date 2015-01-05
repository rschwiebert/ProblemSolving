#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=67
# This program develops a calendar to solve the question of how many Sundays fell on 
# the first of month in the twentieth century
# January 1 1900 was a Monday.
# January 1 1901 was a Tuesday.

# The following two methods (according to timeit) are identical in terms of speed.

import datetime
from itertools import product


def method1():
    """Straightforward method."""
    monthmod = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month, year = (2, 0, 1901)    # this is Tuesday, January 1, 1901 (0 indexed months)
    ctr = 0
    
    while year < 2001:
        # Check to see if current day is a Sunday.
        if day % 7 == 0:
            ctr += 1
        # Now advance to the first of the next month
        day += monthmod[month]
        if month == 11:
            year += 1
        # Leap day adjustment
        if month == 1 and year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                pass
            else:
                day += 1
        month = (month + 1) % 12
        
    return ctr


def method2():
    """Leverage datetime.date"""
    months = list(range(1, 13))
    years = list(range(1901, 2001))
    yearmon = product(years, months)
    answer = len([1 for (y,m) in yearmon if datetime.date(y, m, 1).weekday == 6])
    return answer
    
if __name__ == "__main__":
    print("The answer is %d." % method1())