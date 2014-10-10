class interval:
    def __init__(self, string):
        self.string = string
        self.lb_type = string[0]
        self.ub_tpye = string[-1]
        self.lb, self.ub = map(int, string.strip('()[]').split(','))
        self.lb_new = []
        self.ub_new = []
        
        if self.lb_type == '(':
            self.lb_new = self.lb + 1
        if self.ub_tpye == ')':
            self.ub_new = self.ub - 1
        if self.lb_new > self.ub_new:
            raise Exception('Invalid interval')
        
    def __repr__(self):
        return self.string


def mergeIntervals(int1, int2):
    
    if int1.ub_new < (int2.lb_new - 1) or int2.ub_new < (int1.lb_new - 1):
        raise Exception("Intervals do not overlap, can not merge!")    
    new_interval_lb = int(int1.lb < int2.lb)*int1.lb + int(int2.lb < int1.lb)*int2.lb
    new_interval_ub = int(int1.ub > int2.ub)*int1.ub + int(int2.ub < int1.ub)*int2.ub  
    if int1.lb == int2.lb:
        new_interval_lb_type = int(int1.lb_new < int2.lb_new)*int1.lb_type + int(int2.lb_new < int1.lb_new)*int2.lb_type
    else:
        new_interval_lb_type = int(int1.lb < int2.lb)*int1.lb_type + int(int2.lb < int1.lb)*int2.lb_type
    if int1.ub_new == int2.ub_new:
        new_interval_ub_type = int(int1.ub_new > int2.ub_new)*int1.ub_type + int(int2.ub_new > int1.ub_new)*int2.ub_type
    else:
        new_interval_ub_type = int(int1.ub > int2.ub)*int1.ub_type + int(int2.ub > int1.ub)*int2.ub_type
    new_interval = new_interval_lb_type + str(new_interval_lb) + ',' + str(new_interval_ub) + new_interval_ub_type
    return interval(new_interval)

def mergeOverlapping(intlist):
    intlist = sorted(intlist, key = lambda x: x.lb )
    tmp1 = [intlist[0]]
    tmp2 = intlist[0]
    for i in range(len(intlist)):
        try:
            tmp2 = mergeIntervals(tmp2, intlist[i])
        except:
            tmp1.append(tmp2)
            tmp2 = intlist[i]
    tmp1.append(tmp2)
    
    return tmp1


def insert(intlist, newint):
    intlist.append(newint)
    intlist = sorted(intlist, key = lambda x: x.lb)
    
    return mergeOverlapping(intlist)

def main():
    string = raw_input('List of intervals?').split(',')
    str_list = []
    for i in range(len(string)):
        str_list.append(interval(string[i]))
        
    while True:
        str_new = raw_input('Intervals?')
        if str_new != 'quit':
            try:
                insert(str_list, interval(string))
            except:
                print 'Invalid interval!'
        else:
            break
        
if __name__ == '__main__':
    main()

        
    
    























