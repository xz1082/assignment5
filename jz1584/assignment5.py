from Q1 import *
from Q2 import *
from Q3 import *
from Q4 import *



#Q1 testing
print "Q1 testing:"
a=interval("[2,2]")
b=interval('[-2,2)')
c=interval("(2,400)")
d=interval("(-3,-2]")
print a, b, c, d
#f=interval("(-2,-1)") #error should be expected
#print f

#Q2 testing
print "Q2 testing:"
q2="[1,5)" 
q21="(-2,7]"
#note [-1,7] is the same as (-2,7]
mergeIntervals(q2,q21)

#Q3 testing
print "Q3 testing:"
#"Note:Merged all intervals into equivalent inclusive-interval form:"
intlist='(2,5],[-2,7),(7,10],[8,18]'
Q3=mergeOverlapping(intlist)
print Q3

#Q4 testing
print "Q4 testing:"
Q4=insert("[1,2], (3,5), [6,7), (8,10], [12,16]", '[4,9]')
print Q4 #We know (3,5) is the same as [2,4]

#Q5 is in a seperate files called assignment5_Q5.py

