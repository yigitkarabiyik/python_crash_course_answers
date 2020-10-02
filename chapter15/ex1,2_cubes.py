import matplotlib.pyplot as plt

"""plot fives cubic numbers"""

x_values=list(range(1,5001))
cubes=[x**3 for x in x_values]

plt.scatter(x_values[:5],cubes[:5])
plt.show()

"""plot 5000 cubic numbers"""

plt.scatter(x_values,cubes, c=cubes, cmap=plt.cm.Reds, s=10)
plt.show()


