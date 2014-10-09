import os
import sys
import re
import numpy as np


class interval:
	def __init__(self, inter):
		self.expr = inter.replace(" ", "")

		if validOrNot(self.expr) == None:
			self.valid = False
			raise InitErr
			return

		self.L = self.expr[0]
		self.R = self.expr[-1]

		self.bound = self.expr.strip("()[]").split(",")

		for i in range(len(self.bound)):
			self.bound[i] = int(self.bound[i])
		
		self.firstNum = self.bound[0]
		if self.L == "(":
			self.firstNum = self.bound[0] + 1
	
		self.lastNum = self.bound[1]
		if self.R == ")":
			self.lastNum = self.bound[1] - 1

		if self.firstNum > self.lastNum:
			self.valid = False
			raise InitErr
			return

		self.valid = True

	
	def __repr__(self):
		return self.expr + " represents the number " + str(self.firstNum) + " through " + str(self.lastNum)

class InitErr(Exception):
	def __str__(self):
		return "Invalid Interval"

class MergeErr(Exception):
	def __str__(self):
		return "Can not merge."

def validOrNot(interval):
	return re.match(r"^[\[\(]\s*-?\d+\s*\,\s*-?\d+\s*[\)\]]$", interval)


def overlappedOrNot(int1, int2):
	intlist = sorted([int1, int2], key = lambda i: (i.bound[0], i.firstNum, i.lastNum, i.bound[1]))
	
	if intlist[0].lastNum + 1 < intlist[1].firstNum:
		return False
	return True


def mergeIntervals(int1, int2):
	if not overlappedOrNot(int1, int2):
		raise MergeErr

	intlist = sorted([int1, int2], key = lambda i: (i.bound[0], i.firstNum, i.lastNum, i.bound[1]))

	return  interval( intlist[0].L + str(intlist[0].bound[0]) + "," + str(intlist[1].bound[1]) + intlist[1].R )


def mergeOverlapping(intlist):
	intlist =  sorted(intlist, key = lambda i: (i.bound[0], i.firstNum, i.lastNum, i.bound[1]))

	stack = [intlist[0]]
	intlist.pop(0)
	while len(intlist) != 0:
		if overlappedOrNot(stack[-1], intlist[0]):
			stack[-1] = mergeIntervals(stack[-1], intlist[0])
		else:
			stack.append(intlist[0])
		intlist.pop(0)

	return stack


def insert(intlist, newint):
	intlist.append(newint)
	return mergeOverlapping(intlist)


def set_intlist(intlist_expr):
	intlist_expr =  intlist_expr.split(", ")

	intlist = []
	for i in intlist_expr:
		tmpint = interval(i)
		if not tmpint.valid:
			return []
		intlist.append( tmpint )

	return intlist


def print_intlist(intlist):
	for i in range(len(intlist)):
		print intlist[i].expr,
	print ""

if __name__ == "__main__":

	intlist = set_intlist( raw_input("List of intervals? ") )
	while len(intlist) == 0:
		intlist = set_intlist( raw_input("Invalid interval\nList of intervals? ") )
		
	ipt = raw_input("Intervals? ")
	while ipt != "quit":

		try:
			i = interval( ipt )
		except:
			ipt = raw_input("Invalid interval\nIntervals? ")
			continue

		intlist = insert(intlist, i)

		print_intlist( intlist )

		ipt = raw_input("Intervals? ")


