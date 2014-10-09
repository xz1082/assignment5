#include packages:

import itertools
import numpy as np


#######################  Classes ##########################
class Myexception(Exception):
	def __str__(self):
		return "Boundry notation Error"


class Interval:
	def __init__(self, string1):
		string2 = string1.replace(" ", "")
	 	parts = string2.split(",")
                if len(parts) != 2 :
                	raise Myexception()       
                low_r = int(parts[0][1:])
                high_r = int(parts[1][:-1])


		if string2[0] == "[":
			self.bound_low = "["
			if string2[-1] =="]": # [,]
				#print "yay"
				self.low_r = low_r
				self.high_r = high_r
				self.bound_high = "]"
				
				if self.low_r >self.high_r:
					raise NameError("Values are weirddd!")
				
			elif string2[-1] == ")": #[,)
				#print "[,)"
				self.bound_high = ")"
				self.low_r = low_r
                                self.high_r = high_r-1

				if self.low_r >self.high_r:
                                        raise NameError("Values are weirddd!")

			else:
				raise Myexception()
		elif string2[0] == "(": 
			self.bound_low  = "("
                        if string2[-1] =="]": # (,]
                                #print "yay"
				self.bound_high = "]"
				self.low_r = low_r+1
                                self.high_r = high_r

				if self.low_r >self.high_r:
                                        raise NameError("Values are weirddd!")


                        elif string2[-1] == ")": #(,)
				self.bound_high = ")"
				self.low_r = low_r+1
                                self.high_r = high_r-1

				if self.low_r >self.high_r:
                                        raise NameError("Values are weirddd!")

                        else:
                                raise Myexception()

		else:
			raise Myexception()

		#print self.low_r, self.high_r, self.bound_low, self.bound_high

	def __repr__(self):
		str = "This is the boundry %d %d " % (self.low_r, self.high_r)
		return str
###################### Functions #################

def mergeIntervals(int1, int2):
	int1 = Interval(int1)
	int2 = Interval(int2)
	#if overlap, merge:

	a = int1.low_r
	b = int1.high_r
	c = int2.low_r
	d = int2.high_r
	
	if a<=c and b+1 >=c: # note that we are adding +1 to b to account for [1,4]+[5,6] --> [1,6]
		
		if b <= d: #overlap
			if int1.bound_low == "(":
				a = a-1
			if int2.bound_high == ")":
				d = d+1
			return "%s %d, %d %s" % (int1.bound_low, a, d, int2.bound_high)

		else: #contained
			if int1.bound_low == "(":
                                a = a-1
                        if int1.bound_high == ")":
                                b = b+1
                        return "%s %d, %d %s" % (int1.bound_low, a, b, int1.bound_high)


	elif c<=a and d+1>=a:
	
		if d<= b: #overlap
			if int2.bound_low == "(":
                                c = c-1
                        if int1.bound_high == ")":
                                b = b+1
                        return "%s %d, %d %s" % (int2.bound_low, c, b, int2.bound_high)

		else: #contained
			if int2.bound_low == "(":
                                c = c-1
                        if int2.bound_high == ")":
                                d = d+1
                        return "%s %d , %d %s" % (int2.bound_low, c, d, int1.bound_high)
	else:
		raise NameError("Ranges do not overlap")	



def mergeOverlapping(li):
	merged_li = []
	# Sort list by lower bound for easier merging
	li.sort(key=lambda x: Interval(x).low_r)
	print li
	while len(li)>1:
		try: 
			temp =  mergeIntervals(li[0], li[1])
			li.pop(0) #remove element we are done with
			li[0] = temp
		except:
			merged_li.append(li.pop(0))

	merged_li.append(li[0])	
	return  merged_li #merged range!
		

def insert(intlist, newint):
	intlist.append(newint)
	return mergeOverlapping(intlist)


def parsing_f(initial):
	cum_li = []
        counter_low = []
        counter_high =[]
        for i,c in enumerate(initial):
        
                if c == "[" or c == "(":
                        counter_low.append(i)

                if c == "]" or c == ")":
                        counter_high.append(i)

        for x in zip(counter_low,counter_high):
                cum_li.append(initial[x[0]:x[1]+1])

	return cum_li


#####################################33		


if __name__ == "__main__":
	initial = raw_input("Please enter a list of intervals:   ")

	cum_li = parsing_f(initial)
	
	while cum_li == [] and initial != "quit":
		initial = raw_input("Oops.... something went wrong. Please enter list again:  ")
		cum_li = parsing_f(initial)


	if initial != "quit":
		intervaltoadd = raw_input("Interval?")
		while intervaltoadd != "quit":
			if len(intervaltoadd) < 1:
				intervaltoadd = raw_input("Interval? ")
			else:
				try:
					Interval(intervaltoadd) #check to make sure that the interval is by speficiations.
					cum_li = insert(cum_li, intervaltoadd)
					print ".... the result of merging intervals... ", cum_li
					intervaltoadd = raw_input("Interval? ")
				except:
					intervaltoadd = raw_input("Don't be sloppy. Try again...  ")
