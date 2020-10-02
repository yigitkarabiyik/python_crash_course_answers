import csv
from pygal.maps.world import COUNTRIES, World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

filename='inflation_csv.csv'
with open(filename) as f:
	data=csv.reader(f)
	header_row=next(data)
	header_row=next(data)
	header_row=next(data)
	header_row=next(data)
	header_row=next(data)
#countries={}
	countries_list={}
	
	for countries in data:
		country=countries[0]
		value=countries[51]
		print(value)
		code=get_country_code(country)
		if code:
			countries_list[code]=value

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in countries_list.items():
	if pop < 1:
		cc_pops_1[cc] = pop
	elif pop < 10:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
		
# Styling world maps in pygal
wm_style =  RS('#108080',base_style=LCS)
wm= World(style=wm_style)

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#wm=World()
wm.title='World GDP in 2016, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_gdp_2016.svg')
