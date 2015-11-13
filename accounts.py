import pygame, time, random
import operator
import os
import os.path
PIN = ""
def write():
	ask = raw_input("If you have an account press y and if you dont, press n ")
	if ask == "y":
		pinnum = int(raw_input("Enter your PIN: "))
		pinstr = str(pinnum)

		meh = os.path.exists('C:\Users\Dylan\Documents\GitHub\CodeCamp15\\5050.txt')
		print meh
		if os.path.exists('C:\Users\Dylan\Documents\GitHub\CodeCamp15\\%s')%(pinstr):
			print "yes"
		elif os.path.exists('C:\Users\Dylan\Documents\GitHub\CodeCamp15\\%s')%(pinstr) != True:
			print "no"

	elif ask == "n":
		name = raw_input("What do you want your PIN to be? ")
		newfile = open(name+'.txt','w')   # Trying to create a new file or open one
		newfile.close()

	else:
		print "print y or n dummy"
write()