
file_name= 'guest.txt'

guest_name=input("What is your name? ")

with open(file_name,'w') as file_object:
	file_object.write(guest_name)
