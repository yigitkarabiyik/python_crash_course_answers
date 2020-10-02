
###hangling the ZeroDevisionError exception

# solution: using try-except blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# solution: the else block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
	
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't dvide by 0!")
	else:
		print(answer)

# solution: handling the FilenotFoundError exception
filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) 
	+ " words.")
	
# solution: for working with multiple files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#pass insted of print msg
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# Count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) +
			" words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
