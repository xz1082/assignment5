'''
Created on Oct 9, 2014

@author: ds-ga-1007
'''
#QUESTION 1
class interval:
    def __init__(self,str):
        self.str = str
        self.lower = str[0]
        self.upper = str[-1]
        i = str.index(',')
        self.l = int(str[1:i])
        self.u = int(str[i+1:-1])
        if self.lower == '[':
            self.lower_bound = self.l
        else:
            self.lower_bound = self.l+1
        if self.upper == ']':
            self.upper_bound = self.u
        else:
            self.upper_bound = self.u-1
        if self.lower_bound > self.upper_bound:
            raise Exception('Error! Invalid interval!')
    
    def range_of_int(self):
        return range(self.lower_bound,self.upper_bound+1)
    def __repr__(self):
        return self.str

#QUESTION 2
def mergeIntervals(int1,int2):
    x = int1.range_of_int()   
    y = int2.range_of_int()
    if int(x[0])>int(y[-1]) or int(y[0])>int(x[-1]):
        raise Exception('The intervals do not overlap!')
    else:
        if int1.lower_bound < int2.lower_bound:
            merge = int1.lower + str(int1.lower_bound)+','
        elif int1.lower_bound == int2.lower_bound:
            if int1.l < int2.l:
                 merge = int1.lower + str(int1.l)+','
            else:
                 merge = int2.lower + str(int2.l)+','
        else :
            merge = int2.lower + str(int2.l) + ','
        if int1.upper_bound > int2.upper_bound:
            merge = merge + str(int1.u) + int1.upper
        elif int1.upper_bound == int2.upper_bound:
            if int1.u > int2.u:
                merge = merge + str(int1.u) + int1.upper
            else:
                merge = merge + str(int2.u) + int2.upper
        else:
            merge = merge + str(int2.u) + int2.upper
    merge_int = interval(merge)
    return merge_int

#QUESTION 3
def merged(int1,int2):
    if int1.lower_bound <= int2.lower_bound:
        x = int1
        y = int2
    else:
        x = int2
        y = int1
    return (x.upper_bound >= y.lower_bound)

def mergeOverlapping(intlist):
    intlist = sorted(intlist,key = lambda i: i.lower_bound)
    temp = intlist[0]
    mergeO = []
    for i in range(1,len(intlist)):
        if merged(temp,intlist[i]):
            temp = mergeIntervals(temp,intlist[i])
        else:
           mergeO.append(temp)
           temp = intlist[i]
    mergeO.append(temp)
    return mergeO

#QUESTION 4
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

#QUESTION 5
def main():
    str = raw_input('List of intervals?')
    string = str.split(', ')
    list_of_int = []
    for i in range(len(string)):
        list_of_int.append(interval(string[i]))
        
    while True:
        insint = raw_input('Intervals?')
        if insint == 'quit':
            break
        try:
                newint = interval(insint)
                list_of_int = insert(list_of_int,newint)
                print list_of_int
        except:
                print 'Invalid Interval'
                continue

    
if __name__ == '__main__': 
    main()
