
file_name='python_learned_content.txt'

with open(file_name) as my_file:
	for line in my_file:
		print(line.replace('PYTHON','C').strip())
