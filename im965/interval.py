#interval.py (assignment 5 for programming for DS)

#start by declaring the class interval

class interval:

  def __init__(self,intstr):
    
    #input errors
    if type(intstr) is str==False :
      raise NameError("Input interval as a string")
    if (intstr[0]!='[') and (intstr[0]!='(') :
      raise NameError("Must start with ( or [")

    if (intstr[-1]!=']') and (intstr[-1]!=')') :
      raise NameError("Must end  with ) or ]")
    
    
    #make sure start/endpoints are numeric
    import re
    res=re.findall("\d+\,",intstr)
    ree=re.findall("\,\d+",intstr)

 
    res=re.sub(r',','',res[0])
    ree=re.sub(r',','',ree[0])
    

    ts=int(res)
    te=int(ree)
        
    #seperate into four classes (open), [closed], (OC] , [CO)
    #foreach class: raise exception if need define list endpoint

    if intstr[0]=="(" and intstr[-1]==")" :
      intclass=1
    if intstr[0]=="[" and intstr[-1]=="]" :
      intclass=2
    if intstr[0]=="(" and intstr[-1]=="]" :
      intclass=3
    if intstr[0]=="[" and intstr[-1]==")" :
      intclass=4


    #make sure ordering 'makes sense' as stated in the assignment
    if intclass==1 and not ts<(te-1) :
      raise NameError("Endpoints error") 
    if intclass==2 and not ts<=te :
      raise NameError("Endpoints error") 
    if (intclass==3 or intclass==4) and not ts<te :
      raise NameError("Endpoints error") 

    #endpoints depending on open or closed braces
    if intclass==1 or intclass==3 :
      tsa=ts+1
    if intclass==2 or intclass==4 :
      tsa=ts
    if intclass==1 or intclass==4 :
      tea=te-1 
    if intclass==2 or intclass==3 :
      tea=te

    #attributes : list,type, start,end
    self.mem=[z for z  in range(tsa,tea+1,1)]
    self.oc=intclass
    self.start=tsa
    self.end=tea
    self.bs=intstr[0]
    self.be=intstr[-1]

  #print (repr)
  def __repr__(self):
    strp = "["+str(self.start)+","+str(self.end)+"]"
    return strp


#define a function that merges the intervals
def mergeIntervals(int1,int2) :
  
  #first, check to make sure that the intervals overlap
    if int1.start<int2.start and int1.end<int2.start:
      raise NameError("No overlap between intervals")
  
    if int1.start>int2.start and int1.end>int2.start:
      raise NameError("No overlap between intervals")

  #extract min/max
    iis=min(int1.start,int2.start)
    iie=max(int1.end,int2.end)

  #return merged
    ii="["+str(iis)+","+str(iie)+"]"
    return interval(ii)


def mergeOverlapping(intlist) :

  #generate a list with class object
  clist=[]
  mlist=[]
  
  for i in intlist :
    tmem=interval(i)
    mem=tmem.mem
    for j in mem :
        mlist.append(j)

 
  setlist=set(mlist)
  ulist=list(setlist)
  ulist.sort()

  stop=len(ulist)
  
  iter=0
  new=1
  olist=[]

  while iter<stop :
      
    if new==1 :
      sb=ulist[iter]
      new=0
    
    if iter==stop-1 :
      insert="["+str(sb)+","+str(ulist[iter])+"]"
      olist.append(interval(insert))
      iter=iter+1

    elif ulist[iter]==ulist[iter+1]-1 :
      iter=iter+1
   
    else :
      insert="["+str(sb)+","+str(ulist[iter])+"]"
      olist.append(interval(insert))
      new=1
      iter=iter+1

  return olist



def insert(intlist,newint) :
  intlist.append(newint)
  presort= mergeOverlapping(intlist)
  sorted=sorted(presort,key=lambda int: int.start)
  return sorted

########
inp=input('List of intervals? ')

if inp!='quit':
  a=inp.split(",")
  b=[]

for i in range(0,len(a),2) :
  b.append(a[i]+","+a[i+1])

output=mergeOverlapping(b)
print output

while inp!='quit' :
  if inp!='quit' :
    inp=input('another interval? ')
    b.append(inp)
    zz=mergeOverlapping(b)
    print zz

  else:
    print "You have quit the interval program"
