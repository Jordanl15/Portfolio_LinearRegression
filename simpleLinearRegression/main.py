from DataSet import DataSet
from LinearRegression import perform_linear_regression, plot_data_and_regression, predict_value

data1 = DataSet("Y")
data1.getDataFromCsv("testData1.csv")

a, b, se, r, r2 = perform_linear_regression(data1)
plot_data_and_regression(data1, a, b)
predict_value(a, b)
