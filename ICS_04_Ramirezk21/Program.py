import math, turtle

def drawShape():
	n = 6
	N_TO_SHAPE = (n-2)*180/n
	N_TO_INSIDE = 180 - N_TO_SHAPE
	#all functions at top
	bob = turtle.Turtle()
	#tell the turtle what to do
	while n > 0:
		bob.forward(50)
		bob.left(N_TO_INSIDE)
		n = n - 1

	screen = bob.getscreen()
	screen.mainloop()

	screen = bob.getscreen()
	screen.mainloop()
	
def fahrenheitToCelsius():
	f = 32
	F_TO_C = (f-32) * (5/9)
	print( str(f) + " degrees fahrenheit is " + str(F_TO_C) + " degrees Celsius.")

def acresToBarns():
	a = 7
	A_TO_B = a * 4.047
	print(str(a) + " acre/acres equals " + str(A_TO_B) + " * e+31 " + " barns.")

fahrenheitToCelsius()
acresToBarns()
drawShape()
