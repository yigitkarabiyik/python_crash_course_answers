
file_path='C:/Users/yigit/OneDrive/Masaüstü/harry_potter_chamber_chapter1.txt'
file_name='harry_potter_chamber_chapter1'

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
		print("The file " + filename + "\nhas about " + str(num_words) +
			" words.\n")
		# count number of specific word 
		counts=contents.lower().count('')
		print(counts)
		# if you want it you can print whole content
		#print(contents)

count_words(file_path)
