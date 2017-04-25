class Person(object):
	def __init__(self,name,gender,cell):
		self.name = name
		self.gender = gender
		self.species = "Human"
		# self.number_of_arms = number_of_arms
		self.phone = {
			"cell": cell,
			"home": "Who has one anymore"
		}

	def greet(self, other_person):
		print "Hello %s, I am %s!" %(other_person, self.name)	

	def print_contact_info(self):
		if (self.phone['cell'] != ""):
			print "%s's number is %s" % (self.name, self.phone['cell'])

class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def print_info(self):
		print self.year, self.model, self.make
	def change_year(self, new_year):
		self.year = new_year
	def get_year(self):
		return self.year

marissa = Person("Marissa", "female", "770-777-7777")
print marissa.name, marissa.gender
print marissa.species
merilee = Person("Merilee", "female", "555-555-5555")
merilee.species = "Robot"
print merilee.species
# print merilee.number_of_arms
print merilee.phone['cell']
print marissa.phone['home']
marissa.greet("Bob")
merilee.print_contact_info()

david_cummings_car = Vehicle("Mcclaren", 'Mp4-12c', 2013)
david_cummings_car.print_info()
# david_cummings_car.change_year(2015)
david_cummings_car.year = 2015
david_cummings_car.print_info()
print david_cummings_car.get_year()
print david_cummings_car.year