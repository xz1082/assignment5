
#Problem 1
class interval:
    def __repr__(self):
        return self.lo+str(self.lf)+','+str(self.rt)+self.up
        
    def __init__(self,rep):
        self.rep=rep 
        self.num=self.rep[1:-1].split(",")
        self.lf=int(self.num[0])
        self.rt=int(self.num[1])
        self.lo=rep[0]
        self.up=rep[-1]
        
        if (self.lo=='[' and self.up==']'):
            self.lf<=self.rt
        elif ((self.lo=='(' and self.up==']') or (self.lo=='[' and self.up==')')):
            self.lf<self.rt
        elif (self.lo=='(' and self.up==')'):
            self.lf<self.rt-1
        else:
            raise Exception ("Invalid Interval")
        
    def span(self):    
        if (self.lo=='[' and self.up==']'):
            return range(self.lf,self.rt+1)
        elif (self.lo=='(' and self.up==']'):
            return range(self.lf+1,self.rt+1)
        elif (self.lo=='[' and self.up==')'):
            return range(self.lf,self.rt)                        
        else:
            return range(self.lf+1,self.rt)
            
    def change(self,a,b,c,d):
        self.lo=a
        self.lf=b
        self.rt=c
        self.up=d
        
        
        


#Problem 2

def mergeIntervals(int1,int2):
    newint=interval('(0,0)')
        
    if int1.span()[0]>int2.span()[0]:
        tmp=int2
        int2=int1
        int1=tmp
        
        
    newrt=max(int1.rt,int2.rt)     
    if  set(int1.span())&set(int2.span()) or int2.span()[0]-int1.span()[-1]<2:
        if newrt==int2.rt:
           newint.change(int1.lo,int1.lf,newrt,int2.up)
        else:
           newint.change(int1.lo,int1.lf,newrt,int1.up)

    else:
        raise Exception('Can\'t be merged')
        
    return newint
        


#Problem 3

def mergeOverlapping(intlist):
    intlist.sort(key=lambda x: x.span()[0])
    newint=[intlist[0]]
    
    for elem in intlist:
        try:
            newint[-1]=mergeIntervals(elem,newint[-1]) 
        except Exception:
            newint.append(elem)
        
    return newint 


 

#Problem 4
def insert(intlist,newint):
    
    #insertion
    if intlist[-1].span()[0]<=newint.span()[0]:
        intlist.append(newint)
    else:
        for i in range(len(intlist)-1):
            if intlist[i].span()[0]<=newint.span()[0] and newint.span()[0]<=intlist[i+1].span()[0]:
               intlist.insert(i+1,newint)
               break
    
         
    #Merge
    intlist=mergeOverlapping(intlist)

    return intlist       
         
    
   

#Problem 5

def main():
    import re
    listofint=raw_input('List of intervals? ')
    try:
        listofint=[interval(x) for x in re.split('(?<=[\]\)])\s*,\s*', listofint)]
    except Exception:
        print "Invalid Interval Input"
        
        
    while True:    
        newinput=raw_input('Interval? ')
        if newinput=='quit':
            break
        else:
            try:
                listofint=insert(listofint,interval(newinput))
                print listofint
            except Exception:
                print 'Invalid interval'
                continue
        
    

if __name__=='__main__':
    main()
    





    
    
    
    
