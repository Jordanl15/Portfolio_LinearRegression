import math
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import csv

#https://github.com/Jordanl15/Portfolio_LinearRegression.git

# Initialize empty lists for x and y values
x = []
y = []

# Ask user if data has headers
header = input("Does the file have headers? y/n: ")


# Open the CSV file
with open('testData1.csv', newline='') as csvfile:

    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Skip the header row if present
    if header.upper() == "Y":
        next(csv_reader)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Get the values from the row and append to x and y lists
        x.append(int(row[0]))
        y.append(int(row[1]))

x2 = [num ** 2 for num in x]

y2 = [num ** 2 for num in y]

xy = [num_x * num_y for num_x, num_y in zip(x, y)]

sum_x = sum(x)

sum_y = sum(y)

sum_x2 = sum(x2)

sum_y2 = sum(y2)

sum_xy = sum(xy)

n = len(x)

b = (n * sum_xy - sum_x * sum_y) / ((n * sum_x2) - (sum_x**2))

a = (sum_y / n) - (b * (sum_x / n))

x_toPredict = int(input("Enter x value for line of best fit: "))

y1 = a + b * x_toPredict

se = math.sqrt((sum_y2 - a * sum_y - b * sum_xy) / (n - 2))

r = (n * sum_xy - sum_x * sum_y) / (math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)))

r2 = r ** 2

print("y1 = ", y1)
print("b =", b)
print("a =", a)
print("se =", se)
print("r =", r)
print("r2 =", r2)

x_1, y_1 = 0, a  # Coordinates of the first point
x_2, y_2 = x_toPredict, y1  # Coordinates of the second point

fig, ax = plt.subplots()

ax.plot(x_1, y_1, 'ro')  # Plot the first point as a red circle
ax.plot(x_2, y_2, 'ro')  # Plot the second point as a red circle

line = lines.Line2D([x_1, x_2], [y_1, y_2], color='blue')  # Create a Line2D object

ax.add_artist(line)  # Add the line to the plot


plt.scatter(np.array(x), np.array(y))
plt.grid(True)
plt.show()

wantToPredict = "Y"

while wantToPredict.upper() == "Y":
    wantToPredict = input("Would you like to predict another value? y/n: ")
    if wantToPredict.upper() == "Y":
        predict = int(input("Enter x value you want to predict: "))
        print("When x is", predict, "y will be", a + b * predict)



