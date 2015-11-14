import pygame, time, random
import operator
import os
import turtle




songs = {
	'Hello - Adele': 10,
	'Hotline Bling - Drake': 10,
	'The Hills - The Weeknd': 10,
	'Sorry - Justin Beiber': 10,
	'What Do You Mean? - Justin Beiber': 10,
	'Stiches - Shawn Mendes': 10,
	'Focus - Ariana Grande': 10,
	'Wildest Dreams - Taylor Swift': 10,
	'679 - Fetty Wap': 10,
	'Like Im Gonna Lose You - Meghan Trainor': 10,
	'Locked Away - R. City': 10,
	'Exs & Ohs - Elle King': 10,
	'Here - Alessia Cara': 10,
	'Cant Feel My Face - The Weeknd': 10,
	'Watch Me - Silento': 10,
	'Jumpman - Drake & Future': 10,
	'Same Old Love - Selena Gomez': 10,
	'On My Mind - Ellie Goulding': 10,
	'Lean On - Major Lazer & DJ Snake': 10,
	'Renegades - X Ambassadors': 10,
	'Downtown': 10,
	'Hit The Quan - iLoveMemphis': 10,
	'Tennessee Whiskey': 10,
	'Trap Queen - Fetty Wap': 10,
	'Good For You - Selena Gomez': 10,
	'Drag Me Down - One Direction': 10,
	'Antidote - Travi$ Scott': 10,
	'Die A Happy Man - Thomas Rhett': 10,
	'How Deep Is Your Love - Calvin Harris': 10,
	'Where Ya At - Future feat Drake': 10,
}

s1 = songs['Hello - Adele']
s2 = songs['Hotline Bling - Drake']
s3 = songs['The Hills - The Weeknd']
s4 = songs['Sorry - Justin Beiber']
s5 = songs['What Do You Mean? - Justin Beiber']
s6 = songs['Stiches - Shawn Mendes']
s7 = songs['Focus - Ariana Grande']
s8 = songs['Wildest Dreams - Taylor Swift']
s9 = songs['679 - Fetty Wap']
s10 = songs['Like Im Gonna Lose You - Meghan Trainor']
s11 = songs['Locked Away - R. City']
s12 = songs['Exs & Ohs - Elle King']
s13 = songs['Here - Alessia Cara']
s14 = songs['Cant Feel My Face - The Weeknd']
s15 = songs['Watch Me - Silento']
s16 = songs['Jumpman - Drake & Future']
s17 = songs['Same Old Love - Selena Gomez']
s18 = songs['On My Mind - Ellie Goulding']
s19 = songs['Lean On - Major Lazer & DJ Snake']
s20 = songs['Renegades - X Ambassadors']
s21 = songs['Downtown']
s22 = songs['Hit The Quan - iLoveMemphis']
s23 = songs['Tennessee Whiskey']
s24 = songs['Trap Queen - Fetty Wap']
s25 = songs['Good For You - Selena Gomez']
s26 = songs['Drag Me Down - One Direction']
s27 = songs['Antidote - Travi$ Scott']
s28 = songs['Die A Happy Man - Thomas Rhett']
s29 = songs['How Deep Is Your Love - Calvin Harris']
s30 = songs['Where Ya At - Future feat Drake']

hello = []

rest_count = 1
def tick():
	global rest_count
	#ops = (add, sub)
	#randomizes + or -
	#op = random.choice(ops)
	#grabs a random song

	ransong = random.choice(songs.keys())
	rannum = random.randint(1,3)

	num = 0
	if rannum == 1:
		num = songs[ransong]
		print ransong
		print "stays same"
		print num
	elif rannum == 2:
		num = songs[ransong] + random.randint(1,5)
		print ransong
		print "add"
		print num
	elif rannum == 3:
		num = songs[ransong] - random.randint(1,5)
		print ransong
		print "minus"
		print num



	#rannum = op(songs[ransong], num)

	if num < 0:
		songs[ransong] = 0
	elif num >= 0:
		songs[ransong] = num

	time.sleep(1)
	os.system('cls')
	print rannum
	sortedx = sorted(songs.items(), key=operator.itemgetter(1))
	sortedd = sortedx.reverse()
	for i in sortedx:
		print i

	#for i in songs:
		#print i, songs[i]
	print rest_count
	rest_count = rest_count + 1
	return rest_count
def main():
	while rest_count < 7:
		tick()
		hello.append(str(songs["Hello - Adele"]))
		print hello
if __name__ == "__main__":
	main() 
