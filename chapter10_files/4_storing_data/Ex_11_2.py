
import json

filename='favorite_number.json'

with open(filename) as f_obj:
	file_inside=json.load(f_obj)
	
print("I know your favorite number is "+file_inside+".")
