import re
class interval:
    def __init__(self, interval_string = ''):
        self.string = interval_string
        if interval_string: 
            self.lower, self.upper = map(int, interval_string.strip('[] ()').split(','))
            if (interval_string[0] == '[') and (interval_string[-1] == ']') and (self.lower <= self.upper):
                self.lower_type = '['
                self.upper_type = ']' 
                self.range = range(self.lower, self.upper + 1)
            elif (interval_string[0] == '[') and (interval_string[-1] == ')') and (self.lower < self.upper):
                self.lower_type = '['
                self.upper_type = ')' 
                self.range = range(self.lower, self.upper)
            elif (interval_string[0] == '(') and (interval_string[-1] == ']') and (self.lower < self.upper):
                self.lower_type = '('
                self.upper_type = ']' 
                self.range = range(self.lower + 1, self.upper + 1)
            elif (interval_string[0] == '(') and (interval_string[-1] == ')') and (self.lower < self.upper - 1):
                self.lower_type = '('
                self.upper_type = ')' 
                self.range = range(self.lower + 1, self.upper)
            else:
                raise Exception('Invalid interval.')
        
    def __repr__(self):
        return self.string


def mergeIntervals(int1, int2):
    range1 = int1.range
    range2 = int2.range
    #assign the lower_types and upper_types for interval1 and interval2
    lt1 = int1.lower_type
    lt2 = int2.lower_type
    ut1 = int1.upper_type
    ut2 = int2.upper_type
    l1 = int1.lower
    u1 = int1.upper
    l2 = int2.lower
    u2 = int2.upper
    if (range1[-1] + 1 < range2[0]) or (range2[-1] + 1 < range1[0]):
        raise Exception ('These two intervals are not overlapping.')
    elif range1[-1] +1 == range2[0]: 
        merged = interval(lt1+ str(l1) + ',' + str(u2) + ut2)
    elif range2[-1] + 1== range1[0]:
        merged = interval(lt2+ str(l2) + ',' + str(u1) + ut1)
    else: 
        if  (range1[0] >= range2[0]) and (range1[-1] <= range2[-1]):
            merged_interval = range2
            merged = int2
        elif (range1[0] >= range2[0]) and (range1[-1] >= range2[-1]):
            merged_interval = range(range2[0], range1[-1])
            merged = interval(lt2+ str(l2)+','+ str(u1) + ut1)
        elif (range1[0] <= range2[0]) and (range1[-1] >= range2[-1]):
            merged_interval = range1
            merged = int1
        elif (range1[0] <= range2[0]) and (range1[-1] <= range2[-1]):
            merged_interval = range(range1[0], range2[-1])
            merged = interval(lt1+ str(l1) + ', ' + str(u2) + ut2)        
    return merged

def mergeOverlapping(intlist):
    n = len(intlist)
    # sort the intervals 
    intlist.sort(key = lambda x: x.lower)
    
    for i in xrange(0, n - 1): 
        j = i + 1
        try:
            intlist[j] = mergeIntervals(intlist[i], intlist[j])
            intlist[i] = ''
        except:
            pass      
    return [intlist[i] for i in range(len(intlist)) if intlist[i] != '']
        
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)



def main():
    #global variable intlist
    intlist = []
    input_interval = raw_input('List of intervals?')
    try:
        intlist = [interval(x) for x in re.split('(?<=[\]\)])\s*,\s*', input_interval.strip())]
    except:
        print 'Invalid interval'           

    while True:
        new_input = raw_input('Interval?')
        if new_input == 'quit':
            break
        else:
            try:
                new_input = interval(new_input.strip())
                intlist = insert(intlist,new_input)
            except:
                print 'Invalid interval!'
                continue
        print intlist     
          

            
if __name__ == '__main__':
    main()






