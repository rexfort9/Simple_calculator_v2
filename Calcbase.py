from colorama import init
from colorama import Fore, Back, Style
# Use Colorama to make Termcolor work on Windows too
init()

# Request for a calculation
print(Fore.BLACK)
print(Back.GREEN)
what = input("What we're up to? (+,-,/,*):")

# Request for variables
print(Back.CYAN)
a = float(input("Print first variable: "))
b = float(input("Print second variable: "))

# Calculating actions & result output
if what == "+":
	c = a + b
	print(Fore.WHITE)
	print(Back.RED)
	print("The resolve is: " + str(c))

elif what == "-":
	c = a - b
	print(Fore.WHITE)
	print(Back.RED)
	print("The resolve is: " + str(c))

elif what == "/":
	c = a / b
	print(Fore.WHITE)
	print(Back.RED)
	print("The resolve is: " + str(c))

elif what == "*":
	c = a * b
	print(Fore.WHITE)
	print(Back.RED)
	print("The resolve is: " + str(c))

else:
	print("Invalid input...")
