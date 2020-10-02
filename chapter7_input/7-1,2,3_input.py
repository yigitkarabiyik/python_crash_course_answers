#7-0

number=int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number%2==0:
	print("\nThe number "+str(number)+" is even.")
else:
	print("\nThe number "+str(number)+" is odd.")
print("")

#7-1
car=input("What kind of rental car you would like. ")
print("\nLet me see if I can find you a "+car.title()+".")

#7-2
people=int(input("\nHow many people are in their dinner group. "))

if people>8:
	print("You'll have to wait for table.")
else:
	print("Your table is ready.")

#7-3
number=int(input("\nEnter a number, and I'wll tell you whether the number "
+"is a multiple of 10 or not. "))

if number%10==0:
	print("The number is a multiple of 10")
else:
	print("The number is not a multiple of 10")
