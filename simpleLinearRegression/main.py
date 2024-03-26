from DataSet import DataSet
from LinearRegression import perform_linear_regression, plot_data_and_regression, predict_value
from tkinter import *

# Define filename as a global variable
filename = ""
headerCheck_value = 0
data1 = DataSet("N")



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
        fileErrorText.set(f"{filename} found\nFile {'has headers' if hasHeaders == 'Y' else 'does not have headers'}")  # Update label text if file is found
        ask_plot.config(state="normal")
        ask_plot.focus_set()
        ask_line.config(state='normal')
        ask_line.focus_set()
    except FileNotFoundError:
        fileErrorText.set(f"The file {filename} could not be found")  # Update label text if file is not found
    except ValueError:
        fileErrorText.set(f"Headers were found in {filename} please check the box for headers")


window = Tk()


def openDataWindow():
    data_window = Toplevel(window)
    data_window.geometry("500x150")
    data_window.title("Data and Regression Analysis")

    try:
        a, b, se, r, r2 = perform_linear_regression(data1)

        # Create a frame to hold the plot
        plot_frame = Frame(data_window)
        plot_frame.pack()

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

        # Plot the data and regression
        if get_plot.get() == 1:
            plot_data_and_regression(data1, a, b, get_plot.get(), get_line.get(), int(x_value_entry.get()))

    except ZeroDivisionError:
        print("Error in linear regression")

    data_window.mainloop()


def enable_xValue_entry():
    if get_line.get() == 1:
        x_value_entry.config(state='normal')
        x_value_entry.focus_set()  # Move focus to the next entry
    else:
        x_value_entry.config(state='disabled')


window.geometry("500x500")
window.title("Linear Regression GUI")

label_File = Label(window, text="Enter csv file: ")
label_File.pack()

fileName_entry = Entry(window, font=("Arial", 20))
fileName_entry.pack()

label_Header = Label(window, text="Check if data has headers: ")
label_Header.pack()

get_value = IntVar()
header_checkbox = Checkbutton(window, variable=get_value)
header_checkbox.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

fileErrorText = StringVar()
labelFileError = Label(window, textvariable=fileErrorText)
labelFileError.pack()


label_File = Label(window, text="Check to plot data: ")
label_File.pack()

get_plot = IntVar()
ask_plot = Checkbutton(window, variable=get_plot, state="disabled")
ask_plot.pack()


label_Line = Label(window, text="Check for line of best fit: ")
label_Line.pack()

get_line = IntVar()
ask_line = Checkbutton(window, variable=get_line, state="disabled", command=enable_xValue_entry)
ask_line.pack()


label_File = Label(window, text="Enter single x value for line of best fit: ")
label_File.pack()

x_value_entry = Entry(window, font=("Arial", 20), state="disabled")
x_value_entry.pack()


button = Button(window, text="Open New Window", command=openDataWindow)
button.pack()


window.mainloop()
