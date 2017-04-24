import os

phonebook_data = {"Melissa": "404-235-5428", "Joe": "404-235-2125", "Mike": "770-134-2229", "Igor": "770-233-3461"}

def getInteger():
	try:
		user_input = int(raw_input("Enter your selection: "))
		return user_input
	except ValueError:
		print "Invalid input. Please provide an integer.\n"
		return getInteger()
def lookup():
	who = raw_input("Who are you looking for? ")
	if not phonebook_data.has_key(who):
		print "%r is not in the Phonebook.\n" % who
	if who in phonebook_data:
		print "%r can be reached at " % (who) + phonebook_data[who] + "\n"
def new_entry(phonebook_data):
	new_name = raw_input("What is their name? ")
	new_number = raw_input("What is their number? ")
	phonebook_data[new_name] = new_number
	print "%s and %s are now in the phonebook.\n" % (new_name, phonebook_data[new_name])
def del_entry(phonebook_data):
	del_name = raw_input("Who do you want to delete? ")
	del phonebook_data[del_name]
	print ("%r has been deleted.\n" % del_name)
	print phonebook_data
def print_book(phonebook_data):
	for i in phonebook_data:
		print (i + " : " + phonebook_data[i])
def reverse_lookup(phonebook_data):
	number = raw_input("What number are you looking up? ")
	for i,j in phonebook_data.items():
		if j == number:
			print ("Found: " +  i + " : " + j + "\n")
	# print number

	
while 1:
	print """Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit\n"""

	# user_input = raw_input("What do you want to do (1 - 6)? ")
	# try:
	# 	convert_user = int(user_input)
	# except ValueError:
	# 	os.system("clear")
	# 	print "You must enter a number!\n"
	selection = getInteger()
	if (selection == 1):
		lookup()
	elif (selection == 2):
		new_entry(phonebook_data)
	elif (selection == 3):
		del_entry(phonebook_data)
	elif (selection == 4):
		print_book(phonebook_data)
	elif (selection == 5):
		reverse_lookup(phonebook_data)
	elif (selection == 6):
		print "Goodbye."
		break


