# -*- coding: utf-8 -*-
"""
Assignment 5 
"""

import re

class interval:
    def __init__(self, new_string = ''):
        self.string = new_string
        if new_string:
            self.lower, self.upper = map(int, new_string.strip(' ()[]').split(','))
            if (new_string[0] == '[') & (new_string[-1] == ']') & (self.lower <= self.upper):
                self.lower_bound = '['
                self.upper_bound = ']'
                self.range = range(self.lower, self.upper + 1)
            elif (new_string[0] == '(') & (new_string[-1] == ')') & (self.lower < self.upper-1):
                self.lower_bound = '('
                self.upper_bound = ')'
                self.range = range(self.lower + 1, self.upper)
            elif (new_string[0] == '(') & (new_string[-1] == ']') & (self.lower < self.upper):
                self.lower_bound = '('
                self.upper_bound = ']'
                self.range = range(self.lower + 1, self.upper + 1)
            elif (new_string[0] == '[') & (new_string[-1] == ')') & (self.lower < self.upper):
                self.lower_bound = '['
                self.upper_bound = ')'
                self.range = range(self.lower, self.upper)
            else:
                raise Exception('Input Error')
    
    def get_val (self):
        return self.range
    
    def __repr__(self):
        return '{} represents the number from {} through {} \n'.format(self.string, self.range[0], self.range[-1])


def mergeIntervals(int1, int2):
    range1 = int1.get_val()
    range2 = int2.get_val()
    if (range1[-1] < range2[0] - 1) or (range2[-1] + 1 < range1[0]):
        raise Exception('Intervals do not overlap')
    else:
        lower = min(int1.lower, int2.lower)
        upper = max(int1.upper, int2.upper)
        if lower == int1.lower:
            lower_bound = int1.lower_bound
        if lower == int2.lower:
            lower_bound = int2.lower_bound  
        if upper == int1.upper:
            upper_bound = int1.upper_bound
        if upper == int2.upper:
            upper_bound = int2.upper_bound  
        
        string = lower_bound + '%d,%d' %(lower, upper) + upper_bound
        mergeInterval = interval(string)
        return mergeInterval


def mergeOverlapping(intlist):
    if not intlist:
        raise Exception('Empty list')
    else:
        intlist.sort(key = lambda x: x.lower)
        current = intlist[0]        
        merged_list = []
        for x in range(1,len(intlist)):
            try:
                current = mergeIntervals(current, intlist[x])
            except:
                merged_list.append(current)
                current = intlist[x]
        
        merged_list.append(current)
        return merged_list


def insert(intlist, newint):
    intlist.append(newint)    
    newlist = mergeOverlapping(intlist)
    newlist.sort(key = lambda x: x.lower)
    return newlist 


def main():
    string = raw_input('List of intervals?')
    new_list = [interval(x) for x in re.split('(?<=[\]\)])\s*,\s*', string.strip())]
    while string:
        newint = raw_input('Interval?')
        if newint == 'quit':
            break
        try:
            newint = interval(newint.strip())
        except:
            print 'Invalid interval'
            continue
        new_list = insert(new_list, newint)
        print new_list
        
if __name__ == '__main__':
    main()
