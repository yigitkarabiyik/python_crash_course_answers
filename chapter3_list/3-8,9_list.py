#3-8
cities=["Paris","Los Angles","Argentina","Roma","Zagreb","Barcelona","London"]


print("Orginal list:			" +str(cities))

print("\nsorted(cities):			" + str(sorted(cities)))
print("cities:				"+str(cities))

print("\nsorted(cities, reverse=True):	"+str(sorted(cities, reverse=True)))
print("cities:				"+str(cities))

cities.reverse()
print("\nReverse:			"+str(cities))

cities.reverse()
print("Reverse again:			"+str(cities))

cities.sort()
print("\nSort:				"+str(cities))

cities.sort(reverse=True)
print("Sort again:			"+str(cities))

print("\ncities:				"+str(cities))
print("\n")
#3-9
names=["lilly","james","dumbledore","mcgonagall"]

while len(names)>=3:
	print("I am sorry I can't invite you "+names.pop().title())
	print("The number of inviting people: "+str(len(names)))
