'''
Created on Oct 9, 2014

@author: ds-ga-1007
'''
class interval:
    def __init__(self, string):
        self.string=string
        self.lower=string[0]
        self.upper=string[-1]
        comma=string.find(',')
        self.lower_bound=int(string[1:comma])
        self.upper_bound=int(string[comma+1:-1])
        
        if self.lower=='[':
            self.l=self.lower_bound
        else:
            self.l=self.lower_bound+1
        if self.upper==']':
            self.u=self.upper_bound
        else:
            self.u=self.upper_bound-1
        if self.l>self.u:
            raise Exception("Error")
    def __repr__(self):
        return self.string
    
def mergeIntervals(int1, int2):
    new_string=''
    if int1.u<int2.l-1 or int2.u+1< int1.l:
        raise Exception("Cannot merge")
    else:
        if int1.l<int2.l:
            merge_lower=int1.lower
            merge_lower_bound=int1.lower_bound
        else:
            merge_lower=int2.lower
            merge_lower_bound=int2.lower_bound
        if int1.u<int2.u:
            merge_upper=int2.upper
            merge_upper_bound=int2.upper_bound
        else:
            merge_upper=int1.upper
            merge_upper_bound=int1.upper_bound
        new_string=merge_lower+str(merge_lower_bound)+','+str(merge_upper_bound)+merge_upper
        merge=interval(new_string)
        return merge

def mergeOverlapping(intlist):
    intlist.sort(key=lambda x: x.lower_bound)
    temp=intlist[0]
    li=[]
    for i in range(1,len(intlist)):
        try:
            temp=mergeIntervals(temp,intlist[i])
        except:
            li.append(temp)
            temp=intlist[i]
    li.append(temp)
    return li

def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

def main():
    start=raw_input('List of intervals?').split(', ')
    new_input=[]
    for x in start:
        new_input.append(interval(x))
    while True:
        new=raw_input('Intervals?')
        if new =='quit':
            break
        else:
            try:
                new=interval(new)
                new_input=insert(new_input,new)
                print new_input
            except:
                print 'Invalid interval'
                continue
        

if __name__ == '__main__':
    main()