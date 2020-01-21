# Exercise 1: Create a program that asks the user to enter their name and their age. Print out a message addressed to
# them that tells them the year that they will turn 100 years old.

# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous
# message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing
# the ENTER button")

# Create a Person Class
class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def changeAge(self, age):
		self.age = age

	def changeName(self, name):
		self.name = name

	def getAge():
		return age

	def getName():
		return name

	# Print the users name, age, and the year that they will turn 100
	def printUser(self, number):
		current_year = 2020
		year_user_turns_hundred = current_year + int(self.age)
		temp_number = int(number)

		for num in range(0, temp_number):
			print(self.name + " will turn 100 in year " + str(year_user_turns_hundred))

# Prompt the user to enter their name and age
def askUser():
	print("Please enter your name: ")
	name = input()
	print("Your name is " + name + "\n")

	print ("Please enter your age: ")
	age = input()
	print("Your age is " + age + "\n")

	person = Person(name, age)

	print("Please enter how many times you want the message to repeat")
	number = input()
	print("You entered number " + number + "\n")
	person.printUser(number)


person = askUser()