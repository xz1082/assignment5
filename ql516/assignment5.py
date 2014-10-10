'''
Created on Oct 7, 2014

@author: LaiQX
'''
# Q1: Class  
class interval(object):
    def __init__(self,strr):
        #True is inclusive
        if strr[0]=='[':
            self.l=True
        else:
            self.l=False
        if strr[-1]==']':
            self.u=True
        else:
            self.u=False
        coma_i=strr.index(',')
        self.x=int(strr[1:coma_i])
        self.y=int(strr[coma_i+1:-1])
        self.data=[]
        if self.x>self.y: 
            print "error:!"
        else:
            if self.u and self.l:
                self.data=range(self.x,self.y+1)
            if (self.u and (not self.l)) :
                if self.x!=self.y: 
                    self.data = range(self.x+1,self.y+1)
                else : 
                    print "error:!!1" 
            if ((not self.u) and self.l) :
                if self.x!=self.y: 
                    self.data = range(self.x,self.y)
                else :
                    print "error:!!2"
            if ((not self.u)and (not self.l)) :
                if self.x<self.y-1:
                    self.data = range(self.x+1,self.y)
                else :
                    print "error:!!!3"

    def __repr__(self):
        if self.l:
            ll="["
        else:
            ll="("
        if self.u:
            uu="]"
        else:
            uu=")"
        str_out=ll+str(self.x)+','+str(self.y)+uu
        return str_out
        

#Q2: mergeIntervals()        
def mergeIntervals(int1, int2):
    s1=set(int1.data)
    s2=set(int2.data)
    if (s1-s2) == s1:
        return (int1.data[-1]+int2.data[-1])
    else:
        if int1.x<int2.x:
            xx=str(int1.x)
            if int1.l: ll='['
            else: ll='('
        else:
            xx=str(int2.x)
            if int2.l: ll='['
            else: ll='('
        
        if int1.y>int2.y:
            yy=str(int1.y)
            if int1.u :
                uu=']'
            else:
                uu=')'
        else:
            yy=str(int2.y)
            if int2.u :
                uu=']'
            else:
                uu=')'
        intvl= ll+xx+','+yy+uu
        return interval(intvl)
# check whether the two intervals can be merged
def mergable(int1,int2):
    if int1.data[0]<=int2.data[0]:
        l1=int1
        l2=int2
    else:
        l2=int1
        l1=int2
    return (l1.data[-1]>=l2.data[0]-1)

#merge function    
def merge(int1,int2):
    if mergable(int1,int2):
        if int1.x<=int2.x:
            xx=str(int1.x)
            if int1.l: ll='['
            else: ll='('
        else:
            xx=str(int2.x)
            if int2.l: ll='['
            else: ll='('
        
        if int1.y>=int2.y:
            yy=str(int1.y)
            if int1.u :
                uu=']'
            else:
                uu=')'
        else:
            yy=str(int2.y)
            if int2.u :
                uu=']'
            else:
                uu=')'
        intvl= ll+xx+','+yy+uu
        return interval(intvl)   

#Q3: mergeOverlapping function
def mergeOverlapping(intlist):
    itvstd = sorted(intlist,key=lambda intva: intva.data[0])
    n=len(itvstd)
    head =itvstd[0]
    new = []
    for i in range(1,n):
        if mergable(head,itvstd[i]):
            head=merge(head,itvstd[i])
        else:
            new.append(head)
            head=itvstd[i]
    new.append(head)
    return new

#Q4: insert()
def insert(intlist,newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

#Q5: main 
x=raw_input("List of intervals? ")
inlist=x.split(', ')
intval_list = []
for i in range(len(inlist)):
    intval_list.append(interval(inlist[i]))
while True:
    y=raw_input("Interval?")
    if y=="quit":
        break
    try:
        y_int=interval(y)
        intval_list=insert(intval_list,y_int)
        print intval_list
    except:
        print 'Invalid Interval'
        continue

