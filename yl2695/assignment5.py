class interval():
    def __init__(self, string):
        self.string = string
        self.low = string[0]
        self.upper = string[-1]
        for letter in string:
            if letter == ',':
                index = string.index(letter)
                self.lower_bound_origin = int(string[1:index])
                self.upper_bound_origin = int(string[index+1:-1])
        if self.low == '(':
            self.lower_bound = self.lower_bound_origin + 1
        else:
            self.lower_bound = self.lower_bound_origin
        if self.upper == ')':
            self.upper_bound = self.upper_bound_origin - 1
        else:
            self.upper_bound = self.upper_bound_origin
        if self.lower_bound > self.upper_bound:
            raise Exception("invalid value")   
    
    def __repr__(self):
        return self.string

def mergeIntervals(int1, int2):
    target_string = ''
    if int1.upper_bound < (int2.lower_bound - 1) or int2.upper_bound < (int1.lower_bound - 1):
        raise Exception("Can't merge")
    if int1.lower_bound < int2.lower_bound:
        target_string = target_string + int1.low + str(int1.lower_bound_origin) + ','
    elif int1.lower_bound == int2.lower_bound:
        if int1.lower_bound_origin <= int2.lower_bound_origin:
            target_string = target_string + int1.low + str(int1.lower_bound_origin) + ','
        else:
            target_string = target_string + int2.low + str(int2.lower_bound_origin) + ','
    else:
        target_string = target_string + int2.low + str(int2.lower_bound_origin) + ','
    if int1.upper_bound < int2.upper_bound:
        target_string = target_string + str(int2.upper_bound_origin) + int2.upper
    elif int1.upper_bound == int2.upper_bound:
        if int1.upper_bound_origin >= int2.upper_bound_origin:
            target_string = target_string + str(int1.upper_bound_origin) + int1.upper
        else:
            target_string = target_string + str(int2.upper_bound_origin) + int2.upper
    else:
        target_string = target_string + str(int1.upper_bound_origin) + int1.upper
    merged = interval(target_string)
    return merged


def mergeOverlapping(intlist):
    def getkey(x):
        return x.lower_bound
    intlist = sorted(intlist, key=getkey)
    target_list = []
    i = 0
    while i < len(intlist):
        for j in range(i+1, i+2):
            try:
                intlist.insert(i, mergeIntervals(intlist[i], intlist[j]))
                intlist.remove(intlist[i+1])
                intlist.remove(intlist[i+1])
                i -= 1
                break
            except:
                target_list.append(intlist[i])
                pass
        i += 1
    return target_list


def insert(intlist, newint):
    intlist.append(newint)  
    
    def getkey(x):
        return x.lower_bound
    intlist = sorted(intlist, key=getkey)
    return mergeOverlapping(intlist)


def main():
    start_string = raw_input("List of intervals? ")
    start_list = start_string.split(', ')
    interval_list = []
    for item in start_list:
        interval_list.append(interval(item))
    interval_list = mergeOverlapping(interval_list)
    while True: 
        input_string = raw_input("Interval? ")
        if input_string != 'quit':
            try:
                insert(interval_list, interval(input_string))
                print '... result of inserting into list...'
                print '... the list now is', mergeOverlapping(interval_list), '...'
            except:
                print 'Invalid interval'
        else:
            break

if __name__ == '__main__':
     main()
