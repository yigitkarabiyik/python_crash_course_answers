
import matplotlib.pyplot as plt

### calculating data automatically
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

### set chart title and lables axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

### set size of tick lables.
#plt.tick_params(axis='both', which='major', labelsize=14)


#plt.axis([0,1100,0,1100000]) # need min and max value for both labels

### color
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=10)
#plt.scatter(x_values, y_values, c=(0.7,0,0), edgecolor='none', s=10)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
	edgecolor='none', s=20)
	
### saving your plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
