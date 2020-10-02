# Return the 2-digit country code
from pygal.maps.world import COUNTRIES, World

def get_country_code(country_name):
	"""Return the Pygal 2-digit country code for the given country."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
		elif country_name == 'Yemen, Rep.':
			return 'ye'
		elif country_name =='Congo, Dem. Rep.':
			return 'cg'
	# If the country wasn't found, retun None.
	return None
	

		
