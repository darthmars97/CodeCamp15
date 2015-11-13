import pygame, time, random
import operator
import os
import os.path
status = "off"
PIN = ""
name = ""
def write():
	ask = raw_input("If you have an account press y and if you dont, press n ")
	if ask == "y":
		while status == "off":
			names = raw_input("Enter your pin: ")+".txt"
			if os.path.exists(names):
				name = names
				status = "on"
			else:
				print "This pin does not exist" 

	elif ask == "n":
		status = "off"
		while status == "off":	
			name = raw_input("Enter your desired 4 digit pin: ")+".txt"
			os.system('cls')
			if os.path.exists(name):
				print "That pin is already taken, try another one"
			else:
				open(name, "a")
				print "Congrats your pin now created"
				status = "on"

	else:
		print "print y or n dummy"
write()