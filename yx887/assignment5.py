import re

class Interval:
    def __init__(self, string=''):
        if string:
            self.lower, self.upper = map(int, string.strip(' ()[]').split(','))
            if string.strip()[0] == '(':
                self.lower_inclusive = False
            elif string.strip()[0] == '[':
                self.lower_inclusive = True
            if string.strip()[-1] == ')':
                self.upper_inclusive = False
            elif string.strip()[-1] == ']':
                self.upper_inclusive = True
            
            if self.lower + int(not self.lower_inclusive) + int(not self.upper_inclusive) > self.upper:
                raise Exception('Invalid interval bounds')
            
    def get_val(self):
        return range(self.lower + int(not self.lower_inclusive), self.upper + int(self.upper_inclusive))

    def __repr__(self):
        return self.lower_inclusive * '[' + (1-self.lower_inclusive) * '(' + str(self.lower) + ',' + str(self.upper) + self.upper_inclusive * ']' + (1-self.upper_inclusive) * ')'

def mergeIntervals(int1, int2):
    range1 = int1.get_val()
    range2 = int2.get_val()
    if range1[-1] < range2[0] - 1 or range1[0] > range2[-1] + 1: 
        raise Exception('Two intervals not overlapping')
    else:
        lower, lower_inclusive = (int1.lower, int1.lower_inclusive) if int1.lower - 0.5 * int1.lower_inclusive <= int2.lower - 0.5 * int2.lower_inclusive else (int2.lower, int2.lower_inclusive)
        upper, upper_inclusive = (int1.upper, int1.upper_inclusive) if int1.upper + 0.5 * int1.upper_inclusive >= int2.upper + 0.5 * int2.upper_inclusive else (int2.upper, int2.upper_inclusive)

        int_merged = Interval()
        int_merged.lower, int_merged.upper, int_merged.lower_inclusive, int_merged.upper_inclusive = lower, upper, lower_inclusive, upper_inclusive
    return int_merged
        

def mergeOverlapping(intlist):
    # first sort the list for the following operations
    intlist.sort(key = lambda x: x.lower - 0.5 * x.lower_inclusive)
    current = intlist[0]
    res = []
    for i in xrange(1, len(intlist)):
        # try merge, if cannot merge create a new one and continue
        try:
            current = mergeIntervals(current, intlist[i])
        except:
            res.append(current)
            current = intlist[i]
    
    # append the last interval
    res.append(current)
    
    return res

def insert(intlist, newint):
    intlist.sort(key = lambda x: x.lower - 0.5 * x.lower_inclusive)
    for i in xrange(len(intlist)):
        if newint.lower - 0.5 * newint.lower_inclusive <= intlist[i].lower - 0.5 * intlist[i].lower_inclusive:
            intlist.insert(i, newint)
            break
    else:
        intlist.append(newint)

    return mergeOverlapping(intlist)

def main():
    string = raw_input('List of intervals? ')
    try:
        intlist = [Interval(x) for x in re.split('(?<=[\]\)])\s*,\s*', string.strip())]
    except:
        print 'Invalid interval'
    while True:
        newint = raw_input('Interval? ')
        if newint == 'quit':
            break
        else:
            try:
                newint = Interval(newint.strip())
            except:
                print 'Invalid interval'
                continue

            intlist = insert(intlist, newint)
            print intlist

if __name__ == '__main__':
    main()
        

