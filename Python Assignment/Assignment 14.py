""" Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
minus all the duplicates.

Extras:
* Write two different functions to do this - one using a loop and constructing a list, and another using sets.
* Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""



# Returning set with no duplicates
def set_with_no_duplicates(numbers):
    new_list = set()

    for x in numbers:
        new_list.add(x)

    return new_list


# Returning list with no duplicates
def list_with_no_duplicates(numbers):
    y = []

    for i in numbers:
        if i not in y:
            y.append(i)
    return y



numbers = [0, 1, 1, 2, 3, 10, 22, 22, 2, 10, 55, 100, 55]


print(set_with_no_duplicates(numbers))

print(list_with_no_duplicates(numbers))