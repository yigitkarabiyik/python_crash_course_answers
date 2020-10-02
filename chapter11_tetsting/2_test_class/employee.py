
class Employee():
	
	def __init__(self,first_name,last_name,annual_salary):
		self.first=first_name
		self.last=last_name
		self.salary=annual_salary
		
	def give_raise(self,add_to_salary=5000):
		
		self.salary+= add_to_salary
		
		
