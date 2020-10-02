# writing on ean empty file
file_name = 'programming.txt'

with open(file_name, 'w') as file_object: # r w a
	file_object.write("I love programming.")
	
# writing multiple lines
with open(file_name, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
	
# appending to a file
with open(file_name, 'a') as file_object:
	file_object.write("I also love finding meanin in large dataset.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

