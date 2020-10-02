#3-1
names=["lilly","james","dumbledore","mcgonagall"]
for name in names:
	print(name)
print("")

#3-2
for name in names:
	print("Hi " +name+ " nice to see you:)")
print("\n")

#3-3
motors=["honda","bmw","vespa","ducati"]

for motor in motors:
	print("I would like to own a "+motor.title()+" motorcycle.")
print("\n")	

#3-4
for name in names:
	print("I would like to see "+name.title()+" on diner.")

#3-5
print("\n" +names[1].title()+" will not able to come to dinner.\n")

names.pop(1)
names.append('hermonie')

for name in names:
	print("I would like to see "+name.title()+" on diner.")
print()

#3-6
names.insert(0,"snape")
names.insert(2,"hagrid")
names.append("ron")

for name in names:
	print("I would like to see "+name.title()+" on diner.")
print("")
#3-7

while len(names)>=3:
	print("I am sorry I can't invite you "+names.pop().title())

print("")

for name in names:
	print("You still invited "+name.title())
	
del names[0]
del names[0]

print(names)
