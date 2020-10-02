import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	
	def setUp(self):
		
		self.snape=Employee('severus','snape',100000)
		
	
	def test_give_default_raise(self):
		"""test give_raise function with default value"""
		
		self.snape.give_raise() # call give_rise function with snape's values
		self.assertEqual(self.snape.salary,105000) # default amount 5000
	
	def test_give_custom_raise(self):
		"""test give_raise function with 8000 """
		
		self.snape.give_raise(8000) # call give_rise function with snape's values
		self.assertEqual(self.snape.salary,108000) 
		

unittest.main() 
