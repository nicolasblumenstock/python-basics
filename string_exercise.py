# name = "nicolas"
# new_name = ""
# cap_name = ""
# reverse_name = []
# print(name.upper())
# for letter in name:
# 	new_name += letter.upper()
# print (new_name)
# print (name.capitalize())
# for symbol in name:
# 	if (symbol == name[0]):
# 		cap_name += symbol.upper()
# 	else:
# 		cap_name += symbol
# print cap_name	
# # for character in name:
# # 	reverse_name += n
# for character in name:
# 	reverse_name.insert(0, character)
# print (''.join(reverse_name))

# paragraph = """This is a paragraph.
# There is a lot of info in it.
# Like this line here.
# This too."""

# replacements = [['A', '4'] , ['E', '3'] , ['G' , '6'] , ['I' , '1'] , ['O' , '0'] , ['S' , '5'] , ['T' , '7']]
# new_paragraph = paragraph.upper()
# for old, new in replacements:
# 	new_paragraph = new_paragraph.replace(old, new)
# print new_paragraph

# word = "cheese"
# # word = raw_input("Say a word, any word. ")
# # word_list = []
# # for i in word:
# # 	word_list.append(i)
# # # print word_list
# # len_word_list = len(word_list)
# # # print len_word_list
# # for j in range(0, len_word_list):
# # 	counter = 1
# # 	if (counter <= 5 and word_list[j] == word_list[j - 1]):
# # 		word_list.insert(j, word_list[j])
# # 		counter =+ 1
# # 	# else:
# # 	# 	counter = 1
# # print (''.join(word_list))

# # counter = 0
# # for ch in word:
# # 	if ch in 'aeiou' and counter < 1:
# # 		word = word.replace(ch, 'e' * 5)
# # 		counter += 1
# # print word

# # list() -> converts data type as a list
# # list_name = list(name)
# # print list_name

# a_string = "My name is Rob"
# new_string = ""
# for i in range(0, len(a_string)):
# 	last_index = len(a_string) - 1
# 	letter_stepping_backwards = last_index - i
# 	new_string += a_string[letter_stepping_backwards]
# print new_string

# leet_string = "Leet"
# leet_string_as_list = list(leet_string)
# for character in leet_string_as_list:
# 	if (character.upper() == "A"):
# 		leet_string_as_list.remove(character)
# 		leet_string_as_list.insert(character, "4")

# result = ""
# current = ""
# previous = ""

# string_to_test = "meet"

# for i in range(0, len(string_to_test)):
# 	current = string_to_test[i]
# 	if (current == previous):
# 		result = result + 4 * current
# 	else:
# 		result = result + current
# 	previous = current

# print result

def decrypt_function(encrypted_letter):
	try:
		number = encrypted_list.index(encrypted_letter)
	except ValueError:
		# do this!
		decrypted_message.append(encrypted_letter)
	else:
		decrypted_message.append(decrypted_list[number])


message = "lbh zhfg hayrnea jung lbh unir yrnearq!?"
decrypted = "abcdefghijklmnopqrstuvwxyz"
encrypted = "nopqrstuvwxyzabcdefghijklm"
message_list = list(message)
decrypted_list = list(decrypted)
encrypted_list = list(encrypted)
decrypted_message = []

for i in range(0, len(message_list)):
	decrypt_function(message_list[i])
print(''.join(decrypted_message))


