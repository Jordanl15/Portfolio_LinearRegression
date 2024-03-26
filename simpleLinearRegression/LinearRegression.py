import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as lines


def perform_linear_regression(data1):
    x2 = [num ** 2 for num in data1.x]
    y2 = [num ** 2 for num in data1.y]
    xy = [num_x * num_y for num_x, num_y in zip(data1.x, data1.y)]

    sum_x = sum(data1.x)
    sum_y = sum(data1.y)
    sum_x2 = sum(x2)
    sum_y2 = sum(y2)
    sum_xy = sum(xy)

    n = len(data1.x)

    b = (n * sum_xy - sum_x * sum_y) / ((n * sum_x2) - (sum_x ** 2))
    a = (sum_y / n) - (b * (sum_x / n))
    se = math.sqrt((sum_y2 - a * sum_y - b * sum_xy) / (n - 2))
    r = (n * sum_xy - sum_x * sum_y) / (math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)))
    r2 = r ** 2

    return a, b, se, r, r2


def plot_data_and_regression(data1, a, b, ask_plot, ask_line, x_value):

    if ask_plot == 1:

        if ask_line == 1:
            y1 = a + b * x_value
            x_1, y_1 = 0, a  # Coordinates of the first point
            x_2, y_2 = x_value, y1  # Coordinates of the second point

            fig, ax = plt.subplots()

            ax.plot(x_1, y_1, 'ro')  # Plot the first point as a red circle
            ax.plot(x_2, y_2, 'ro')  # Plot the second point as a red circle

            line = lines.Line2D([x_1, x_2], [y_1, y_2], color='blue')  # Create a Line2D object

            ax.add_artist(line)  # Add the line to the plot

        plt.scatter(np.array(data1.x), np.array(data1.y))
        plt.grid(True)
        plt.show()


def predict_value(a, b):
    want_to_predict = "Y"
    while want_to_predict.upper() == "Y":
        want_to_predict = input("Would you like to predict another value? y/n: ")
        if want_to_predict.upper() == "Y":
            predict = int(input("Enter x value you want to predict: "))
            print("When x is", predict, "y will be", a + b * predict)
