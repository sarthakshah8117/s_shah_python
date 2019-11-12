# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gamesshah

while gamesshah.player is False:
	# set player to True
	
	print("**********************************")
	print("Computer lives: ", gamesshah.computer_lives, "/", gamesshah.total_lives, "\n")
	print("Player lives: ", gamesshah.player_lives, "/", gamesshah.total_lives, "\n")
	print("Choose your weapon!\n")
	print("**********************************")

	
	print("**********************************")
	print("**********************************")
	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("gamesshah.computer chose ", gamesshah.computer, "\n")
	print("player chose ", player, "\n")
	
	print("**********************************")
	print("**********************************")

	if player == "quit":
		exit()
	elif gamesshah.computer == player:
		print("tie! no one wins, play again")

	elif player == "rock":
		if gamesshah.computer == "paper":
			print("You lose!", gamesshah.computer, "covers", gamesshah.player, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", gamesshah.player, "smashes", gamesshah.computer, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	elif player == "paper":
		if gamesshah.computer == "scissors":
			print("You lose!", gamesshah.computer, "cuts", player, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", gamesshah.player, "covers", gamesshah.computer, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	elif player == "scissors":
		if gamesshah.computer == "rock":
			print("You lose!", gamesshah.computer, "smashes", player, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", gamesshah.player, "cuts", gamesshah.computer, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	else:
		print("______________________________________________")
		print("That's not a valid choice, try again")
		print("______________________________________________")



	# handle all lives lost for player or AI
	if gamesshah.player_lives is 0:
		winlose.winorlose("lost")

	elif gamesshah.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gamesshah.player = False
		gamesshah.computer = gamesshah.choices[randint(0, 2)]	

