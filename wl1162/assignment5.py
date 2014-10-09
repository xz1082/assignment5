# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 18:16:23 2014

@author: Wenxi
"""
import ast

class interval:
    def __init__(self, string):
        list1 = ast.literal_eval(string)
        self.lower_bound = list1[0]
        self.upper_bound = list1[-1]
        if string[0] == '[' and string[-1] == ']':
            self.actual_interval = range(self.lower_bound, self.upper_bound + 1)
        elif string[0] == '(' and string[-1] == ']':
            self.actual_interval = range(self.lower_bound + 1, self.upper_bound + 1)
        elif string[0] == '[' and string[-1] == ')':
            self.actual_interval = range(self.lower_bound, self.upper_bound)
        elif string[0] == '(' and string[-1] == ')':
            self.actual_interval = range(self.lower_bound + 1, self.upper_bound)
            
    def __repr__(self):
        str = '%s' %(self.actual_interval)
        return str
        
def mergeIntervals(int1, int2):
    range1 = int1.actual_interval
    range2 = int2.actual_interval
    range3 = [i for i in range2 if i not in range1]
    
    if len(range3) == len(range2):
        raise Exception('No Overlapping between Two Intervals')
    else:
        range4 = range1 + range3
        range4.sort()
    return range4

def sort_interval(int1, int2):
    if int1.lower_bound < int2.lower_bound:
        return -1
    elif int1.lower_bound > int2.lower_bound:
        return 1
    return 0
    
def mergeOverlapping(intlist):
    interval_list = intlist[:]
    interval_list.sort(sort_interval)    
    empty_list = []
    result = []    
    while len(interval_list) > 0:
        initial = interval_list[0]
        for i in interval_list:
            try:
                initial = mergeIntervals(initial, i)
            except:
                empty_list.append(i)
    result.append(initial)
    interval_list = empty_list[:]
    empty_list = []
    return result
        
def insert(intlist, newint):
    interval_list = intlist[:]
    interval_list.append(newint)
    out = mergeOverlapping(interval_list)
    out.sort(sort_interval)
    return out
    
def ConsoleProgram():
    input_interval = raw_input('List of Intervals?').split(',')
    interval_list = [interval(i) for i in input_interval]
    while True:    
        more_intervals = raw_input('Intervals?')
        if more_intervals == 'quit':
            break
        try:
            more = interval(more_intervals)
        except:
            more.lower_bound > more.upper_bound
            print 'invalid interval'
            continue
        interval_list = insert(interval_list, more)
        print interval_list
        
    

        
        
        


