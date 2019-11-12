from random import randint
# set up some variables for player and AI lives
player_lives = 1
computer_lives = 1
total_lives = 1

# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices (0, 1 or 2)
computer = choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False