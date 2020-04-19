""" Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function."""


def first_last_elements(numbers):
    return [numbers[0], numbers[len(numbers) - 1]]


numbers = [0, 1, 2, 3, 4, 5]

print(first_last_elements(numbers))