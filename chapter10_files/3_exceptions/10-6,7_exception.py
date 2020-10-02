
print("Enter two numbers for adding.")
print("When you press 0 it will stop.\n")

while True:
	try:
		number1=int(input("First number: "))
		if number1==0:
			break
		number2=int(input("Second number: "))
		if number2==0:
			break
		
	except ValueError:
		print("\nGive me a acceptable number.\n")
	else:
		print("Result: "+str(number1+number2)+"\n")
		
