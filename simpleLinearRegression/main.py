from DataSet import DataSet
from LinearRegression import perform_linear_regression, plot_data_and_regression, predict_value
from tkinter import *

# Define global variables
filename = ""
data1 = DataSet("N")
headerCheck_value, a, b = 0, 0, 0
info_count = 0


# Function to handle file submission
def submit():
    global filename, headerCheck_value, data1
    filename = fileName_entry.get()
    headerCheck_value = get_value.get()
    try:
        if headerCheck_value == 0:
            hasHeaders = "N"
        else:
            hasHeaders = "Y"
        data1 = DataSet(hasHeaders)
        data1.getDataFromCsv(filename)
        fileErrorText.set(f"{filename} found\nFile {'has headers' if hasHeaders == 'Y' else 'does not have headers'}")
        ask_plot.config(state="normal")
        ask_line.config(state='normal')
    except FileNotFoundError:
        fileErrorText.set(f"The file {filename} could not be found")
    except ValueError:
        fileErrorText.set(f"Headers were found in {filename} please check the box for headers")


# Function to handle predictions
def predict(data_window, entry_predict):
    global info_count
    predict_info = StringVar()
    info_count += 1
    try:
        predict_info.set(f"{info_count}: When x is {entry_predict}, y will be {predict_value(a, b, int(entry_predict))}")
    except ValueError:
        predict_info.set(f"{info_count}: Please enter a valid integer for x")
    label_predict_value = Label(data_window, textvariable=predict_info)
    label_predict_value.pack()


def openDataWindow():
    global filename, a, b
    data_window = Toplevel(window)
    data_window.geometry("500x300")
    data_window.title(f"Data and Regression Analysis - {filename}")

    try:
        a, b, se, r, r2 = perform_linear_regression(data1)

        # Display regression coefficients
        label_a = Label(data_window, text=f"a: {round(a, 4)}")
        label_a.pack()
        label_b = Label(data_window, text=f"b: {round(b, 4)}")
        label_b.pack()
        label_se = Label(data_window, text=f"Standard Error: {round(se, 4)}")
        label_se.pack()
        label_r = Label(data_window, text=f"Correlation Coefficient: {round(r, 4)}")
        label_r.pack()
        label_r2 = Label(data_window, text=f"R^2: {round(r2, 4)}")
        label_r2.pack()

        # Predict value of y for given x
        label_predict = Label(data_window, text="Enter x value for prediction:", font=("Arial", 15))
        label_predict.pack(pady=(15, 0))

        entry_predict = Entry(data_window)
        entry_predict.pack()

        button_predict = Button(data_window, text="Predict", command=lambda: predict(data_window, entry_predict.get()))
        button_predict.pack()

        # Plot the data and regression
        plot_data = get_plot.get()
        plot_line = get_line.get()
        x_value = x_value_entry.get()

        if plot_data == 1:
            if plot_line == 0:
                x_value = 0
            plot_data_and_regression(data1, a, b, get_plot.get(), get_line.get(), x_value)

    except ZeroDivisionError:
        print("Error in linear regression")
    except Exception as e:
        print(f"An error occurred: {e}")

    data_window.mainloop()


# Function to enable/disable x value entry based on the line checkbox state
def enable_xValue_entry():
    if get_line.get() == 1:
        x_value_entry.config(state='normal')
        x_value_entry.focus_set()
    else:
        x_value_entry.config(state='disabled')


# Main Tkinter window
window = Tk()
window.geometry("500x400")
window.title("Linear Regression GUI")

# Labels, entries, and buttons for file submission
label_File = Label(window, text="Enter csv file:")
label_File.pack()

fileName_entry = Entry(window, font=("Arial", 20))
fileName_entry.pack()

label_Header = Label(window, text="Check if data has headers:")
label_Header.pack()

get_value = IntVar()
header_checkbox = Checkbutton(window, variable=get_value)
header_checkbox.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

fileErrorText = StringVar()
labelFileError = Label(window, textvariable=fileErrorText)
labelFileError.pack()

# Labels and checkboxes for plotting options
label_File = Label(window, text="Check to plot data:")
label_File.pack()

get_plot = IntVar()
ask_plot = Checkbutton(window, variable=get_plot, state="disabled")
ask_plot.pack()

label_Line = Label(window, text="Check for line of best fit:")
label_Line.pack()

get_line = IntVar()
ask_line = Checkbutton(window, variable=get_line, state="disabled", command=enable_xValue_entry)
ask_line.pack()

# Entry for x value
label_File = Label(window, text="Enter single x value for line of best fit:")
label_File.pack()

x_value_entry = Entry(window, font=("Arial", 20), state="disabled")
x_value_entry.pack()

# Button to open data window
button = Button(window, text="Open Data Window And Plot", command=openDataWindow)
button.pack()

window.mainloop()
