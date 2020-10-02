#8-0 keyword arquments

def describe_pet(animal_type,pet_name):
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title())

describe_pet(animal_type='hamster',pet_name='scabbers')
describe_pet(pet_name='scabbers',animal_type='hamster')

#8-0 default values

def describe_pet(pet_name,animal_type='dog'):
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title())

	#A dog named fang.
describe_pet('willie')
describe_pet(pet_name='willie')
	#A cat named crookshanks
describe_pet('crookshanks', 'cat')
describe_pet(pet_name='crooksharks', animal_type='cat')
describe_pet(animal_type='cat', pet_name='crooksharks')

#8-3
def make_shirt(size):
	print("\nThe size of the shirt is "+size+".")
	
make_shirt("large")
make_shirt(size="small")

#8-4
def make_shirt(size="large",message="I love Python"):
	print("\nThe size of the "+message.title()+" shirt"+" is "+size+".")

make_shirt()
make_shirt("medium","harry potter")
print()	
	
#8-5
def describe_city(name="vancouver",country="canada"):
	print(name.title()+" is in "+country.title()+".")
	
describe_city()
describe_city("toronta")
describe_city("los angles","america")
