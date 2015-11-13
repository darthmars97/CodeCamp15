import pygame, time, random
import operator
import os



songs = {
	'song1': 10,
	'song2': 10,
	'song3': 10,
	'song4': 10,
	'song5': 10,
	'song6': 10,
	'song7': 10,
	'song8': 10,
	'song9': 10,
}




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

