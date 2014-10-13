class Error(Exception):
				pass

class invalidInterval(Error):
				pass

class invalidMerge(Error):
				pass

class interval(object):
				def __init__(self,intRange):

								
                                                                intRange = intRange.replace(" ","")

                                                                self.orig = intRange

								if intRange[0] == "[":
												self.lowInclusive = 0
								elif intRange[0] == "(":
												self.lowInclusive = 1
								else:
												raise invalidInterval
								if intRange[-1] == "]":
												self.upInclusive = 0
								elif intRange[-1] == ")":
												self.upInclusive = 1
								else:
											 raise invalidInterval

								self.lowerbound = int(intRange[1:-1].split(",")[0])
								self.upperbound = int(intRange[1:-1].split(",")[1])
								self.startvalue = int(intRange[1:-1].split(",")[0]) + self.lowInclusive
								self.endvalue = int(intRange[1:-1].split(",")[1]) - self.upInclusive

								self.inttup = (self.lowerbound, self.startvalue, self.endvalue, self.upperbound)

								if self.endvalue - self.startvalue < 0 :
												self.valid = False
												raise invalidInterval

def mergeIntervals(int1,int2):
				int1tup = int1.inttup
				int2tup = int2.inttup
				LB = ""
				UB = ""
				L = U = 0
				mergeL = mergeH = 0

				if (int1tup[0] + int1tup[1] < int2tup[0] + int2tup[1]):
								firsttup = int1tup
								secondtup = int2tup
				else:
								firsttup = int2tup
								secondtup = int1tup

				try:
								if (firsttup[2] + 1 < secondtup[1]):
												raise invalidMerge
								elif (firsttup[2] >= secondtup[1] and firsttup[2] <= secondtup[2]):
												mergeL = firsttup[0]
												mergeH = secondtup[3]
												L = firsttup[1] - firsttup[0]
												U = secondtup[3] - secondtup[2]
								elif (firsttup[2] <= secondtup[1]):
												mergeL = firsttup[0]
												mergeH = secondtup[3]
												L = firsttup[1] - firsttup[0]
												U = secondtup[3] - secondtup[2]
								else:
												mergeL = firsttup[0]
												mergeH = firsttup[3]
												L = firsttup[1] - firsttup[0]
												U = firsttup[3] - firsttup[2]

								if L == 0:
												LB = "["
								elif L == 1:
												LB = "("

								if U == 0:
												UB = "]"
								if U == 1:
												UB = ")"

				except invalidMerge:
								print("Invalid Merge! \n")

				return interval(LB+str(mergeL)+","+str(mergeH)+UB)

def mergeOverlapping(intlist):

				intlist = sorted(intlist, key = lambda i : (i.inttup[0],i.inttup[1],i.inttup[2],i.inttup[3]))

				mergelist = []

				mergelist.append(intlist[0])
				intlist.pop(0)
				

				while len(intlist) !=  0:
								if mergelist[-1].inttup[2] + 1 < intlist[0].inttup[1]:
												mergelist.append(intlist[0])
												del intlist[0]
								else:
												mergelist.append(mergeIntervals(mergelist[-1],intlist[0])) 
												del mergelist[-2]
												del intlist[0]

				return mergelist

def print_intlist(intlist):
				strlist = []
				for i in intlist:
								strlist.append(i.orig)

				return strlist

def make_intlist(strlist):
				intlist = []
				strlist = strlist.split(", ")
				for i in strlist:
								intlist_interval = interval(i)
								intlist.append(intlist_interval)

				return intlist

def insert(intlist,newint):

				intlist.append(newint)

				return mergeOverlapping(intlist)

if __name__ == ("__main__"):

				intlist = raw_input("Enter the list of intervals:")
				intlist = make_intlist(intlist)
				newint = raw_input("Enter the interval to insert:")
				while newint != "quit":
								try:
												newint = interval(newint)
												newlist = insert(intlist,newint)
												print print_intlist(newlist)
												newint = raw_input("Enter another interval to insert:")
								except:
												print("Invalid Interval!")
												newint = raw_input("Enter another interval to insert:")

				print ("Have a good day!")