import string
class interval:
    def __init__(self, string_raw):
        string2 = string.replace(string_raw,' ','')
        middle_place=string2.find(',')
        if (string2[0] == '[') & (string2[len(string2)-1] == ']') & (int(string2[1:middle_place]) <= int(string2[middle_place+1:len(string2)-1])):
            self.lower_bound = int(string2[1:middle_place])
            self.lower_show = int(string2[1:middle_place])
            self.lower_bound_type = '['
            self.upper_bound = int(string2[middle_place+1:len(string2)-1])
            self.upper_show = int(string2[middle_place+1:len(string2)-1])
            self.upper_bound_type = ']'
        elif (string2[0] == '(') & (string2[len(string2)-1] == ')') & (int(string2[1:middle_place])+1 <= int(string2[middle_place+1:len(string2)-1])-1):
            self.lower_bound = int(string2[1:middle_place])+1
            self.lower_show = int(string2[1:middle_place])
            self.lower_bound_type = '('
            self.upper_bound = int(string2[middle_place+1:len(string2)-1])-1
            self.upper_show = int(string2[middle_place+1:len(string2)-1])
            self.upper_bound_type = ')'
        elif (string2[0] == '(') & (string2[len(string2)-1] == ']') & (int(string2[1:middle_place])+1 <= int(string2[middle_place+1:len(string2)-1])):
            self.lower_bound = int(string2[1:middle_place])+1
            self.lower_show = int(string2[1:middle_place])
            self.lower_bound_type = '('
            self.upper_bound = int(string2[middle_place+1:len(string2)-1])
            self.upper_show = int(string2[middle_place+1:len(string2)-1])
            self.upper_bound_type = ']'
        elif (string2[0] == '[') & (string2[len(string2)-1] == ')') & (int(string2[1:middle_place]) <= int(string2[middle_place+1:len(string2)-1])-1):
            self.lower_bound = int(string2[1:middle_place])
            self.lower_show = int(string2[1:middle_place])
            self.lower_bound_type = '['
            self.upper_bound = int(string2[middle_place+1:len(string2)-1])-1
            self.upper_show = int(string2[middle_place+1:len(string2)-1])
            self.upper_bound_type = ')'
        else:
            raise Exception('Input Error')
    def __repr__(self):
        return self.lower_bound_type+'%d,%d' %(self.lower_show,self.upper_show)+self.upper_bound_type



def mergeIntervals(int1, int2):
    lower_bound_1 = int1.lower_bound
    lower_bound_2 = int2.lower_bound
    upper_bound_1 = int1.upper_bound
    upper_bound_2 = int2.upper_bound
    if (upper_bound_1+1 < lower_bound_2) or (upper_bound_2+1 < lower_bound_1):
        raise Exception('No overlapping')
    if (upper_bound_1 == max(upper_bound_1,upper_bound_2)):
        upper_bound = upper_bound_1
        upper_bound_show = int1.upper_show
        upper_bound_type = int1.upper_bound_type
    if (upper_bound_2 == max(upper_bound_1,upper_bound_2)):
        upper_bound = upper_bound_2
        upper_bound_show = int2.upper_show
        upper_bound_type = int2.upper_bound_type
    if (lower_bound_1 == min(lower_bound_1,lower_bound_2)):
        lower_bound = lower_bound_1
        lower_bound_show = int1.lower_show
        lower_bound_type = int1.lower_bound_type
    if (lower_bound_2 == min(lower_bound_1,lower_bound_2)):
        lower_bound = lower_bound_2
        lower_bound_show = int2.lower_show
        lower_bound_type = int2.lower_bound_type
    string = lower_bound_type + '%d,%d' %(lower_bound_show, upper_bound_show) + upper_bound_type
    return interval(string)

def interval_sort(a,b):
    if a.lower_bound > b.lower_bound:
        return 1
    if b.lower_bound > a.lower_bound:
            return -1
    return 0

def mergeOverlapping(intlist):
    A=intlist[:]
    A.sort(interval_sort)
    B=[]
    answer=[]
    while len(A)>0:
        x0=A[0]
        for x in A:
            try:
                x0=mergeIntervals(x0,x)
            except:
                B.append(x)

        answer.append(x0)
        A=B[:]
        B=[]
    return answer

def insert(intlist,newint):
    input=intlist[:]
    input.append(newint)
    string=mergeOverlapping(input)
    string.sort(interval_sort)
    return string

def input():
    input_list = raw_input('List of intervals?').split(', ')
    list = [interval(x) for x in input_list]
    while True:
        add = raw_input('Intervals?')
        if add=='quit':
            break
        try:
            add_int=interval(add)
        except:
            print 'Invalid interval'
            continue
        list = insert(list,add_int)
        print(list)
