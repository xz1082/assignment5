from Q1 import interval
from Q3 import mergeOverlapping as mo

"""
This program will insert and merge the inputed interval, and print out the list of merged interval
"""
print "If you want to quit the program, please enter: quit" 
temp=""
a=1
while a>0:
    initial=raw_input('please enter an interval :')
    if initial == "quit":
        break
    try:
        
        check=interval(initial)
        temp=temp+","+initial 
        final=mo(temp)
        print final
        
    except:
        print" Invalid interval"
        
#Note: interval is the class I imported from question 1 codes. 
