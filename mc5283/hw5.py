class interval:
    def __init__(self, interval):
        self.lbound, self.ubound = interval.strip(' ()[]').split(',')
        self.lbound = int (self.lbound)
        self.ubound = int (self.ubound)

        self.a = interval.strip()[0]
        self.b = interval.strip()[-1]

        self.lrange = self.lbound + int(self.a == '(')
        self.urange = self.ubound - int(self.b == ')')

#exceptions       
        if self.a == "[" and self.b == "]":
            if self.lbound > self.ubound:
                raise Exception ('Interval invalid')
        elif (self.a == "[" and self.b == ")") or (self.a == "(" and self.b == "]"):
            if self.lbound >= self.ubound:
                raise Exception('Interval invalid')
        elif self.a == '(' and self.b == ')':
            if self.lbound >= self.ubound - 1:
                raise Exception ('Interval invalid')
        else:
            raise Exception ('Interval invalid')

#print interval
    def __repr__(self):
        return int(self.a == '[') * '[' + int(self.a == '(') * '(' + str(self.lbound) + ',' + str(self.ubound) + int(self.b == ')') * ')' + int(self.b == ']') * ']'

def intOverlap(int1, int2):
    intlist = [int1, int2]

    sorted_list = sorted(intlist, key = lambda i: (i.lbound, i.lrange, i.urange, i.ubound))
    merge1 = sorted_list[0].urange
    merge2 = sorted_list[1].lrange
    
    if merge1 + 1 >= merge2:
        return True

def mergeIntervals(int1, int2):
    if not intOverlap(int1, int2):
        raise Exception('Merge failed')

    L = int1.a
    lowerRange = int1.lrange
    lowerBound = int1.lbound
    if lowerRange > int2.lrange or lowerBound > int2.lbound:
        lowerRange = int2.lrange
        lowerBound = int2.lbound
        L = int2.a

    R = int2.b
    upperRange = int2.urange
    upperBound = int2.ubound
    if upperBound < int1.ubound or upperRange < int1.urange:
        upperBound = int1.ubound
        upperRange = int1.urange
        R = int1.b
    return interval(L + str(lowerBound) + ',' + str(upperBound) + R)

def mergeOverlapping(intlist):
    intlist = sorted(intlist, key = lambda i: (i.lbound, i.lrange, i.urange, i.ubound))
    temp = [intlist[0]]
    merging = intlist[0]
    
    for i in range(1, len(intlist)):
        if intOverlap(merging, intlist[i]):
            merging = mergeIntervals(merging,intlist[i])
            temp[-1] = merging
        else:
            merging = intlist[i]
            temp.append(merging) 
    return temp

def insert(intlist, newint):
    intlist = sorted(intlist, key = lambda i: (i.lbound, i.lrange, i.urange, i.ubound))
    for i in range (0, len(intlist)-1):
        if intOverlap(intlist[i],intlist[i+1]):
            raise Exception('The list of intervals are overlapping')
        intlist.append(newint)
    return mergeOverlapping(intlist)

def main():
    string = raw_input('List of intervals?').split(', ')
    stringlist = []
    for i in range(len(string)):
        stringlist.append(interval(string[i]))

    while True:
        intnew = raw_input('Interval?')
        if intnew == 'quit':
            break
        else:
            try: 
                intnew = interval(intnew)
            except:
                print 'Invalid interval'
                continue
            stringlist = insert(stringlist,intnew)
        print 'The merge interval list is', stringlist
    
if __name__ == "__main__":
    main()
