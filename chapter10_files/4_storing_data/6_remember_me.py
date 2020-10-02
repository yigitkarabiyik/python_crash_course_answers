
import json

def greet_user():
	"""Greet the user by name."""
	filename='username.json'
	try:
		#try to open file having user name
		with open(filename) as f_obj:
			username=json.load(f_obj)
				
	except FileNotFoundError:
		# if there is not file having username
		# creat file and request username
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, "+username+"!")
	
	else:
		# if there is a file having username
		# say welcome bak
		print("Welcome back, "+username+"!")

# call function for gereet the user by name	
greet_user()
