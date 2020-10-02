# Rolling the die
import pygal
from die import Die

# Create a die
die=Die()

# Make some tolls, adn store results in a lis.
results=[]

for roll_num in range(1000):
	result = die.roll() * die.roll()
	results.append(result)

#Analyze the results. (how many times roll each number)
frequencies=[]
max_result= die.num_sides * die.num_sides

for value in range(1, max_result+1):
	frequency= results.count(value)
	frequencies.append(frequency)
	
#Visualize the results.
hist = pygal.Bar()

hist.title="Results of rolling a D6 and D10 1000 times."
hist.x_labels=[label for label in range(1,max_result+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('Two D6 mul.', frequencies)
hist.render_to_file('dice_multiply_visual.svg')
