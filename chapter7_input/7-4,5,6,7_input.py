
#7-0 while
prompt="\nTell me something and I will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program. "

message=""
while message!='quit':
	message=input(prompt)
	if message!='quit':
		print(message)
#7-0 flag
active=True
while active:
	message=input(prompt)
	
	if message == 'quit':
		active=False
	else:
		print(message)

#7-0 break
prompt="\nEnter the name of city you have visited."
prompt+="\n(Enter quit when you are finished.)"

while True:
	city=input(prompt)
	
	if city=='quit':
		break
	else:
		print("I'd love to go to "+city.title()+"!")

#7-0 continue
current_number=0
while current_number<10:
	current_number+=1
	if current_number%2==0:
		continue
	
	print(current_number)

#7-4

print("\nEnter a series of pizza toppings until you enter a 'quit' value.")
topping=""
while topping!='quit':
	topping=input("You'll add that topping to your pizza. ")

#7-5
person=int(input("\nEnter your age: "))
if person<3:
	print("Your movie ticket is free")
elif person<12:
	print("Your movie ticket is $10")
else:
	print("Yout movie ticket is $15")
	
#7-6

active=True
while active:
	if person<3:
		print("Your movie ticket is free")
		break
	elif person<12:
		print("Your movie ticket is $10")
		active=False
	else:
		print("Yout movie ticket is $15")
		break

#7-7
x=0
while x!=5:
	print(x)
