#Q1
class interval():
    def __init__(self, string):
        self.string = string
        self.lbd = string[0]
        self.ubd = string[-1]
        self.index = string.find(',')
        self.value1 = int(string[1:self.index])
        self.value2 = int(string[self.index+1:-1])
        if self.lbd == '[' and self.ubd == ']' and self.value1 <=self.value2:
            self.lower = self.value1
            self.upper = self.value2
        elif self.lbd == '[' and self.ubd == ')' and self.value1 <= self.value2-1:
            self.lower = self.value1
            self.upper = self.value2-1
        elif self.lbd == '(' and self.ubd == ']' and self.value1+1 <= self.value2:
            self.lower = self.value1+1
            self.upper = self.value2
        elif self.lbd == '(' and self.ubd == ')' and self.value1+1 <= self.value2-1:
            self.lower = self.value1+1
            self.upper = self.value2-1
        else:
            raise Exception("invalid value")
        
    def __repr__(self):
        return self.string

#Q2
def mergeIntervals(int1, int2):
    merge_interval = ""
    if int1.upper < (int2.lower -1) or int2.upper < (int1.lower-1):
        raise Exception("The intervals do not overlap! ")
        
    if int1.lower < int2.lower or (int1.lower == int2.lower and int1.value1 <= int2.value1):
        merge_interval = merge_interval + int1.lbd + str(int1.lower) + ","
    else:
        merge_interval = merge_interval + int2.lbd +str(int2.value1) + ","
        
    if int1.upper < int2.upper or (int1.upper == int2.upper and int1.value2 <= int2.value2):
        merge_interval = merge_interval + str(int2.value2) + int2.ubd
    else:
        merge_interval = merge_interval + str(int1.value2) + int1.ubd
        
    merged_interval = interval(merge_interval)
    return merged_interval

#Q3
def mergeOverlapping(intlist):
    intlist = sorted(intlist, key=lambda int:(int.lower))
    merged_list = []
    while len(intlist)>0:
        try:
            intlist[0] = mergeIntervals(intlist[0],intlist[1])
            del intlist[1]
        except:
            merged_list.append(intlist[0])
            del intlist[0]
    return merged_list     

#Q4
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

#Q5
def main():
    input_string = raw_input("List of intervals? ")
    input_list = input_string.split(', ')
    merged_list = []
    for item in input_list:
        merged_list.append(interval(item))
    merged_list = mergeOverlapping(merged_list)
    while True:
        add_string = raw_input("Interval? ")
        if add_string != 'quit':
            try:
                merged_list.append(interval(add_string))
                print "...result of inserting into list..."
                print mergeOverlapping(merged_list)
            except:
                print "Invalid interval"
        else:
            break

if __name__ == '__main__':
    main()
