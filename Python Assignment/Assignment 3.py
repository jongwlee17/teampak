# Exercise 3
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
# it and print out this new list
# 2. Write this in one line of Python
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than
# that number given by the user

a = [1, 1 ,2, 3, 5, 8, 13, 21, 34, 55, 89]

def lessThanNumber(numbers, check):
	b = []
	for i in numbers:
		if i < check:
			b.append(i)
	print(b)


check = int(input("Please enter the number to check the list with: "))
""" print([aa for aa in a if aa < 5]), A list comprehension behaves like this: [output] for [item] in [list] if [filter]
As you can see there are 4 components in its syntax: output, item, list and filter.
In this case
output = aa
item = aa
list = a
filter = aa < 5

What this means is that I'm outputting the variable 'aa' which refers to each item in the list (a).
Since 'aa' is set to refer to each item in list(a), the output will print the items in list(a). However, I also have a filter
specified at the end of the code "if aa < 5"

This means that only the items in the list (referred to as aa) that are below 5 are printed out.
"""

lessThanNumber(a, check)