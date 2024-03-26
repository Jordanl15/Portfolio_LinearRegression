import csv


class DataSet:

    x = []
    y = []

    def __init__(self, headers):
        self.headers = headers

    def getDataFromCsv(self, file_name):

        # Open the CSV file
        with open(file_name, newline='') as csvfile:

            # Create a CSV reader object
            csv_reader = csv.reader(csvfile)

            # Skip the header row if present
            if self.headers.upper() == "Y":
                next(csv_reader)

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Get the values from the row and append to x and y lists
                self.x.append(int(row[0]))
                self.y.append(int(row[1]))

    def getDataManually(self, x_values, y_values):
        self.x = x_values
        self.y = y_values