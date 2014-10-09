
from Q3 import mergeOverlapping as mo
"""
Q3 is the from question 3 function that I created, for simplicity, I just used it for creating new function
"""
def insert(intlist,newint):
    
    granlist=intlist+','+newint
    #print granlist
    Mlist=mo(granlist)
    #print Mlist# for instant print out purpose
    return Mlist 


"""
#testing code, work !
a=insert("[1,2], (3,5), [6,7), (8,10], [12,16]", '[4,9]')
print a
#We know (3,5) is the same as [2,4]
"""
