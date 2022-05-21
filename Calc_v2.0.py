from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print(Fore.WHITE)
print(Back.CYAN)
print("Inputting '0' instead of calculation will close the app.")

while True:

	print(Fore.BLACK)
	print(Back.GREEN)


	what = input("What we're up to? (+,-,/,*):")
	if what == "0":	
		print(Fore.RED)
		print(Back.WHITE)
		print("Thanks for using my soft!")
		exit()
	if what not in ('+','-','*','/','0'):
		print(Fore.WHITE)
		print(Back.RED)
		print("Please, enter the correct command!""\nIt might be calculation sign(+,-,/,*) or quit key(0)")
	if what in ('+','-','*','/'):
		print(Back.CYAN)
		a = float(input("Print first variable: "))
		b = float(input("Print second variable: "))

		if what == "+":
			c = a + b
			print(Fore.WHITE)
			print(Back.RED)
			print(f"The resolve is: {c}")

		elif what == "-":
			c = a - b
			print(Fore.WHITE)
			print(Back.RED)
			print(f"The resolve is: {c}")

		elif what == "*":
			c = a * b
			print(Fore.WHITE)
			print(Back.RED)
			print(f"The resolve is: {c}")	

		elif what == "/":
			if b !=0:
				c = a / b
				print(Fore.WHITE)
				print(Back.RED)
				print(f"The resolve is: {c}")
			else:
				print(Fore.RED)
				print(Back.BLACK)
				print("Dividing by Zero is undefined.")
		
		else:
			print(Fore.WHITE)
			print(Back.RED)
			print("Invalid input...")
			break
