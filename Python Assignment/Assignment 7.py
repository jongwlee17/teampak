""" Exercise 7: Let's say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line
of Python that takes this list a and makes a new list that has only the even elements of this list in it.

Discussion

Concepts for this week:
- List comprehensions

List Comprehensions
The idea of a list comprehension is to make code more compact to accomplish tasks involving lists. Take for example this code:
	years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
	ages = []
	for year in years_of_birth:
		ages.append(2014 - year)
And at the end, variable ages has the list [24, 23, 24, 24, 22, 23]. What this code did was translate the years of birth
into ages, and it took us a for loop and an append statement to a new list to do that.

Compare to this piece of code:
	years_of_birth = [1990, 1991, 1990, 1992, 1991]