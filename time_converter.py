# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 03:26:05 2015

@author: J
"""

# import datetime
#from itertools import imap

def convert_time(course_time):
    """Example format: '08:00AM-09:15AM' """
    t1, t2 = course_time.split('-')
    return map(_convert_time, (t1, t2))


def _convert_time(time):
    if 'AM' in time:
        time = time.replace('AM', '')
        time = map(int, time.split(':'))
        t1, t2 = time
        if t1 == 12:
            t1, t2 = t1 + 12, t2
        time = float(t1) + float(t2) / 60.0
        return time

    if 'PM' in time:
        time = time.replace('PM', '')
        time = map(int, time.split(':'))
        t1, t2 = time
        if t1 != 12:
            t1, t2 = t1 + 12, t2
        time = float(t1) + float(t2) / 60.0
        return time


def main():
    test()


def test():
    print convert_time('08:00AM-12:15PM')

#    print convert_time('1:00PM-3:00PM')



if __name__ == '__main__':
    main()