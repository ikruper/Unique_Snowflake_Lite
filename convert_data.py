# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 03:49:47 2015

@author: J
@contributor: Ian
"""

from time_converter import convert_time


"""example input"""
example_input = [
                     '20001',
                     'ANT210.101',
                     'PhysicalAnthropol',
                     '3.00',
                     'LEC',
                     'MWF',
                     '10:00AM-10:50AM',
                     'LS305',
                     'Becker',
                     'S',
                     '20',
                     '8',
                     '12',
                     '01/21/15-05/14/15'
 ]



def convert_data(data_in):
    times = convert_time(data_in[6])
    days = data_in[5]
    return times,days

def convert_days(days, times):
    """example dates: "MWF", "TR", "R", etc"""
    conversions = {
                    'M' : 0,
                    'T' : 1,
                    'W' : 2,
                    'R' : 3,
                    'F' : 4
    }
    new_day = []
    for i in range(5):
        new_day.append([0,0])
    for day in days:
        new_day[conversions[day]] = times
        
    return new_day
    
    
    
def main():
#    print len(example_input)
    """time is inp[6]"""
    t = convert_time(example_input[6])
    d = convert_days(example_input[5], t)
    for _d in d:
        pass
        print _d
    
if __name__ == '__main__':
    main()