#### using json.dump() and json.load()
import json

### saving and reading user-genereted data
# reading
filename='username.json'

with open(filename) as f_obj:
	username=json.load(f_obj)
	print("Welcome back, "+username+"!")
