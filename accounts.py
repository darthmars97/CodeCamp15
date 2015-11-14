import pygame, time, random
import operator
import os
import os.path
basemoney = "10000"
money = 0
name = ""
status = "off"
#LOGIN


def login():

	ask = raw_input("If you have an account press y and if you dont, press n ")
	if ask == "y":
		while status == "off":
			names = raw_input("Enter your username: ")+".txt"
			if os.path.exists(names):
				name = names
				status = "on"
				print "You are now logged in"
			else:
				print "This username does not exist" 
	#SIGNUP
	elif ask == "n":
		status = "off"
		while status == "off":	
			name = raw_input("Enter your desired username: ")+".txt"
			os.system('cls')
			if os.path.exists(name):
				print "That username is already taken, try another one"
			else:
				open(name, "a")
				print "Congrats your username is now created"
				status = "on"

	#IF FILE IS EMPTY PUT 0 IN IT
	money = open(name, "r").read()
	while status == "on":
		if os.stat(name).st_size == 0:
			with open(name, "w") as myfile:
				myfile.write(basemoney)
		else:
			pass

	#ADDS THE NUMBER TO THE FILE 
		filen = open(name, "w")
		added = str(money)
		with open(name, "w") as myfile:
			myfile.write(added)
	name.close()

