import os
import sys
import re


class Interval:
    def __init__(self,interval):
        self.interval = interval
        a,b = interval.strip(' ()[]').split(',')
        self.LBound = int(a)
        self.UBound = int(b)

        self.a = interval.strip()[0]
        self.b = interval.strip()[-1]

        self.firstNum = self.LBound + int(self.a == '(')
        self.lastNum = self.UBound - int(self.b == ')')
    def __repr__(self):
        return int(self.a == '(') * '(' + (1-int(self.a=='(')) * '[' + str(self.LBound) + ',' + str(self.UBound) + int(self.b == ']') * ']' + (1 - int(self.b == ']')) * ')'
    
def d_validity(interval):
    validity = True
    if interval.strip().find(',') == -1:
        validity = False
        #print validity
    elif interval.strip().find('(') == -1 or interval.strip().find(')') == -1 :
        print "stuck here"
        if interval.strip().find('[') == -1 or interval.strip().find(']') == -1:
            validity = False
            #print validity
    if validity == True:
    
        a = interval.strip()[0]
        b = interval.strip()[-1]
        L, U = interval.strip(' ()[]').split(',')
        
        if L.isdigit() == True and U.isdigit() == True:
            LBound = int(L)
            UBound = int(U)
            
            if a == '(' and b == ')':
                if LBound >= UBound - 1:
                    validity = False
            elif (a == '(' and b == ']') or (a == '[' and b == ')'):
                if LBound >= UBound:
                    validity = False
            elif a == '[' and b == ']':
                if LBound > UBound:
                    validity = False
        else:
            validity = False
    
    return validity
    
def overlapped(int1,int2):
        intList = (int1, int2)
        intList = sorted(intList, key = lambda num:(num.LBound,num.firstNum,num.lastNum,num.UBound))
        if intList[0].lastNum + 1 < intList[1].firstNum:
            return False
        return True

def mergeInterval(int1, int2):
        if overlapped(int1,int2) != True:
            raise Exception ("Not overlapped")
        intList = (int1, int2)
        intList = sorted(intList, key = lambda num:(num.LBound,num.firstNum,num.lastNum,num.UBound))
        if intList[0].lastNum < intList[1].lastNum:
            return Interval(int(intList[0].a == '(') * '(' + (1-int(intList[0].a=='('))*'[' + str(intList[0].LBound) + ',' + str(intList[1].UBound) + int(intList[1].b==']')*']' + (1-int(intList[1].b==']'))*')')
        return intList[0]

def mergeOverlapping(intList):
    intList = sorted(intList, key = lambda num: (num.LBound, num.firstNum, num.lastNum, num.UBound))
    newList = []
    newList.append(intList[0])
    intList.pop(0)
    while len(intList) != 0:
        if overlapped(intList[0],newList[-1]) == True :
            newList[-1] = (mergeInterval(intList[0],newList[-1]))
        else:
            newList.append(intList[0])
        intList.pop(0)
    #print newList
    return newList

def insert(intList,interv):
    intList.append(interv)
    return mergeOverlapping(intList)

def getInput(string):
    intListE = string.split(", ")
    intList = []
    for i in intListE:
        intList.append(Interval(i))
    return intList

def print_List(intList):
    finalList = []
    for i in intList:
        finalList.append(i)
    return finalList

if __name__ == "__main__":
    intList = getInput(raw_input("Please enter the intervals:"))
    ipt = raw_input("Intervals?")
    while ipt != "quit":
        if d_validity(ipt) == False:
            print "Invalid Interval"
            ipt = raw_input("Intervals?")
        else:
            itv = Interval(ipt)
            intList = insert(intList, itv)
            print print_List(intList)
            ipt = raw_input("Intervals?")
    
