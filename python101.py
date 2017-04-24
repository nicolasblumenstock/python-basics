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
# make_me_a_string = str(pi_the_magic_float) = "3.14"

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
# age = raw_input("How old are you? ")
# age_as_int = int(age)
# print type(age)
# if (age_as_int >= 21):
	# print "You can buy beer."
# elif (age_as_int >= 18):
	# print "A few more years."
# else: 
	# print "You are underage."

# import random
# random_number = random.randint(1, 10)
 
#  # loop - keep doing something until i tell you to stop

# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("Guess a number between 1 and 10. ")
# 	if (int(guess_a_number) == random_number):
# 		print "You guessed the number!";
# 		not_guessed = False;

# student1 = "Marissa"
# student2 = "Merilee"
# student3 = "Daniel"
# student4 = "Chris"

# print(student1,student2,student3,student4)

# list is a single variable with a bunch of numbered parts
# the number that an element is in, is called the "index"

students = [
	"Marissa",
	"Merilee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew"
	]
# print(students[1])
# print(students[3])
# print(students[7])
# print(students[-1]) <-- starts from the end

# atlantaTeams = [
# 	"Falcons",
# 	"Braves",
# 	"Hawks",
# 	"Thrashers"
# 	]

# # print(atlantaTeams)
# # To add an element to the end of a list, you can use the append method
# atlantaTeams.append("Atl United")
# # print (atlantaTeams)
# # to delete an index, you can use the remove method
# atlantaTeams.remove("Thrashers")
# pop removes the last item on the list
# atlantaTeams.pop()
# print (atlantaTeams)
# # print (atlantaTeams)
# # we can insert into any incidie with the insert method
# atlantaTeams.insert(0,"Tom Brady's Team")
# # print (atlantaTeams)

# teams_as_a_string = "Falcons,Braves,Hawks,Thrashers"
# teams_as_a_list = teams_as_a_string.split(",")
# print (teams_as_a_list)
# # atlantaTeams.sort();
# print (atlantaTeams)
# # sorted will sort but not change the list
# copy_of_atlanta_teams = sorted(atlantaTeams)
# print (copy_of_atlanta_teams)

# copy_of_atlanta_teams.reverse();
# print (copy_of_atlanta_teams)

# length_of_atlanta_teams = len(copy_of_atlanta_teams)
# print (length_of_atlanta_teams)
# print (copy_of_atlanta_teams[-1])
# print (copy_of_atlanta_teams[length_of_atlanta_teams-1])
# print (len(copy_of_atlanta_teams[0]))

# the other type of loop is a for loop

# for i in range(1, 10):
# 	print i
# For Loop format:
# 	[for] [what_you_want_to_call_the_thing_you_are_on] [in] [variable_looping_through]
# for student in students:
# 	# print student
# 	if (student == "Chris"):
# 		print "Welcome, Chris!"
# 	else:
# 		print "You are not, Chris."
# set up a for loop... but the range will be 0 to len-1
# students_length = len(students)
# for i in range(0,students_length):
	# print (students[i])
# for i in range(start, end, step):
# for i in range(0,10,2):
	# print i
# if you want a portion of a list, you can use the [x:y] format
# this will create a copy of the array, does not mutate or change the original
# it will start at the xth element, and will stop at the yth element
# print (students)
# second_and_third = students[1:3]
# print second_and_third
# print(students)
# all_but_the_first = students[1:]
# all_but_the_first = students[1:len(students)] is long form of previous line
# print all_but_the_first

# a funtion is a piece of code that can be called from the main body of the program,
 #the upshot is that if you have complicated code or code that is repeated often,
 # a function is your answer
 # repeating yourself is bad.
# a function in python is not a function, it is a definition.
# to declare a function in python, you use "def"
# fuctions always have ()

# def say_hello():
# 	print("Hello")

# say_hello()

# def say_hello_with_name(name):
# 	print("Hello, " + name)

# # say_hello_with_name() this will fail
# # say_hello_with_name("Rob","Chad") this will fail as well
# say_hello_with_name("Nick")
# # print name doesn't work because name in the function is a local variable
# def say_hello_with_default(name, in_class = "Yes"):
# 	print("Hello, " + name)
# 	print("Is student in class? " + in_class)
# say_hello_with_default("Carla")
# say_hello_with_default("Max", "No")

# # Functions always return something
# def return_user_name(name):
# 	return name
# print(return_user_name("YingRong"))

# def make_uppercase(string):
# 	return string.upper()

# normalized_string = [make_uppercase("Im a WilD and CrazY GUY")]
# normalized_string.append(make_uppercase("mE toO"))
# print normalized_string





# Tuples

# lists are awesome. but it's changeable. what if you
# you wanted something that wasn't changeable?
# a tuple is the same in all ways as a list, except;
# 1. it's values cannot be changed
# 2, it uses () instead of []
# 
# a_tuple_test = (1,5, 8)
# print a_tuple_test[1]
# a tuple test
# a_tuple_test[1] = 6

# dictionaries

# dictionaries are very simple objects.
# operate with a "key-value pair"
# name = "Rob"
# gender = "Male"
# height = "Tall"

person = {
	"name": "Rob",
	"gender": "Male",
	"height": "Tall"

}

print (person["height"])

zombie ={}

# can add key-values as needed
zombie['weapon'] = 'axe'
zombie['health'] = 100
zombie['startX'] = 10
zombie['startY'] = 20
zombie['speed'] = 10

print(zombie)

for key,value in zombie.items():
	print("Zombie has a key of %s with a value of %s" % (key, value))
	print (zombie[key])
if (zombie['speed'] <= 5):
	zombie['position'] = zombie['startX'] + 5
elif(zombie['speed'] <10):
	zombie['position'] = zombie['startX'] + 10
else:
	zombie['position'] = zombie['startX'] + 15

zombie['pointless'] = "Why?"
del zombie['pointless']
print zombie

player_push = "up"
if(player_push == "up"):
	direction = "startY"
else:
	direction = "startX"
zombie[direction] += 10

zombies = []
zombies.append(
	{
		'speed': 10,
		'weapon': 'fist',
		'name': 'Hank'
	}
)
zombies.append({
	'speed': 5,
	'weapon': 'baseball bat',
	'name': 'Bruiser'
	})

# get the second zombies speed...

print (zombies[1]['speed'])

zombies[1]['victims'] = [
	"Jane",
	"Mike",
	"Bob"
]

print(zombies[1]['victims'][2])












