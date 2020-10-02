
#9-13
from collections import OrderedDict

glossary=OrderedDict()

glossary['key']='item of dictionary first element'
glossary['value']='item of dictionary second element'
glossary['item']='dictionary element'
glossary['pop']='del but store'
glossary['del']='just del'
glossary['set']='set(dictionary.values()): not write same value again'
glossary['for']='for key,value in dictionaty.items()'
glossary['len']='len(list)'
glossary['append']='list.append() add to last'
glossary['insert']='list.insert(2,"someting") add to 2nd element '
glossary['difference']='list1.difference(list2) only list1 has'

for key,value in glossary.items():
	print(key.title() +":\n"+value+"\n")
print("")

#9-14
from random import randint

class Die():
	
	def __init__(self,sides=6):
		self.sides=sides
	
	def roll_die(self):
		"""
		prints a random number between 1 and the number of sides 
		the die has(6)
		"""

		return randint(1,self.sides)

die_6=Die()
die_6.roll_die()

result=[]
#6 sided die and roll 10 times
print("\n6-sided die and roll it 10 times:")
for roll_times in range(10):
	
	result.append(die_6.roll_die())
	
print(result)
#10 sided die rolling 10 times
die_10=Die(10)
die_10.roll_die()
result=[]

print("\n10-sided die and roll it 10 times:")
for roll_times in range(10):
	
	result.append(die_10.roll_die())
	
print(result)
#20 sided die rolling 10 times
die_20=Die(20)
die_20.roll_die()
result=[]

print("\n20-sided die and roll it 10 times:")
for roll_times in range(10):
	
	result.append(die_20.roll_die())
	
print(result)


