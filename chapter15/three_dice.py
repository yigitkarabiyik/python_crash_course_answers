# Rolling the die
import pygal
from die import Die

# Create a D6 and a D10.
die=Die()

# Make some tolls, adn store results in a lis.
results=[]

for roll_num in range(1000):
	result = die.roll() + die.roll() + die.roll()
	results.append(result)

#Analyze the results. (how many times roll each number)
frequencies=[]
max_result= 3 * die.num_sides

for value in range(3, max_result+1):
	frequency= results.count(value)
	frequencies.append(frequency)
	
#Visualize the results.
hist = pygal.Bar()

hist.title="Results of rolling three D6 dice 1000 times."
hist.x_labels=[label for label in range(3,max_result+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('Two D8s', frequencies)
hist.render_to_file('three_dice_visual.svg')
