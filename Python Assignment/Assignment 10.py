""" This week's exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works won two lists of different sizes. Write this using at least one list comprehension.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def findCommon(list_a, list_b):
    final_list = [a for a in set(list_a) for b in list_b if a == b]

    return final_list

print(findCommon(a, b))