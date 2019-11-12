# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gamesshah, compare

while gamesshah.player is False:
	# set player to True
	
	print("**********************************")
	print("Computer lives: ", gamesshah.computer_lives, "/", gamesshah.total_lives, "\n")
	print("Player lives: ", gamesshah.player_lives, "/", gamesshah.total_lives, "\n")
	print("Choose your weapon!\n")
	print("**********************************")

	
	print("**********************************")
	print("**********************************")
	gamesshah.player = input("choose rock, paper or scissors: ")
	gamesshah.player = gamesshah.player.lower()

	print("gamesshah.computer chose ", gamesshah.computer, "\n")
	print("player chose ", gamesshah.player, "\n")
	
	print("**********************************")
	print("**********************************")

	### this is where you would call compare
	compare.comparechoices(gamesshah.computer, gamesshah.player)
	
	### end compare stuff


	# handle all lives lost for player or AI
	if gamesshah.player_lives is 0:
		winlose.winorlose("lost")

	elif gamesshah.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gamesshah.player = False
		gamesshah.computer = gamesshah.choices[randint(0, 2)]	

