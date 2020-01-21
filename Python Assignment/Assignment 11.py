""" Exercise 11: Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten
, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below."""

def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, "is not a prime number")
                print(i, "times", number)
                break
        else:
                print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


askUser = int(input("Please enter a number"))

isPrime(askUser)