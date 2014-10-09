'''
Created on Oct 7, 2014

@author: ds-ga-1007
'''
class interval:
    def __init__(self, s=''):
        if s!='':
            l1=s.split(',')
            left=l1[0]
            right=l1[-1]
            self.lower=int(left.strip()[1:])
            self.upper=int(right.strip()[:-1])
           
            if left.strip()[0]=='(':
                self.lower_inclu=False
            elif left.strip()[0]=='[':
                self.lower_inclu=True
            if right.strip()[-1]==')':
                self.upper_inclu=False
            elif right.strip()[-1]==']':
                self.upper_inclu=True
            
            if self.lower+int(not self.lower_inclu)>=self.upper+int(self.upper_inclu):
                raise Exception('This interval is invalid!')
            
    
    def __repr__(self):
        inter=self.lower_inclu*'['+(not self.lower_inclu)*'('+str(self.lower)+','+str(self.upper)+self.upper_inclu*']'+(not self.upper_inclu)*')'
        return inter
        #return '{} represents the numbers {} through {}'.format(inter,interval.ran(self)[0],interval.ran(self)[-1])
    def ran(self):
        return range(self.lower+int(not self.lower_inclu),self.upper+int(self.upper_inclu))

def mergeIntervals(int1, int2):
    r1=int1.ran()
    r2=int2.ran()
    if r1[-1]<r2[0]-1 or r1[0]>r2[-1]+1:
        raise Exception('Two intervals do not overlap!')
    else:
        lower=min(r1+r2)
        upper=max(r1+r2)
        if lower in r1:
            if lower in r2 and int1.lower>int2.lower:
                lower,lower_inclu=int2.lower,int2.lower_inclu
            else:
                lower,lower_inclu=int1.lower,int1.lower_inclu                    
        elif lower in r2:
            lower,lower_inclu=int2.lower,int2.lower_inclu 
        
        if upper in r1:
            if upper in r2 and int1.upper<int2.upper:
                upper,upper_inclu=int2.upper,int2.upper_inclu
            else:
                upper,upper_inclu=int1.upper,int1.upper_inclu            
        elif upper in r2:
            upper,upper_inclu=int2.upper,int2.upper_inclu
    res=interval()
    res.lower,res.upper,res.lower_inclu,res.upper_inclu=lower,upper,lower_inclu,upper_inclu
    return res

def mergeOverlapping(intlist):
    intlist.sort(key=lambda x:x.lower-x.lower_inclu)
    temp=intlist[0]
    res=[]
    for i in range(len(intlist)-1):
        try:
            temp=mergeIntervals(temp, intlist[i+1])
        except:
            res.append(temp)
            temp=intlist[i+1]
    res.append(temp)   
    return res

def insert(intlist, newint): 
    intlist.append(newint)
    res=mergeOverlapping(intlist)
    return res
           
def main():
    s=raw_input('List of intervals? ')
    li=s.split(', ')
    intlist=[interval(x) for x in li]
    intlist=mergeOverlapping(intlist)
    s=raw_input('Interval? ')
    while s!='quit':
        try:
            newint=interval(s)
            res=insert(intlist,newint)
            for it in res[:-1]:
                print str(it)+',',
            print res[-1]           
        except:
            print 'Invalid interval'
        s=raw_input('Interval? ')

if __name__ == '__main__':
    main()
    