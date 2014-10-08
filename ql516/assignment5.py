'''
Created on Oct 7, 2014

@author: LaiQX
'''

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
        return str(self.data)
        
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

def isovlp(int1,int2):
    s1=set(int1.data)
    s2=set(int2.data)
    if (s1-s2) == s1:  
        return False
    else:
        return True
    
def mergeOverlapping(intlist):
    itvstd = sorted(intlist,key=lambda intva: intva.data[0])
    n=len(itvstd)
    head =itvstd[0]
    new = []
    for i in range(1,n-1):
        if isovlp(head,itvstd[i]):
            head=mergeIntervals(head,itvstd[i])
        else:
            new.append(head)
            head=itvstd[i]
    new.append(head)
    return new


int1=interval("[12,18]")
int2=interval("(17,20)")
int_m=mergeIntervals(int1, int2)
print int_m

intlist=[interval("[1,5]"),interval("[2,6)"),interval("(8,10]"),interval("[8,18]")]
print intlist
new = mergeOverlapping(intlist)
print new