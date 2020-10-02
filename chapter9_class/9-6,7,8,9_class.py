#9-0 inheritance
class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
	
	def read_odometer(self):
		"""Showing the car's mileage."""
		print("This car has "+str(self.odometer_reading)+" miles on it.")
		
	def update_odometer(self,mileage): #modify
		"""Set the odometer reading to the given value."""
		self.odometer_reading=mileage
	
	def increment_odometer(self,miles): #increment
		"""Add the given amount to the odometer reading."""
		self.odometer_reading+=miles
	
	
	
	
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self,make,model,year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make,model,year)
		self.battery_size=70
	
	def describe_battery(self):
		"""Desctibing the battery size."""
		print("This car has a "+str(self.battery_size)+" -kWh battery.")
	def fill_gas_tank(self):
		print("This car doesn\'t need gas tank.")
		


		
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.fill_gas_tank()
print()
### inheritance in Python 2.7 ###
#super(ElectricCar,self).__init__(make,model,year)

#9-0
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		"""Initilize the battery's attributes."""
		self.battery_size=battery_size
		
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+" -kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size==70:
			range =240
		elif self.battery_size==85:
			range=270
		
		message="This car can go approximately "+ str(range)
		message+=" miles on a full charge."
		print(message)
		
class ElectricCar(Car):
	"""Represent aspect of a car, specific to electric vehicles."""
	def __init__(self,make,model,year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make,model,year)
		self.battery=Battery()

my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
print()

#9-6
class Restaurant():
	""""""
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.cuisine=cuisine_type
		self.number_served=0
		
	def describe_restaurant(self):
		print("The "+self.name.title()+" is "+self.cuisine+" cuisine restaurant.")
	
	def open_restaurant(self):
		print("The "+self.name.title()+" is open now.")
	
	def show_served(self):
		print("The "+self.name.title()+" has "+str(self.number_served)
		+" customers.")

	def set_number_served(self,customers):
		self.number_served=customers
		
	def increment_number_served(self,new_customers):
		self.number_served+=new_customers

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['choocolate','vanilla','strawberry','caramel','blueberry']
	
	def display_flavors(self):
		print("We have:")
		for flavor in self.flavors:
			print(flavor.title())
			
kemal_usta=IceCreamStand('kemal_usta','ice_cream')
kemal_usta.display_flavors()
print()

#9-7
class User():
		
	def __init__(self,first_name,last_name,age,gender,living_city,job,
			single_or_relationship,best_hobby):
			
			
		self.name=first_name
		self.last=last_name
		self.age=age
		self.gender=gender
		self.city=living_city
		self.job=job
		self.single=single_or_relationship
		self.hobby=best_hobby
		self.login_attempts=0
		
	def describe_user(self):
		print(self.name.title()+" "+self.last.title()+" is a "
			+str(self.age)+" years old " +self.gender
			+" lives in "+self.city.title()
			+"\nwork as "+self.job
			+" in "+self.single
			+" and has fun "+self.hobby+".\n")
	
	def greet_user(self):
		print("Nice to meet you "+self.name+" "+self.last)
			
	def increment_login_attempts(self):
		self.login_attempts+=1
			
	def reset_login_attempts(self):
		self.login_attempts=0
			
	def show_login_attempts(self):
		print(self.name.title()+" attempted to login "
			+str(self.login_attempts)+
			" times.")
				
class Admin(User):
	def __init__(self,first_name,last_name,age,gender,living_city,job,
			single_or_relationship,best_hobby):
		super().__init__(first_name,last_name,age,gender,living_city,job,
			single_or_relationship,best_hobby)
			
		self.privileges=['can delete post','can ban user','can add post']
	
	def show_privileges(self):
		print(self.privileges)
		
harry=Admin('harry','potter',21,'male','hangmeade','wizard',
		'single','fight with voldemort')
harry.show_privileges()
print()

#9-8

class Privileges():

	def __init__(self,privileges=['can delete post','can ban user','can add post']):
		self.privileges=privileges
	
	def show_privileges(self):
		print(self.privileges)
		

class Admin(User):
	def __init__(self,first_name,last_name,age,gender,living_city,job,
			single_or_relationship,best_hobby):
		super().__init__(first_name,last_name,age,gender,living_city,job,
			single_or_relationship,best_hobby)
			
		self.privileges=Privileges()
	

harry=Admin('harry','potter',21,'male','hangmeade','wizard',
		'single','fight with voldemort')

harry.privileges.show_privileges()

#9-9

class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initilize the battery's attributes."""
		self.battery_size=battery_size
		
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+" -kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size==70:
			range =240
		elif self.battery_size==85:
			range=270
		
		message="This car can go approximately "+ str(range)
		message+=" miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		if self.battery_size==70:
			self.battery_size=85
		else:
			print("The battery size already upgraded.")
			

my_tesla=ElectricCar('tesla','model x',2018)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
