# you should write while loop first
filename='programming_poll.txt'

with open(filename, 'a') as f:
	
	while True:
		
		name=input("What is your name bro? ")
		if name=='quit' or name=='q':
			break
		else:
			print("I am adding "+name.title()+" to guest_book file.")
			f.write(name+"\n")
			
			answer=input("Why you like programming?\n\t")
			if answer != 'q':
				f.write("\t"+answer+'\n')
				print("Thank you for your participation.\n")
			else:
				f.write("\t-\n")
				print()
