import random
secret_number = random.randint(1, 10)
number_of_guesses = 5
not_guessed = True
print "I'm thinking of a number between 1 and 10."
while not_guessed:
	print "You have %d guesses left." % number_of_guesses
	guessed_number = raw_input("What am I thinking of? ")
	guessed_num_int = int(guessed_number)
	if (guessed_num_int == secret_number):
		not_guessed = False;
		print "You guessed it!"
		play_again = raw_input("Do you want to play again? Y or N? ")
		if (play_again == "Y"):
			number_of_guesses = 5;
			not_guessed = True;
		if (play_again == "N"):
			print "See ya!"
	else: 
		if (guessed_num_int > secret_number):
			print "%r is too high. Try again." % guessed_num_int
			number_of_guesses -= 1;		
		if (guessed_num_int < secret_number):
			print "%r is too low. Try again." % guessed_num_int
			number_of_guesses -= 1;
		if (number_of_guesses == 0):
			print "Sorry. You ran out of guesses."
			not_guessed = False;
			if (number_of_guesses == 0):
				play_again = raw_input("Do you want to play again? Y or N? ")
				if (play_again == "Y"):
					number_of_guesses = 5;
					not_guessed = True;
				if (play_again == "N"):
					print "See ya!"

