import random

UpperCase = 'No'
LowerCase = 'No'
Symbols = 'No'
Numbers = 'No'
Char = 'No'
Dependencies = [UpperCase, LowerCase, Symbols, Numbers, Char]
SymbolsL = ['!', '@', '#', '$', '%', '^', '&', '*']
LowerCaseL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UpperCaseL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', "S", "T", "U","V", "W", "X", "Y", "Z"]
CurrentOBJ = None
Password = ' '

def start():
	print('How long do you want the password to be?')
	Char = int(input())
	print('UpperCase Letters? (Yes/No)')
	UpperCase = input()
	print('Lowercase Letters?(Yes/No)')
	LowerCase = input()
	print('Symbols? (Yes/No)')
	Symbols = input()
	print('Numbers? (Yes/No)')
	Numbers = input()
	Dependencies = [UpperCase, LowerCase, Symbols, Numbers, Char]
	for i in range(len(Dependencies)):
		print(Dependencies)
	print('..')
	print('..')
	make()
def make():
	for i in range(Char):
		randop = random.randrange(1,4)
		if randop == 1:
			

start()

