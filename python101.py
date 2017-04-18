# print "Hello, World!"
# print two different things on the same line
# print ("Hello, World", "Again")

# this is won't work.
# print "This 
# is a couple lines of a sentence.
 # Please Print."

# This will for multiple lines.
# print """This
# will ignore the new lines
# until it sees another
# three double quotes"""


# Variables  - string, number, letters, anything that can be made with a keyboard
# and you want to stash not fast into something that is fast
# there is no declaration. 
# JS ex/ var name = Shane;
# in python/ name = "Shane"
# python not heavily typed like C#

# name = "Robert " + "Bunch"
# first_name = "Robert";
# last_name = "Bunch";
# full_name = first_name + last_name
# print full_name

# Arithmatic
# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2
# print the_meaning_of_life % 5
# returns 8 because both are integers
# print the_meaning_of_life / 5
# print int(30.5 / 5.2)
# print 4 + "Joe"
# print 4 * "Joe"

# data types (variable types)
# - Strings - English type stuff for people
# - numbers - something with digits and stuff that goes with digits (. -)
# --- Floats (decimals), Integers 
# - Booleans - True or False, Yes or No, On or Off
 # - lists - list of variables in one variable
 # - dictionary 0 variables of variables
 # - object - deal with it later

# Strings
# first_name = "Rob"
# last_name = "Bunch"
# print "Hello, {} {}!".format(first_name, last_name)
# print "Hello " + first_name + " " + last_name
# placeholders
# print "Hello, %s %s!" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

# floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer

# booleans - true or false
# the_truth = True
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
# first_name = raw_input("First Name: ")
# print first_name
# last_name = raw_input("Last Name: ")

# conditionals
# 1 = means you want to assign something on the left to the thing on the right
# 2 = means you want to compare what's on the left with what's on the right
# if you want to compare = or greater than, >=
# if (first_name == last_name):
	# print "Your first name is the same as your last name?"
age = raw_input("How old are you? ")
age_as_int = int(age)
# print type(age)
if (age_as_int >= 21):
	print "You can buy beer."
