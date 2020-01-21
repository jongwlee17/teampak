""" Exercise 5: Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# random_a = range(1, random.randint(1,30))
# random_b = range(1, random.randint(1,40))

print("Random_a list consists of: ", random_a)
print("Random_b list consists of: ", random_b)


def findCommonValues(a, b):
	final_list = []

	for num in a:
		if num in b:
			if num not in final_list:
				final_list.append(num)
	return final_list


print(findCommonValues(a, b))