# printing two-digit country codes

from pygal.maps.world import COUNTRIES, World

for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])
