'''

@author: jiminzi
'''

import re
#q1
class Interval():
    def __init__(self,string):
        self.string = string
        self.split_self = re.split('[,:]',string)
        self.left_string = self.split_self[0]
        self.right_string = self.split_self[1]
        self.lowbound = int(self.left_string[1:])
        self.upbound = int(self.right_string[0:-1])
        self.left_bound_mark=str(self.left_string[0])
        self.right_bound_mark=str(self.right_string[-1])
        #self.lowerbounds=int(self.lowbound+1)
        #self.upperbounds=int(self.upbound-1)
        while self.left_bound_mark=='(' and self.right_bound_mark==')' and int(self.upbound - self.lowbound) < 2 :
            raise Exception("invalid input interval")
        if int(self.lowbound) > int(self.upbound) :
            raise Exception("invalid input interval")
        elif self.left_bound_mark == '(':
            self.lowerbounds=int(self.lowbound)+1
        else:
            self.lowerbounds = self.lowbound
        if self.right_bound_mark == ')':
            self.upperbounds=int(self.upbound)-1
        else:
            self.upperbounds=self.upbound
    def __repr__(self):
        return self.string#'{} represents the number from {} through {} \n'.format(self.string, self.lowerbounds, self.upperbounds)

    
    
def mergeIntervals(int1,int2):
    '''
    
    '''
    #int1_low=int1.lowbound
    #int1_lower=int1.lowerbounds
    #int1_up=int1.upbound
    #int1_upper=int1.upperbounds 
    #int2_lower=int2.lowerbounds
    #int2_low=int2.lowbound
    #int2_up=int2.upbound
    #int2_upper=int2.upperbounds  
    #int1_leftmark=
    #int1_rightmark=int1.right_bound_mark
    #int2_leftmark=int2.left_bound_mark
    #int2_rightmark=int2.right_bound_mark
    while (int1.upperbounds<(int2.lowerbounds-1)) or int2.upperbounds<(int1.lowerbounds-1):
        raise Exception('invalid (no overlap)') 
         # min(int1.upbound,int2.upbound) < max(int1.lowbound,int2.lowbound):
          # raise Exception('invalid (no overlap)')  

    #if int1.lowerbounds == int2.lowerbounds:
     #   if int1.lowbound <= int2.lowbound:
      #      newlower=int(min(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
       #     newhigher=int(max(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
  
    if int(min(int1.upbound,int2.upbound))==int(max(int1.lowbound,int2.lowbound)):
            mergeIn=''
            newlower=int(min(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
            newhigher=int(max(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
            if int1.left_bound_mark == '(' or int2.left_bound_mark == '[':
                int1.left_bound_mark == '['
            elif int1.left_bound_mark == '[' or int2.left_bound_mark == '(':
                int1.left_bound_mark == '['
            elif int1.right_bound_mark == ')' or int2.right_bound_mark == ']':
                int2.right_bound_mark == ']'
            elif int1.right_bound_mark == ']' or int2.right_bound_mark == ')':
                int2.right_bound_mark == ']'
            while (int1.right_bound_mark==')' and int2.left_bound_mark=="("and int2.right_bound_mark==')' and int1.left_bound_mark=="("):
                raise Exception('invalid') 
            mergeIn=mergeIn+'{}{},{}{}'.format(int1.left_bound_mark,newlower,newhigher,int2.right_bound_mark)
            newmerge = Interval(mergeIn)
    else:
        mergeIn = ''
        newlower=int(min(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
        newhigher=int(max(int1.lowbound,int2.lowbound,int1.upbound,int2.upbound))
        if int1.left_bound_mark == '(' or int2.left_bound_mark == '(':
            int1.left_bound_mark == '('
        elif int1.right_bound_mark == ')' or int2.right_bound_mark== ')':
            int2.right_bound_mark == ')'
        else:
             int1.left_bound_mark == '[' 
             int2.right_bound_mark == ']'  
        mergeIn=mergeIn+'{}{},{}{}'.format(int1.left_bound_mark,newlower,newhigher,int2.right_bound_mark)
        newmerge = Interval(mergeIn)
    return newmerge
#q3
def mergeoverlapping(intlist):
    def sortkey(a):
        return a.lowerbounds
    intlist =sorted(intlist,key = sortkey)
    new_list = []
    temp=intlist[0]
    x=len(intlist)-1
    for i in range(x):
        try:
            temp=mergeIntervals(temp, intlist[i+1])
        except:
            new_list.append(temp)
            temp=intlist[i+1]
    new_list.append(temp)
    return new_list
# q4
def insert(intlist,newint):
    intlist.append(newint)
    return mergeoverlapping(intlist)
#q5
def main():
    start_string = raw_input("List of intervals? (be careful, there need a bland between each intervals)")
    start_list = start_string.split(', ')
    intvs_list = []
    for itnvs in start_list:
        intvs_list.append(Interval(itnvs))
    intvs_list = mergeoverlapping(intvs_list)
    while True: 
        input = raw_input("Interval? ")
        if input != 'quit':
            try:
                insert(intvs_list, Interval(input))
                print 'Now the list is', mergeoverlapping(intvs_list), '.'
            except:
                print 'Invalid!'
        else:
            break 
    
if __name__ == '__main__':
    main()