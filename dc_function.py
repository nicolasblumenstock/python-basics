fullName = "Daniel Oliva"
age = 23

my_array = []
my_array.append(fullName)
my_array.append(age)
print(my_array)

def say_hello():
	print("Hello!")
say_hello()

splitName = fullName.split()
print (splitName)

def say_name():
	print("Hello, " + splitName[0] + "!")
say_name()

def my_age(year_born):
	print(2017 - year_born)
my_age(1991)

def some_odd_numbers():
	sum = 0
	for i in range(1, 5001, 2):
		sum += i
	return sum

print(some_odd_numbers())

# break example
i = 0
while 1: #this will run forever...
	i += 1
	print i
	if (i == 10):
		break
print "We broke out of the loop."

