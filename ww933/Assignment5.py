__author__ = 'chianti'

class interval:
    def __init__(self, int0):
        self.int0 = int0
        self.a=self.int0.strip().split(',')
        self.sym1=self.a[0][0]
        self.sym2=self.a[1][-1]
        if self.sym1 == '[':
                self.low = int(self.a[0][1:])
        if self.sym1 == '(':
                self.low = int(self.a[0][1:]) + 1
        if self.sym2 == ']':
                self.high = int(self.a[1][:-1])
        if self.sym2 == ')':
                self.high = int(self.a[1][:-1]) - 1
        if int(self.low) > int(self.high):
            self.nature = 0
        if int(self.low) <= int(self.high):
            self.nature = 1
    def __repr__(self):
            if int(self.low) > int(self.high):
                raise Exception('ERROR! The lower bound is higher than the upper bound')
            else:
                return '{} represents the number from {} through {} \n'.format(self.int0, self.low, self.high)


def mergeInterval(int1, int2):
    if (interval(int1).nature) * (interval(int2).nature) == 0:
        raise Exception('ERROR! NOT INTERVALS!')
    if interval(int1).low <= interval(int2).low:
        a1 = interval(int1).low
        a2 = interval(int2).low
        b1 = interval(int1).high
        b2 = interval(int2).high
    else:
        a1 = interval(int2).low
        a2 = interval(int1).low
        b1 = interval(int2).high
        b2 = interval(int1).high
    if a2 == b1 + 1:
        return '[{},{}]'.format(a1, b2)
    if b1 < a2:
        raise Exception('ERROR! the intervals do not overlap!')
    else :
        return '[{},{}]'.format(a1, max(b1,b2))


def mergeOverlapping(intlist):
    num_int = len(intlist)
    intlist.sort(key = lambda t: interval(t).low)
    for i in xrange(0, num_int-1):
        j = i+1
        try:
            intlist[j]=mergeInterval(intlist[i], intlist[j])
            intlist[i] = ''
        except:
            pass
    return [intlist[i] for i in range(len(intlist)) if intlist[i] != '']


def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

def main():
    input_int = raw_input('List of intervals?(put a space after each comma)').split(', ')
    intlist = []
    for i in range(len(input_int)):
        intlist.append(str(input_int[i]))
    while True:
        new_input = raw_input('Intervals?')
        if new_input == 'quit':
            break
        try:
            intlist = insert(mergeOverlapping(intlist), new_input)
            for each_int in intlist[:-1]:
                print each_int + ',',
            print intlist[-1]
        except:
            print 'Invalid interval'





main()