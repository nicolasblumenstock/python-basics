# for i in range(1, 11):
# 	print i

# num1 = raw_input("Start from: ")
# num2 = raw_input("End on: ")
# for j in range(int(num1), int(num2) + 1):
# 	print j
# for i in range(1, 11):
	# if (i % 2 == 1):
		# print i

# size = 5
# for i in range(size):
# 	print ('*' * size)

# size = raw_input("How big is the square? ")
# for i in range(int(size)):
# 	print ('*' * int(size))

# width = raw_input('width? ')
# height = raw_input('height? ')
# int_width = int(width)
# int_height = int(height)

# for i in range(int_height):
# 	if (i == 0 or i == int_height - 1):
# 		print('*' * int_width)
# 	else:
# 		print('*' + (" " * (int_width - 2)) + '*')
height = 4
for i in range(0, height):
		print ((' ' * (height - i) + ('*' * ((height / height) + i)) + (' ' * (height - i))))