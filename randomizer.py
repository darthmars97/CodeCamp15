import pygame, time, random
import operator
import os



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
print songs[]



def tick():
	#ops = (add, sub)
	#randomizes + or -
	#op = random.choice(ops)
	#grabs a random song

	ransong = random.choice(songs.keys())
	rannum = random.randint(1,3)

	num = 0
	if rannum == 1:
		num = songs[ransong]
	elif rannum == 2:
		num = songs[ransong] + random.randint(1,5)
	elif rannum == 3:
		num = songs[ransong] - random.randint(1,5)




	#rannum = op(songs[ransong], num)
	
	if num < 0:
		songs[ransong] = 0
	elif num >= 0:
		songs[ransong] = num

	time.sleep(2)
	os.system('cls')
	print rannum
	sortedx = sorted(songs.items(), key=operator.itemgetter(1))
	sortedd = sortedx.reverse()
	for i in sortedx:
		print i

	#for i in songs:
		#print i, songs[i]	


while True:
	tick()

