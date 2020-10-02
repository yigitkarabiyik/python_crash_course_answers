#6-4
glossary={'key':'item of dictionary first element',
'value':'item of dictionary second element',
'item':'dictionary element',
'pop':'del but store',
'del':'just del',
'set':'set(dictionary.values()): not write same value again'}

glossary['for']='for key,value in dictionaty.items()'
glossary['len']='len(list)'
glossary['append']='list.append() add to last'
glossary['insert']='list.insert(2,"someting") add to 2nd element '
glossary['difference']='list1.difference(list2) only list1 has'

for key,value in glossary.items():
	print(key.title() +":\n"+value+"\n")
print("")

#6-5
rivers={'nile':'egypt','dicle':'turkey','mississippi':'america'}

for key,value in rivers.items():
	print("The "+key.title()+" runs through "+value.title()+".")
print("\n")
for key in rivers.keys():
	print(key.title())
print("\n")
for value in rivers.values():
	print(value.title())
print("\n")

#6-6
people=['jen','lilly','sarah','james','edward','phill','ron','hermonie']
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in people:
	if name in favorite_languages.keys():
			print(name.title()+"'s favorite language is "+favorite_languages[name])
	else:
		print(name.title()+" would be want to register to favorite languages poll.")
	


