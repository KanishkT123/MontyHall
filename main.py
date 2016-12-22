import random

def game(start, alldoor, switch, number):
	print "Playing " + str(number) + " times"
	#All the doors
	choices = ["A","B","C"]
	wins = 0
	#All the iterations
	for i in range(0,number):
		#Pick where the goat goes
		goat = random.choice(choices)
		#If the starting choice door was given:
		if start == 'y':
			chosen = alldoor
		else:
			chosen = random.choice(choices)

		#Find the unused doors (i.e., not chosen and not goat)
		unused = [x for x in choices if x != chosen]

		if chosen != goat:
			possible = goat
		else:
			possible = random.choice(unused)			

		if switch == "SW":
			chosen = possible
		if switch == "R":
			if random.choice([True, False]):
				chosen = possible

		if chosen == goat:
			wins += 1
	print "You won: " + str(wins) + " Times"


def main():
	start = raw_input("Any choice at the start? (y/n) ").lower()
	alldoor = 'X'
	if start == 'y':
		alldoor = raw_input("What is your choice? (A/B/C) ")
	switch = raw_input("Will you switch, stay, or have it be random? (SW/ST/R) ")
	number = int(raw_input("How many times are we going to run this trial? I need a number! "))
	game(start, alldoor, switch, number)

if __name__ == '__main__':
	main()
