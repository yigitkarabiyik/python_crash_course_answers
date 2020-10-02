
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Test's for 'name_function.py'"""
	
	def test_first_last_name(self):
		"""Do name like 'Severus Snape' work?"""
		formatted_name=get_formatted_name('severus','snape')
		self.assertEqual(formatted_name,'Severus Snape')
		
	def test_first_last_middle_name(self):
		"""Do name like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name=get_formatted_name(
				'wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
		
		
unittest.main()
