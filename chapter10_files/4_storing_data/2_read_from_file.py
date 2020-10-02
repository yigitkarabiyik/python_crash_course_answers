#### using json.dump() and json.load()
import json

#json.load() for read
filename='numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
