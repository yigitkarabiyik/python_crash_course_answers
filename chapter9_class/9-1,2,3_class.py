#9-0
class Dog():
	"""A simple attempt to model a dog."""
	def __init__(self,name,age):
		"""Initialize name and age attributes."""
		self.name=name
		self.age=age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title()+" is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title()+" rolled over!")

my_dog= Dog('frang',6)
your_dog=Dog('lucy',4)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old")
my_dog.sit()

print("\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old")
your_dog.roll_over()
print()
#9-1
class Restaurant():
	""""""
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.cuisine=cuisine_type
		
	def describe_restaurant(self):
		print("The "+self.name.title()+" restaurant is "+self.cuisine+" cuisine.")
	
	def open_restaurant(self):
		print("The "+self.name.title()+" is open now.")
		
near_restaurant=Restaurant('sushico','chinese')
near_restaurant.describe_restaurant()
near_restaurant.open_restaurant()
print()
#9-2
kipos=Restaurant('kipos','fish')
epic=Restaurant('epic burger','burger')
nusret=Restaurant('nusr-et','meat')

kipos.describe_restaurant()
print()
epic.describe_restaurant()
print()
nusret.describe_restaurant()
print()

#9-3
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
		
		def describe_user(self):
			print(self.name.title()+" "+self.last.title()+" is a "
				+str(self.age)+" years old " +self.gender
				+" lives in "+self.city.title()
				+"\nwork as "+self.job
				+" in "+self.single
				+" and has fun "+self.hobby)
	
		def greet_user(self):
			print("Nice to meet you "+self.name+" "+self.last)
		
		
harry=User('harry','potter',21,'male','hogsmeade','wizard','relationship',
		'fighting with voldemort')

harry.describe_user()
print()
hermonie=User('hermonie','granger',21,'female','london','wizard','single',
		'reading book')

hermonie.describe_user()
