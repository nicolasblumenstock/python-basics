# Exercise 1
phonebook_dict = {
	'Alice': '703-493-1834',
	'Bob': '857-384-1234',
	'Elizabeth': '484-584-2923'

}

print phonebook_dict['Elizabeth']
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict

# Exercise 2
ramit = {
	'name': 'Ramit',
	'email': 'ramit@gmail.com',
	'interests': ['movies', 'tennis'],
	'friends':[
		{
			'name': 'Jasmine',
			'email': 'jasmine@yahoo.com',
			'interests': ['photography', 'tennis']

		},
		{
			'name': 'Jan',
			'email': 'jan@hotmail.com',
			'interests': ['movies', 'tv']
		}
	]
}

print ramit['email']
ramit_email = ramit['email']
print ramit_email
ramit_first_interest = ramit['interests'][0]
print ramit_first_interest
jasmine_email = ramit['friends'][0]['email']
print jasmine_email
jan_second_interest = ramit['friends'][1]['interests'][1]
print jan_second_interest

# Letter Summary
def letter_histogram(word):

	letter_summary = {}
	
	for characters in word:
		if characters in letter_summary:
			letter_summary[characters] += 1
		else:
			letter_summary[characters] = 1

		
	print letter_summary

letter_histogram("pizza")

# word summary
def word_histogram(paragraph):
	word_list = paragraph.split(' ')
	word_summary = {}
	for piece in word_list:
		if piece in word_summary:
			word_summary[piece] +=1
		else:
			word_summary[piece] = 1
	print word_summary

word_histogram('to be or not to be. that is the question')

# bonus
def best_words(runon):
	runon_list = runon.split(' ')
	runon_summary = {}
	for i in runon_list:
		if i in runon_summary:
			runon_summary[i] += 1
		else:
			runon_summary[i] = 1
	
	presort_runon = []
	
	for j in runon_summary:
		presort_runon.append([runon_summary[j], j])
	
	# print presort_runon

	sorted_runon = sorted(presort_runon)

	# print ("Gold Medal Count: '%s' With %d uses." % (sorted_runon[-1][1], sorted_runon[-1][0]))
	# print ("Silver Medal Count: '%s' With %d uses." % (sorted_runon[-2][1], sorted_runon[-2][0]))
	# print ("Bronze Medal Count: '%s' With %d uses." % (sorted_runon[-3][1], sorted_runon[-3][0]))
	print sorted_runon[:-4:-1]



best_words("the is a dog the is a dog the is a cat the is bird the meh")




# -------Super Bonus
listFellah = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
def make_final_dictionary(list):
  final_dictionary = {
    "one": [],
    "two": [],
    "three": [],
    "four": [],
    "five": [],
    "six": []
  }
  items_dictionary = {}
  for item in list:
    item = str(item)
    if item in items_dictionary:
      items_dictionary[item] += 1
    else:
      items_dictionary[item] = 1
  for organized_item in items_dictionary:
    if (items_dictionary[organized_item] == 1):
      final_dictionary["one"].append(organized_item)
    elif (items_dictionary[organized_item] == 2):
      final_dictionary["two"].append(organized_item)
    elif (items_dictionary[organized_item] == 3):
      final_dictionary["three"].append(organized_item)
    elif (items_dictionary[organized_item] == 4):
      final_dictionary["four"].append(organized_item)
    elif (items_dictionary[organized_item] == 5):
      final_dictionary["five"].append(organized_item)
    elif (items_dictionary[organized_item] == 6):
      final_dictionary["six"].append(organized_item)
  print final_dictionary

make_final_dictionary(listFellah)

