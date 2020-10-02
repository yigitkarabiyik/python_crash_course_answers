#5-8
usernames=["admin","lilly","james","dumbledore","mcgonagall"]
username=usernames[3]

if username=='admin':
	print("Hello admin, would you like to see status report")
else:
	print("Hello "+ username.title()+" thank you for loging in again")
print("")
#5-9
usernames=[]

if usernames==[]:
	print("We need to find some users!")
print("")
#5-10
current_users=["admin","lilly","james","dumbledore","mcgonagall"]
new_users=["Hagrid","Ron","James","Snape","Lilly"]

for user in new_users:
	user=user.lower()
	if user.lower() in current_users:
		print("You will need to ener a new username "+'"'+user+'"'+" has been used")
	else:
		print('"'+user+'"'+" username is available")

#5-11
numbers=list(range(1,10))
ordinal_numbers=[]

for number in numbers:
	if number==1:
		line=str(number)+"st"
		ordinal_numbers.append(line)
	elif number==2:
		line=str(number)+"nd"
		ordinal_numbers.append(line)
	elif number==3:
		line=str(number)+"rd"
		ordinal_numbers.append(line)
	else:
		line=str(number)+"th"
		ordinal_numbers.append(line)

print(ordinal_numbers)
