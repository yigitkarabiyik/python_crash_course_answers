#10-0 reading entire file
file_path='C:/Users/yigit/OneDrive/Masaüstü/pi_digits.txt'

with open(file_path) as file_object:
	contents= file_object.read()
	print(contents)


#10-0 reading line by line
with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip()) #rstrip bec. of empyt lines

#10-0 making a list of lines from file
with open(file_path) as file_object:
	lines=file_object.readlines()

for line in lines:
	print(line.rstrip())
print()

# working with a file's content
with open(file_path) as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print()

# large files: one million digits 
file_path2='C:/Users/yigit/OneDrive/Masaüstü/pi00.txt'

with open(file_path2) as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string +=line.strip()

print(pi_string[:52]+"...")
print(len(pi_string))

# is your birthday contained in pi
pi_string=''
for line in lines:
	pi_string+=line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
