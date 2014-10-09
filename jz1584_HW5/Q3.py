import re
def mergeOverlapping(intlist):
    """
    define a function that can merge a list of string intervals
    """
    #orgainize a list of string intervals
    def Rconvert(string_list):
        nlist=re.findall(r'[+-]?\d+', string_list)
        Nlist=[int(i) for i in nlist]
        blist=re.findall(r'[()[\]]', string_list)
    
        #convert a string list of interval to  equivalent inclusive range
        #for example, in integers case, (3,5) is the same as [2,4]
        for i in range(len(blist)):
            if blist[i]== ")":
                Nlist[i]=Nlist[i]- 1
            if blist[i]== "(":
                Nlist[i]=Nlist[i]+ 1
        #print Nlist
        rlist=[]#create a list of tuple 
        for i in range(0 ,len(Nlist)-1,2):
            rlist.append((Nlist[i],Nlist[i+ 1]))
        return rlist
    rlist=Rconvert(intlist)
    #print rlist
    #mergiing sorted list
    def merging(rlist):
        rlist.sort()
        def slim(rlist,diff):
            init=len(rlist)-diff-1
            if init<1:
                return rlist
            if rlist[init][0]>rlist[init-1][1]:
                return slim(rlist,diff+1)
            else:
                rlist[init-1]=((rlist[init][0],rlist[init-1][0])[rlist[init-1][0]<rlist[init][0]],(rlist[init][1],rlist[init-1][1])[rlist[init-1][1]>rlist[init][1]])
                del rlist[init]
                return slim(rlist,0)
        return slim(rlist,0)
    finalist=merging(rlist)
    #print finalist
    outputlist=[]
    for i in finalist:
        outputlist.append(list(i))
    #print outputlist#just for instant output result

    return outputlist#just for the purpose of Question 4 

"""
#testing codes, works!
print "Note:Merged all intervals into equivalent inclusive-interval form:"
intlist='(2,5],[-2,7),(7,10],[8,18]'
a=mergeOverlapping(intlist)
print a 

"""
