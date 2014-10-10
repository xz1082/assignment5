class interval:   
    def __init__(self,string='No input'):
        self.string = string
        self.firstchar=self.string[0] #either ( or [
        self.lastchar=self.string[-1] #either ) or ]
        comma=self.string.index(',')
        self.lowerbound=int(self.string[1:comma]) #lower number
        self.upperbound=int(self.string[comma+1:-1]) #upper number
        
        if self.firstchar == '[':
            self.actuallower=self.lowerbound
        else:
            self.actuallower=self.lowerbound+1
        if self.lastchar == ']':
            self.actualupper=self.upperbound
        else:
            self.actualupper=self.upperbound-1
        if self.actuallower > self.actualupper: 
            raise Exception('Invalid interval')
        
    def __repr__(self):
        return self.string

def mergeIntervals(int1,int2):
    if int1.actuallower < (int2.actualupper-1) or int2.actuallower < (int1.actualupper-1): #no overlap conditions
        raise Exception('Intervals do not overlap')
    
    if int1.actuallower<int2.actuallower:
        mergedlower=int1.firstchar + int1.lowerbound + ','
    else:
        mergedlower=int2.firstchar + int2.lowerbound + ','
    if int1.actualupper>int2.actualupper:
        mergedupper=int1.upperbound + int1.lastchar
    else:
        mergedupper=int2.upperbound + int2.lastchar
        
    mergedinterval = mergedlower + mergedupper
    return mergedinterval

def mergeOverlapping(intlist):
    intlist.sort(key=lambda x: x.lower)
    i=0
    mergedlist=[]
    for i in range(0,(len(intlist)-1)):
        j=i+1
        try:
            intlist[i] = mergeIntervals(intlist[i],intlist[j])
        except:
            mergedlist.append(intlist[i])
    return mergedlist

def insert(intlist, newint):
    intlist.append(newint)
    newlist=mergeOverlapping(intlist)
    newlist.sort(key=lambda x: x.lower)
    return newlist

def main():
    string=raw_input('List of Intervals?').split(', ')
    newlist=[interval(x) for x in string]
    while True:
        addintervals=raw_input('Intervals?')
        if addintervals=='quit':
            break
        else:
            try:
                newlist = insert(newlist,interval(addintervals))
                print newlist
            except:
                print 'Invalid Interval'
                
if __name__=='__main__':
    main()