# Plotting a complite populatin map
# Extracting Relevant Data
import json
from pygal.maps.world import COUNTRIES, World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

# Load the data into a list.
filename='population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
#print(pop_data)

# Build a dictionary of population data.
cc_populations={}
for pop_dict in pop_data:
	if pop_dict['Year'] == 2016:	# select 2010 population for each country.
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value'])) # get rid of .0 
		code=get_country_code(country_name)
		
		if code:
			cc_populations[code]=population
		else:
			print(country_name)
	
# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
		
# Styling world maps in pygal
wm_style =  RS('#108080',base_style=LCS)
wm= World(style=wm_style)

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#wm=World()
wm.title='World Population in 2016, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population_2016.svg')
