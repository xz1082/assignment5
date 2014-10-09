
###############################################################################
# class that represents an integer interval
###############################################################################

class interval:
# interval stored as upper and lower bounds + bound type

    boundDef = {'(': 'exclusive', ')': 'exclusive', '[': 'inclusive', ']': 'inclusive'}
    
    # Constructor
    # How do you do for empty? interval()

    def __init__(self,inStr):
        
        self.inStr = inStr  
        
        if len(inStr)>0:
            self.setRange()
        
    # Methods
    
    def setRange(self):
        
        try:        
        
            intervalRange = [int(x) for x in self.inStr[1:-1].split(',')]
            
            # Upper and lower bounds of set
            self.upper = intervalRange[1]
            self.lower = intervalRange[0]
                
            self.upperType = self.inStr[-1]
            self.lowerType = self.inStr[0]
                    
            # Max and min of set elements
            self.max = self.upper if interval.boundDef[self.upperType] == 'inclusive' else self.upper - 1 
            self.min = self.lower if interval.boundDef[self.lowerType] == 'inclusive' else self.lower + 1
            
            if self.max < self.min: raise Exception('Invalid Interval 1')
        
        except:
            
            raise Exception('Invalid Interval 2')            
            
    def setStr(self):
        
        self.inStr = self.lowerType + str(self.lower) + ',' + str(self.upper) + self.upperType
    
    def __repr__(self):
        
        return self.inStr

###############################################################################
# Functions for multiple intervals                                         
###############################################################################

# Merge two intervals 
def mergeIntervals(interval1,interval2):
    
    interval1.setRange()
    interval2.setRange()
    
    if interval1.min < interval2.min:
        lowerInterval = interval1
        upperInterval = interval2 
    else:
        lowerInterval = interval2
        upperInterval = interval1

    out = interval('')
        
    # Merge 
    if lowerInterval.max < upperInterval.min - 1:
        
        raise Exception('Disjoint Sets')
        
    elif lowerInterval.max <= upperInterval.max:
        
        out.lowerType = lowerInterval.lowerType 
        out.lower = lowerInterval.lower
        out.upper = upperInterval.upper
        out.upperType = upperInterval.upperType 

    else:
        
        out.lowerType = lowerInterval.lowerType 
        out.lower = lowerInterval.lower
        out.upper = lowerInterval.upper
        out.upperType = lowerInterval.upperType 
        
    out.setStr()
    
    return out

# Merge a list of intervals
def mergeOverlapping(intervalList):
    
    map(lambda x: x.setRange(),intervalList)
    
    # Sort intervals on lower bound
    intervalList.sort(key = lambda x: x.lower)
    
    outList = []
    merged = intervalList[0] 
    
    for idxList in range(len(intervalList)):
    
        try:
            merged = mergeIntervals(merged,intervalList[idxList])
        except:
            outList.append(merged)
            merged = intervalList[idxList]
            
    outList.append(merged)
     
    return outList           

# Insert interval into list
def insert(intervalList, newInterval):
           
    intervalList.append(newInterval)
       
    outList = mergeOverlapping(intervalList)
    outList.sort(key = lambda x: x.lower)
    
    return outList
    
###############################################################################
# Prompts users for intervals                                    
###############################################################################
    
def getUserList() :

    inList = raw_input('List of intervals? ')
    
    isCorrect = False
    
    # Check initial input
    while isCorrect == False:
    
        try:
        
            splitInList = inList.split(', ')
            outList = [interval(x) for x in splitInList]
            
            isCorrect = True
            
        except:
            
            isCorrect = False
            print 'Please make your input of the form [a,b], [c,d)], ,,, , [z,y]'
            inList = raw_input('List of intervals? ')
            
    
    inputInterval = raw_input('Interval? [TYPE quit TO EXIT] ')
    
    # Check intervals
    while inputInterval != 'quit':     
        
        try:
            if inputInterval == '': raise Exception
        
            outList = insert(outList,interval(inputInterval))
            print outList
        
        except:
        
            print 'Invalid Interval'
        
        inputInterval = raw_input('Interval? [TYPE quit TO EXIT] ')



    

