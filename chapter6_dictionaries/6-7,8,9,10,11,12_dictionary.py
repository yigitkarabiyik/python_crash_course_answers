#6-7
hermonie={'first_name':'harmonie','last_name':'Granger','age':21,'city':'london'}
ron={'first_name':'ron','last_name':'weasley','age':21,'city':'devon'}
snape={'first_name':'severus','last_name':'snape','age':50,'city':'hogsmeade'}

wizards=[hermonie,ron,snape]

for wizard in wizards:
	
	print(wizard['first_name'].upper())
	print("Full name: "+wizard['first_name'].title())
	print("Last name: "+wizard['last_name'].title())
	print("Age: "+str(wizard['age']))
	print("City: "+wizard['city'].title())
	print("")

#6-8
hedwig={'kind':'snowy owl','owner':'harry potter'}
trevor={'kind':'toad','owner':'neville'}
crookshanks={'kind':'cat','owner':'hermonie'}
errol={'kind':'grey owl','owner':'weasley family'}

pets=[hedwig,crookshanks,trevor,errol]

for pet in pets:
	for key,value in pet.items():
		print(key.title()+": "+value.title())
	print("")

#6-9
favorite_places={'harmonie':['library','class'],'ron':['chess room'],
'harry potter':['chamber of secrets','quidditch arena','hogwarts']}

for name,favorite_place in favorite_places.items():
	print(name.title()+"'s favorite places are "+' and '.join(favorite_place).title())

print("")
#6-10
favorite_numbers={'james':[2,6],'lilly':[9,7],'snape':[8,4],'ron':[5,3],'harmonie':[7,1]}

for key,value in favorite_numbers.items():
	
	print(key.title()+"'s favorite numbers are "+' and '.join(str(x) for x in value))
print("")

#6-11
cities={'toronto':{'country':'canada','population':'5.6 million','fact':'5th'},
'vancouver':{'country':'canada','population':'675 thousands','fact':'3rd'},
'los angles':{'country':'america','population':'4 million','fact':'10th'}}

for city,information in cities.items():
	print("\n"+city.upper())
	for key,value in information.items():
		print(key.title()+": "+value)

#6-12

