
import json

def get_stored_username():
	"""Get stored username if available"""
	filename='username.json'
	try:
		with open(filename) as f_obj:	# try to open username file
			username= json.load(f_obj)	# and store username
	except FileNotFoundError:
		# if there is not username file
		return None
	else:
		# if there is username file
		return username

def get_new_username():
	"""Prompt for a new user name."""
	username=input("What is your name?")
	filename='username.json'
	with open(filename,'w') as f_obj:	#creat file filename
		json.dump(username,f_obj)		#store username in the file
	return username
	

def greet_user():
	"""Greet the user by name."""
	username=get_stored_username() #look is there username file
	if username: # if there is
		print("Welcome back, "+username+"!")
	else: # if there is not
		username=get_new_username()
		print("We'll remember you when you come back, "+username+"!")
		
greet_user()
