
def get_formatted_city(city,country,population=''):
	if population:
		line=city.title()+", "+country.title()+" - "+str(population)
	else:
		line=city.title()+", "+country.title()
	
	return line
