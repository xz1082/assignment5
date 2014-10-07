'''
Created on Oct 7, 2014

@author: LaiQX
'''
import pandas as pd

class interval:
    def _init_(self,x,y,l=False,u=False):
        #false = inclusive
        self.x = x
        self.y = y
        self.l = l
        self.u = u
        if x>y: print "error:! "
        elif u and l: return range(x,y+1)
        elif (u and (not l)) : return range(x+1,y+1)
        elif ((not u) and l) : return range(x,y)
        elif ((not u)and (not l)): return 
    