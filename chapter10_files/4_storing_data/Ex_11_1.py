
import json

filename='favorite_number.json'

favorite_number=input("What is your favorite number? ")
with open(filename,'w') as f_obj:
	json.dump(favorite_number, f_obj)


#input for favorite number
#store the number to file

