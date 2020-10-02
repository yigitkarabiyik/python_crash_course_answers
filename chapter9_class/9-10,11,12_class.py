#9-10
"""this instance has to be same file with restaurant.py module"""
from restaurant import Restaurant

broomsticks=Restaurant('broomsticks','butterbeer')
broomsticks.describe_restaurant()

#9-11
"""this instance has to be same file with user.py module"""
from user import User, Privileges, Admin


harry=Admin('harry','potter',21,'male','hangmeade','wizard',
		'single','fight with voldemort')

harry.privileges.show_privileges()

#9-12
"""this instance has to be same file with user_onyl.py and privileges_admin.py """
from user import User
from privileges_admin import Privileges, Admin

harry=Admin('harry','potter',21,'male','hangmeade','wizard',
		'single','fight with voldemort')

harry.privileges.show_privileges()
