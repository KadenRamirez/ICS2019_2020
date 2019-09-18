"""
Author- Kaden Ramirez

This Program generates a game in which the computer
generates a number 1-100 and the player tries to guess
the number until they get it right.

"""
import random
def printN(n, goal):
	if n == goal: #TERMINATING CONDITION
		print("you won!")
		playAgain = input("Would you like to play again? If so type Y for yes. If not type any other character.")
		if playAgain == "Y":
			printN(int(input("The computer has generated a number from 1-100. Try and guess the number.")), random.randint(1,100))
		else:
			exit()
	elif n < goal and n >= 0:
		print("Your guess is too low. Try again.")
		printN(int(input("What's your new number?")), goal)
	elif n > goal and n <= 100:
		print("Your guess is too high. Try again.")
		printN(int(input("What's your new number?")), goal)
	else:
		print("Your guess is not between 1 and 100. Please pick again.")
		printN(int(input("What's your new number?")), goal)

printN(int(input("The computer has generated a number from 1-100. Try and guess the number.")), random.randint(1,100))
