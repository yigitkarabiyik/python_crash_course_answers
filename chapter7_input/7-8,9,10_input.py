#7-0 moving items from one list to another
unconfirmed_users=['alice','brian','candance']
confirmed_users=[]

while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	
	print("Verifying user: "+current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed.")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#7-0 removing all instances of specific values from a list

pets=['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

#7-0 filling a dictionary with user input
responses={}
polling_active=True

while polling_active:
	name=input("\nWhat is your name? ")
	response=input("Which mountain would you like to climb someday?")
	
	responses[name]=response
	repeat=input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active=False

print("\n--- Poll Results ---")

for name, response in responses.items():
	print(name.title()+" would like to climb "+response.title()+".")
print("\n")
#7-8

sandwich_orders=["stoner's delight","a wreck","someting else","bench girl",
"sinatra special"]
finished_sandwich=[]

while sandwich_orders:
	sandwich=sandwich_orders.pop()
	print("I made your "+sandwich+" sandwich.")
	finished_sandwich.append(sandwich)
	
print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwich:
	print(sandwich.title())

#7-9
sandwich_orders=["stoner's delight","pastrami","pastrami","a wreck",
"someting else","bench girl","pastrami","sinatra special"]
finished_sandwich=[]

print("\n\nThe deli has run out of pastrami\n")
while sandwich_orders:
	sandwich=sandwich_orders.pop()
	if sandwich=="pastrami":
			
		continue
	else:
		print("I made your "+sandwich+" sandwich.")
		finished_sandwich.append(sandwich)
	
print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwich:
	print(sandwich.title())

#7-10
dream_vocation=""
polls=[]
while dream_vocation!='quit':
	dream_vocation=input("If you could visit one place in the world, where would you go?")
	if dream_vocation=='quit':
		break
	polls.append(dream_vocation)

print("--- Result of th poll ---")
for poll in polls:
	print(poll)
