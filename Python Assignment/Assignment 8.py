""" Exercise 8: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)

Remember the rules:
	- Rock beats scissors
	- Scissors beats paper
	- Paper beats rock
"""

first_player = input("Please enter from the following: Rock, Paper, or Scissors. Type quit when you want to exit the program.\n").strip().lower()
second_player = input("Please enter from the following: Rock, Paper, or Scissors. Type quit when you want to exit the program.\n").strip().lower()


def determineWinner(first_player, second_player):
	if first_player == "rock":
		if second_player == "rock":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nIt's a tie!")
		if second_player == "paper":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 2 wins!")
		if second_player == "scissors":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 1 wins!")
	elif first_player == "paper":
		if second_player == "rock":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 1 wins!")
		if second_player == "paper":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nIt's a tie!")
		if second_player == "scissors":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 2 wins!")
	elif first_player == "scissors":
		if second_player == "rock":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 2 wins!")
		if second_player == "paper":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nPlayer 1 wins!")
		if second_player == "rock":
			print("Player 1 has played " + first_player + "\nPlayer 2 has played " + second_player + "\nIt's a tie!")



while first_player != "quit" or second_player != "quit":
	determineWinner(first_player, second_player)


