# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# 1. If the number is a multiple of 4, print out a different message
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
# evenly into num, tell that to the user. If not, print a different appropriate message.

def oddOrEven(number, check):
	dividebyTwo = 2

	if int(number) % int(check) == 0:
		print (number + " is divisible by " + check + " thus being even")
	elif int(number) % dividebyTwo == 0:
		print(number + " is divisible by " + str(dividebyTwo) + " thus being even")
	else:
		print(number + " is odd")

# another way to input for number
# number = int(input(give me a number to check: "))
# check = int(input("give me a number to divide by: "))

print("Please enter the number ")
number = input()
print("\n")

print("Please enter the number to check with ")
check = input()
print("\n")

oddOrEven(number, check)