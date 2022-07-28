# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Christopher Buckminster
# Creation Date: 2022-07-28
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.)

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''
    while cave != '1' and cave != '2': # 1. Indentation error. Inconsistent use of tabs and spaces
	    print('Which cave will you go into? (1 or 2)') # 2. Indentation error. Inconsistent use of tabs and sapces
	    cave = input() # 3. Indentation error. Inconsistent use of tabs and spaces.

	return caves # 4. "Caves" is undefined. Typo for "cave"? Also, #5. Indentation error. Inconsistent use of tabs and spaces.

def checkCave(chosenCave): 
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2) # 6. This isn't a secure method for generating random numbers, but this isn't a security app, so I guess it's okay

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # 7. Missing parentheses

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # 8. Equals signs are missing here. 
	displayIntro()
	caveNumber = choosecave() # 9. "choosecave" is not defined. Should be "chooseCave"
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing") # 10. Typo here. Should read "Thanks for playing."

