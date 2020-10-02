
import unittest
from city_function import get_formatted_city


class CityTestCase(unittest.TestCase):
	def test_city_country(self):
	
		formatted_city=get_formatted_city('vancouver','canada')
		self.assertEqual(formatted_city,'Vancouver, Canada')
		
	def test_city_country_population(self):
		formatted_city=get_formatted_city('vancouver','canada',6000000)
		self.assertEqual(formatted_city,'Vancouver, Canada - 6000000')

unittest.main()
