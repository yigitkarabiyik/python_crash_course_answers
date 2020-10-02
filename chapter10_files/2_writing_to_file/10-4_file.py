filename = 'guest_book.txt'

with open(filename, 'a') as f:
	
	while True:
		name=input("What is your name bro? ")
		if name=='quit' or name=='q':
			break
		else:
			print("I am adding "+name.title()+" to guest_book file.\n")
			f.write(name+"\n")
				
			
