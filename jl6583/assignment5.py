'''
Created on Oct 9, 2014

@author: jiayi lu(jl6583)
'''
import math as mt

class interval:
    def __init__(self,init_str = ''):
        if type(init_str) == str:
            bound_list = init_str.strip(' []()').split(',')
            self.l_bound = int(bound_list[0])
            self.u_bound = int(bound_list[-1])
            #a 0.9 shift was added to represent exclusive bounds
            if init_str.strip(' ')[0] == '(':
                self.l_bound = self.l_bound+0.9
            if init_str.strip(' ')[-1] == ')':
                self.u_bound = self.u_bound-0.9
        #receiving list input for initialization
        elif type(init_str) == list:
            self.l_bound = init_str[0]
            self.u_bound = init_str[-1]
        if self.l_bound > self.u_bound:
            raise Exception('Invalid Interval!\n')    
    
    def __repr__(self):
        l = mt.floor(float(self.l_bound))
        u = mt.ceil(float(self.u_bound))
        if self.l_bound - l != 0.0:
            l_bracket = '('
        else:
            l_bracket = '['
        if self.u_bound - u != 0.0:
            u_bracket = ')'
        else:
            u_bracket = ']'
        output_str = '%s%d,%d%s'%(l_bracket,l,u,u_bracket)
        return output_str
    
def mergeIntervals(int1,int2):
    if round(int1.l_bound) > round(int2.u_bound)+1 or round(int1.u_bound)+1 < round(int2.l_bound):
        raise Exception('Intervals not overlapping')
    else:
        new_l = min(int1.l_bound,int2.l_bound)
        new_u = max(int1.u_bound,int2.u_bound)
        merged_itvl = interval([new_l,new_u])
        return merged_itvl;
    
def mergeOverlapping(intlist = []):
    #sort the interval list by the lower bound
    intlist.sort(key = lambda x : x.l_bound)
    temp_itvl = intlist[0]
    output_list = list()
    for i in range(1,len(intlist)):
        try: 
            temp_itvl = mergeIntervals(temp_itvl,intlist[i])
        except:
            #if unable to merge create a new interval
            output_list.append(temp_itvl)
            temp_itvl = intlist[i]
    output_list.append(temp_itvl)
    return output_list

def insert(intlist,newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)
    
def main():
    input_list = raw_input('List of intervals? ').split(', ')
    itvl_list = []
    for itvl_str in input_list:
        itvl_list.append(interval(itvl_str))
    while True:
        insert_input = raw_input('Interval? ')
        if insert_input == 'quit':
            break
        #initialzing the interval with a string
        try:
            insert_itvl = interval(insert_input)
            itvl_list = insert(itvl_list,insert_itvl)
            print itvl_list
        except:
            print 'Invalid interval\n'
        
          
if __name__ == '__main__' :
    main()
        
    
    
        
        
            