#4-10
my_list=list(range(1,11))

print("The first three items in the list are: "+ str(my_list[:4]))
print("Three items from the middle of the list are: "+ str(my_list[4:7]))
print("The last three items in the list are: "+str(my_list[7:]))

#4-11-12
my_pizzas=["margherita","marinara","carbonara"]
friend_pizzas=["margherita","napoletana","quattro stagioni"]

my_pizzas.append("emiliana")
friend_pizzas.append("tonno")

print("\nMy favorite pizzas are: ")
for pizza in my_pizzas:
	print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())
	

