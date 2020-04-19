"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Michele
Then I would see the string:

Michele is name My

shown back to me.
"""


def reverseString(word_to_reverse):
    x = word_to_reverse.split()
    print("The split string is: ", x)
    result = []

    for word in x:
        result.insert(0, word)

    return " ".join(result)



def reverse_v2(x):
    y = x.split()
    return " ".join(y[::-1])





user_answer = input("Please enter a string containing multiple words.\n")
print(reverseString(user_answer))