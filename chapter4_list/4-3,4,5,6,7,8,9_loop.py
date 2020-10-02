#4-3
for number in range(1,21):
	print(number)

#4-4
numbers=list(range(1,1000001))
#for number in numbers:
#	print(number)

#4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
odd_numbers=list(range(1,21,2))

for number in odd_numbers:
	print(number)
	
#4-7
multiple=1

for number in range(3,31,3):
	multiple=multiple*number

print(multiple)

#4-8

for number in range(1,11):
	print(number**3)

#4-9
cubes_list=[value**3 for value in range(1,11)]
print(cubes_list)
