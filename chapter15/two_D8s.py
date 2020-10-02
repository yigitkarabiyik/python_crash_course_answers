# Rolling the die
import pygal
from die import Die

# Create a D6 and a D10.
die_8=Die(8)

# Make some tolls, adn store results in a lis.
results=[]

for roll_num in range(1000):
	result = die_8.roll() + die_8.roll()
	results.append(result)

#Analyze the results. (how many times roll each number)
frequencies=[]
max_result= 2 * die_8.num_sides

for value in range(2, max_result+1):
	frequency= results.count(value)
	frequencies.append(frequency)
	
#Visualize the results.
hist = pygal.Bar()

hist.title="Results of rolling a D6 and D10 1000 times."
hist.x_labels=[label for label in range(2,max_result+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('Two D8s', frequencies)
hist.render_to_file('two_D8s_visual.svg')
