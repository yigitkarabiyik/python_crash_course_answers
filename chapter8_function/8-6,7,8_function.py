#8-0 return value
def get_formatted_name(first_name,last_name):
	full_name=first_name+' '+last_name
	
	return full_name.title()
	
character=get_formatted_name('harry','potter')
print(character)

#8-0 making an argument optional

def get_formatted_name(first_name,last_name,middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name=first_name+' '+last_name
	
	return full_name.title()
	
writter=get_formatted_name('joanne','kathleen','rowling')
character=get_formatted_name("harry","potter")
print(writter)
print(character)

#8-0 returning a dictionary
def build_person(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}	
	
	if age:
		person['age']=age

	return person
	
character=build_person('harry','potter',22)
print(character)

#8-0 using a function with a while loop
def get_formatted_name(first_name,last_name):
	full_name=first_name+' '+last_name
	
	return full_name.title()

while True:
	print("\nPlese tell me your name: ")
	print("(enter 'q' at any time to quit)\n")
	
	f_name=input("First name: ")
	if f_name=='q':
		break
	l_name=input("Last name: ")
	if l_name=='q':
		break

	formatted_name=get_formatted_name(f_name,l_name)
	print("\nHello, "+formatted_name+"!")

#8-6
def city_country(city,country):
	print('"'+city.title()+', '+country.title()+'"')

city_country("vancouver","canada")
city_country("toront","canada")
city_country("los angles","america")

#8-7
def make_album(artist_name,album_title,tracks=''):
	music_album={"artist name":artist_name,"album title":album_title}
	
	if tracks:
		music_album['tracks']=tracks
	
	return music_album


print("\nEnter a three different album:")
print("(enter'q' at any time to quit)\n")

for i in range(3):
	artist=input("\nPlease enter artist name: ")
	album=input("Please enter album name: ")
	track=input("Please if you know enter how many tracks in the album: ")
	if track:
		print(make_album(artist,album,track))
	else:
		print(make_album(artist,album))
		
#8-8
def make_album(artist_name='',album_title='',tracks=''):
	music_album={"artist name":artist_name,"album title":album_title}
	
	if tracks:
		music_album['tracks']=tracks
	
	return music_album

print("\nEnter these information until enter 'q' at any tine to quit\n")

while True:
	artist=input("Please enter artist name: ")
	if artist=='q':
		break
	album=input("Please enter album name: ")
	if album=='q':
		break
	track=input("Please if you know enter how many tracks in the album: ")
	if track=='q':
		break
	print()
	print(make_album(artist,album,track))
	
