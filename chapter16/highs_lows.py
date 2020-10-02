### The csv file format

# Parsing the csv file headers
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)	# read the csv file
	header_row=next(reader)	# read the first line header
	
	# Print The header and their positions (0,1,2,...)
#	for index, column_header in enumerate(header_row):	# get index and value
#		print(index, column_header)
		
	# Extracting and Reading data
	dates, highs, lows =[],[], []
	for row in reader:
		try:
			current_date= datetime.strptime(row[0], "%Y-%m-%d")
			high= int(row[1])	# row[1] has max temps
			low=int(row[3])		# row[3] has low temps
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)	# max temp list
			lows.append(low)
print(highs)	
# Ploting Data in a Temperature Chart
# Plot data.
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures, July 2014", fontsize=16)

plt.xlabel('', fontsize=12)
fig.autofmt_xdate()	# draws the date labels diagonally
plt.ylabel("Temperature(F)", fontsize=(12))
plt.tick_params(axis='both',which='major', labelsize=8)

plt.show()
