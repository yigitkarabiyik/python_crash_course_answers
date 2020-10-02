
file_path='C:/Users/yigit/OneDrive/Masaüstü/python_crash_course/chapter10/python_learned_content.txt'
file_name='python_learned_content.txt'

# reading the entire file
with open(file_name) as my_file:
	content=my_file.read()
	print(content)

# reading looping over the file and then print
with open(file_name) as my_file:
	for line in my_file:
		print(line.strip())

# storing the lines in list and then print
with open(file_name) as my_file:
	list_of_lines=my_file.readlines()
	
for line in list_of_lines:
	print(line.strip())
