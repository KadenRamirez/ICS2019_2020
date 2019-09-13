import math
import sys
"""
Kaden Ramirez
This program combines all of the previous
java programs into a gaint python frankenprogram
"""
print("                 /\\\n                /__\\\n               /\\  /\\\n              /__\\/__\\")

try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])

	r1 = (-b + math.sqrt(b * b - 4*a*c))/ (2*a)
	r2 = (-b - math.sqrt(b * b - 4*a*c))/ (2*a)

	print("\nroot 1 is: " + str(r1) + "\nroot 2 is: " + str(r2))
except:
	print("\nYou must enter 3 real integers (not 0 for a).")

DAYS_TO_SECONDS = 24*60*60
SECONDS_TO_DAYS = 86400
SECONDS_TO_HOURS = 3600
SECONDS_TO_MINUTES = 60

daysIn = int(input("\nEnter a number of days: "))

secondsOut = daysIn * DAYS_TO_SECONDS

print("The number of seconds in that many days are: " + str(secondsOut))

secondsIn = int(input("\nEnter a number of seconds: "))

daysOut = secondsIn // SECONDS_TO_DAYS
hoursOut = secondsIn % SECONDS_TO_DAYS // SECONDS_TO_HOURS
minutesOut = secondsIn % SECONDS_TO_DAYS % SECONDS_TO_HOURS // SECONDS_TO_MINUTES
secondsRem = secondsIn % SECONDS_TO_DAYS % SECONDS_TO_HOURS % SECONDS_TO_MINUTES // 1

print("There are " + str(daysOut) + " days, " + str(hoursOut) + " hours, " + str(minutesOut) + " minutes, and a remainder of " + str(secondsRem) + " seconds in that many days/day")

