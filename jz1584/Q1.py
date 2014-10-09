import re
class interval:
    """
    class take string representation of the interval 
    """
    def __init__(self,A):
        self.A=A
        #extra numbers from inputed string A
        nlist=re.findall(r'[+-]?\d+',self.A)
        left=int(nlist[0])
        right=int(nlist[-1])
        
        #defined the requirements of inputed interval regarding the inclusive and exclusive bounds
      
        if self.A[0]=="[" and self.A[-1]==']':# both inclusive
            if left > right: raise ValueError ("Invalid interval: lower must not be more than upper if both bounds are inclusive ")
          
        
        elif self.A[0]=="(" and self.A[-1]==')':#both exclusive
            if left>=right-1:
                raise ValueError ("Invalid interval: lower must be less than upper - 1 if both bounds are exclusive ")
        
        else: #either exclusive or inclusive
            if left>=right:
                raise ValueError ("Invalid interval: lower must be less than upper if either bounds is inclusive ")
    
    
    def __repr__(self):
            return "%s" %(self.A)
        


"""
#Code testing, works!
#normal case testing
a=interval("[2,2]")
b=interval('[-2,2)')
c=interval("(2,400)")
d=interval("(-3,-2]")
print a, b, c, d
#error cases testing:
#f=interval("(-2,-1)") #error should be expected
#print f

"""


    