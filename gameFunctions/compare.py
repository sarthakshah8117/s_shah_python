
# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets 
from gameFunctions import winlose, gamesshah    
def comparechoices(comp,  play):	
	if play == "quit":
			exit()
	elif comp == play:
		print("tie! no one wins, play again") 

	elif play == "rock":
		if comp == "paper":
			print("You lose!", comp, "covers", play, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", play, "smashes", comp, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	elif play == "paper":
		if comp == "scissors":
			print("You lose!", comp, "cuts", play, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", play, "covers", comp, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	elif play == "scissors":
		if gamesshah.computer == "rock":
			print("You lose!", comp, "smashes", play, "\n")
			gamesshah.player_lives = gamesshah.player_lives - 1
		else:
			print("You win!", play, "cuts", comp, "\n")
			gamesshah.computer_lives = gamesshah.computer_lives - 1

	else:
		print("______________________________________________")
		print("That's not a valid choice, try again")
		print("______________________________________________")
