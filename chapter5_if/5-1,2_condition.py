#5-1
my_os="linux"
print("Is operating system == 'linux'?")
print(my_os=="linux")

print("Is operating system == 'microsoft'?")
print(my_os=="microsoft")

#5-2
names=["Lilly","James","Dumbledore","Mcgonagall"]

print("\n5==4? "+str(5==5))
print("5=!4? "+str(5!=4))
print("Is Lilly in the list? "+str(names[0].lower()=='lilly'))
print("5=<4? "+str(5<=4))
print("5=>4? "+str(5>=4))
print("Is Snape in the list? "+str('Snape' in names))
print("Are Dumbledore or Hagrid in the list? "+str('Dumbledore'or'Hagrid' in names))
print("Are Lilly and James in the list? "+str('Lilly'and'James' in names))
