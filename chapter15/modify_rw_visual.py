import matplotlib.pyplot as plt
 
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	# Adding plot points
	rw= RandomWalk()	# call RandomWalk class
	rw.fill_walk()	# call fill_walk function
	
	# Set the size of the plotting window.
	plt.figure(dpi=128, figsize=(10,6))
	
	# Plot and color the random walking
	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, linewidth=0.5)
	
	# Emphasize the first and last points.
	plt.scatter(0,0, c='green', edgecolor='none' , s=50)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none'
		,s=50)
	
	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()	# ploting
	
	# Ask plot again
	keep_running= input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
