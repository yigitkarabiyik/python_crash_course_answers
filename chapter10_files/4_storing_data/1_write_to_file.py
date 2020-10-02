#### using json.dump() and json.load()
import json

#json.dump() for write
numbers=[2,3,5,11,13]
filename='numbers.json'

with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)
