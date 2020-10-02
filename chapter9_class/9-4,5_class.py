#9-0
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
		
my_new_car=Car('volvo','xc40',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying an attribute's value directly
print("\nmofifying an atribute's value directly")

my_new_car=Car('volvo','xc40',2020)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=21
my_new_car.read_odometer()

#modifying an attribute's value through a method
print("\nmodifiying an attribute's value through a method")

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
		
	def update_odometer(self,mileage):
		"""Set the odometer reading to the given value"""
		self.odometer_reading=mileage

my_new_car=Car('volvo','xc40',2020)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(21)
my_new_car.read_odometer()

#incrementing an attribute's value through a method
print("\nincrementing an attribute's value through a method")
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

my_used_car=Car('ford','mustang',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(21200) #modify (equal to)
my_used_car.read_odometer()

my_used_car.increment_odometer(100) #increment (add to)
my_used_car.read_odometer()
print() 

#9-4
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

	
kipos=Restaurant('kipos','fish')
kipos.describe_restaurant()

kipos.number_served=8
kipos.show_served()

kipos.set_number_served(12)
kipos.show_served()

kipos.increment_number_served(12)
kipos.show_served()
print()

#9-5
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
			
hermonie=User('hermonie','granger',21,'female','london','wizard','single',
		'reading book')
		
hermonie.describe_user()
hermonie.increment_login_attempts()
hermonie.increment_login_attempts()
hermonie.increment_login_attempts()
hermonie.increment_login_attempts()
hermonie.increment_login_attempts()
hermonie.increment_login_attempts()

hermonie.show_login_attempts()

hermonie.reset_login_attempts()
hermonie.show_login_attempts()
