
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
		print(contents+"\n")
		
for file in ['dogs.txt','cats.txt']:
	count_words(file)

