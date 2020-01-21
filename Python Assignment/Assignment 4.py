""" Exercise 4: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor
of 26 because 26/13 has no remainder.)

Discussion
The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.

There is an easy way to programatically create lists of numbers in Python.

To create a list of numbers from 2 to 10, just use the following code:
	x = range(2, 11)

Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. Note that the second number in the range() function
is not included in the original list.

Now that x is a list of numbers, the same for loop can be used with the list:
	for elem in x:
		print elem
Will yield the result:
2
3
4
5
6
7
8
9
10
"""

def findDivisor(number):
	a = []
	for i in range(1, number + 1):
		if number % i == 0:
			a.append(i)
	return a


number = int(input("Please enter a number: "))

print(findDivisor(number))