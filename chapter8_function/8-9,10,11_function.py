#8-0
def greet_users(names):

	for name in names:
		msg="Hello, "+name.title()+"!"
		print(msg)
	
usernames=['ron','hermonie','harry']

greet_users(usernames)
print()
#8-0
def print_models(unprinted_designs,completed_models):
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		
		print("Printing model: "+current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models) 
# print_models(unprinted_designs[:], completed_models) for sending the copy of unprint...

show_completed_models(completed_models)

print("\n#8-9\n")
#8-9
def show_magicians(magician_list):
	for magician in magician_list:
		print(magician.title())

magician_names=['ron','hermonie','harry']

show_magicians(magician_names)
print("\n#8-10\n")

#8-10
def make_great(magician_list):
	current_magician=[]
	while magician_list:
		line='Great to '+magician_list.pop()
		current_magician.append(line)
	magician_list[:]=current_magician[:]

make_great(magician_names)
show_magicians(magician_names)
print("\n#8-11\n")

#8-11
magician_names=['ron','hermonie','harry']

def make_great(magician_list,greated_list):
	while magician_list:
		greated_list.append('Great to '+magician_list.pop())

new_list=[]
make_great(magician_names[:],new_list)
show_magicians(magician_names)
print()
show_magicians(new_list)



