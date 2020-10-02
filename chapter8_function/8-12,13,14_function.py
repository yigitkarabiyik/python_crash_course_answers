#8-12
def make_sandwich(*items):
	print("\nOrdered Sandwich: ")
	
	for item in items:
		print("- "+item.title())

make_sandwich('bacon','hardal')
make_sandwich('mashroom','papper','cheese','meetball')
make_sandwich('corn','meat','chicken','tomatto')

#8-13
def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile=build_profile('harry','potter',
birthday='06.31.1980',
mother_name="lilly",
father_name="james")

print(user_profile)

#8-14
def make_car(manufacturer,model_name,**car_info):
	car={}
	car['manufacturer']=manufacturer
	car['model_name']=model_name
	for key,value in car_info.items():
		car[key]=value
	return car

car = make_car('subaru', 'outback', color='blue',two_package=True)
print(car)
