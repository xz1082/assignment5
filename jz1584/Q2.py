
def mergeIntervals(int1,int2):
    """
    this function merge any two overlap string-typed intervals, input should be strings, for example int1="[-2,3]"
    """
    #get the value from string 
    def extract_value(interv):
        if interv[1]=="-":
            left=int(interv[1:3])
            if interv[-3]=="-": right=int(interv[-3:-1])
            else:right=int(interv[-2])
        else:
            left=int(interv[1])
            if int1[-3]=="-": right=int(interv[-3:-1])
            else:right=int(interv[-2])
        return left, right
    
    left1,right1=extract_value(int1)
    left2,right2=extract_value(int2)
    #print left1,right1
    #print left2,right2
    
    """getting lists of number from each interval
    """
    int1_list=[]
    int2_list=[]
    
    if int1[0]=='[' and int1[-1]==']': int1_list=range(left1,right1+1)
    elif int1[0]=='(' and int1[-1]==')': int1_list=range(left1+1,right1)
    elif int1[0]=='(' and int1[-1]==']': int1_list=range(left1+1,right1+1)
    else: int1_list=range(left1,right1)
    
    if int2[0]=='[' and int2[-1]==']': int2_list=range(left2,right2+1)
    elif int2[0]=='(' and int2[-1]==')': int2_list=range(left2+1,right2)
    elif int2[0]=='(' and int2[-1]==']': int2_list=range(left2+1,right2+1)
    else: int2_list=range(left2,right2)
    
    #print int1_list
    #print int2_list
    
    
    try:
        
        if len(set(int1_list).intersection(int2_list)) > 0:
            merge_list=range(min(int1_list[0],int2_list[0]),max(int1_list[-1],int2_list[-1])+1)
            print "[%s,%s]"%(merge_list[0],merge_list[-1])
            
        else:
            c=d  # just for geting an error pass to an exception 
            
    except:
        print "The intervals do not overlap"
    
"""
#testing, works!
a=("[1,5)" )
b=("(-2,7]")
#note [-1,7] is the same as (-2,7]
mergeIntervals(a,b)
"""
