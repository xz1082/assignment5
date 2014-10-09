

from __builtin__ import list

#problem 1
class interval:
    def __repr__(self):
        return self.low_inclusive*"["+ (1-self.low_inclusive)*"("+str(self.lo)+ "," +str(self.up)+self.up_inclusive*"]"+ (1-self.up_inclusive)*")"
        
    def __init__(self,a):
        b=a[1:-1].split(",")
        self.lo=int(b[0])
        self.up=int(b[-1])
   
        if a[0]=="[" :#
            self.low_inclusive=True
        else:
            self.low_inclusive=False
        if a[-1]=="]":
            self.up_inclusive=True
        else: 
            self.up_inclusive=False
    
    def Range(self):
        if self.low_inclusive and self.up_inclusive and self.lo<=self.up:
            return range(self.lo,self.up+1)
        elif self.low_inclusive and not self.up_inclusive and self.lo<self.up:
            return range(self.lo,self.up) 
        elif not self.low_inclusive and self.up_inclusive and self.lo<self.up:
            return range(self.lo+1,self.up+1) 
        elif not self.low_inclusive and not self.up_inclusive and self.lo<self.up-1:
            return range(self.lo+1,self.up) 


#problem 2
def mergeIntervals(int1,int2):
    newinterval=interval('(0,0)')
    ls1=int1.Range()
    ls2=int2.Range()
    
    newls= list (set(ls1)&set(ls2))
   
    if not newls :
        raise Exception('not valid')
    else:
        if int1.lo<=int2.lo:
            newinterval.lo=int1.lo
            newinterval.low_inclusive=int1.low_inclusive
            if int1.up<=int2.up:
                newinterval.up=int2.up
                newinterval.up_inclusive=int2.up_inclusive
            else:
                newinterval.up=int1.up
                newinterval.up_inclusive=int1.up_inclusive
        elif int1.lo>=int2.lo:
            newinterval.lo=int2.lo
            newinterval.lo_inclusive=int2.low_inclusive
            if int1.up<=int2.up:
                newinterval.up=int2.up
                newinterval.up_inclusive=int2.up_inclusive
            else:
                newinterval.up=int1.up
                newinterval.up_inclusive=int1.up_inclusive 
     
    return newinterval
  
#test1=interval("(3,9]")
#test2=interval("(8,12]")
#print mergeIntervals(test1,test2)


#problem 3
def mergeOverlapping(intlist):
  
    #print intlist
    intlist.sort(key=lambda x:x.lo-0.5*x.low_inclusive)
    
    current=intlist[0]
    total=[]
    for i in range(1, len(intlist)):
        try:
            current=mergeIntervals(current, intlist[i])
        except:
            total.append(current)   
            current= intlist[i]
        
    total.append(current)
    return total

    
print mergeOverlapping([interval("(1,5)"),interval("(3,11]"),interval("[7,18]"),interval("[6,9]")])       
#print mergeOverlapping(["[1,5]","(2,6]","(8,10]","[8,18]"])
#print mergeOverlapping(["[1,2]", "(3,5)", "[6,7)", "(8,10]", "[12,16]","[4,9]"]) # WRONG


#problem 4
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)


t1=["[1,3]","[6,9]"]
t2=["[2,5]"]
#print insert(t1,t2)
        
#problem 5
def check_interval(interval):
    try:
        lower = int(interval[1:-1].split(",")[0])
        upper = int(interval[1:-1].split(",")[1])
        if(interval[0] == "[" and interval[-1] == ']'):
            if lower <= upper:
                return True
            else:
                return False

        if(interval[0] == "[" and interval[-1] == ")"):
            if lower < upper:
                return True
            else:
                return False

        if(interval[0] == "(" and interval[-1] == "]"):
            if lower < upper:
                return True
            else:
                return False

        if(interval[0] == "(" and interval[-1] == ")"):
            if lower < upper - 1:
                return True
            else:
                return False
    except:
        return False

#problem 5
def main():
    s=raw_input('List of intervals?').split(", ")
    stringlist=[]
    for i in range(len(s)):
        stringlist.append(interval(s[i]))
    
    while True:
        user=raw_input("Intervals?")
        if user=="quit":
            break
        else:
            if(check_interval(user)):
                stringlist = insert(stringlist, interval(user))
            else:
                print "Invalid Interval"
                continue
        print "the current merged is ", stringlist


if __name__=="__main__":
     main()
            
    
             