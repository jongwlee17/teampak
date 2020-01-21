""" Exercise 6: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
that reads the same forwards and backwards)
"""

def palinedromeChecker(word):
	reverseWord = word[-1::-1].lower()
	
	if word == "":
		print("No word has been entered, please enter a word")
		askUser()
	if reverseWord == word.lower():
		print("The word " + word + " is a palindrome.")
	else:
		print("The word " + word + " is not a palindrome.")


def askUser():
	user_input = input("Please enter a word to check if it is a palindrome\n")
	palinedromeChecker(user_input)


askUser()