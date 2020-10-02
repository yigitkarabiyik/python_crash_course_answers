#6-0
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print(favorite_languages)
print("Sarah's favorite language is "+favorite_languages['sarah'].title()+".")

#6-1
person={'first_name':'harmonie','last_name':'Granger','age':'21','city':'london'}

print('\nFirts name: '+ person['first_name'].title())
print('Last name: '+person['last_name'].title())
print('Age: '+person['age'])
print('Living city: '+person['city'].title())
print("")

#6-2
favorite_numbers={'james':2,'lilly':9,'snape':8,'ron':5,'harmonie':7}

for key,value in favorite_numbers.items():
	print(key.title()+"'s favorite number is "+str(value))
print("")

#6-3

glossary={'key':'item of dictionary first element',
'value':'item of dictionary second element',
'item':'dictionary element',
'pop':'del but store',
'del':'just del',
'set':'set(dictionary.values()): not write same value again'}

for key,value in glossary.items():
	print(key.title() +":\n"+value+"\n")
