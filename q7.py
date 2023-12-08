# Question 7 -> How to Add an Index Field Using R/Python
import pandas as pd

# making data frame from csv file
data = pd.read_csv("D:/coding/Python/Data_Science_Assignement/employees.csv")

# setting first name as index column
data.set_index("First Name",inplace=True)

# display
print(data.head())