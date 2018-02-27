import csv
import pandas as pd

budget= pd.read_csv("C:/Users/swati/Downloads/Python/03-Python/Homework/Instructions/PyBank/raw_data/budget_data_2.csv")
# print(budget.head())

# Calculates the number of total months
total_months=len(budget)
print("Total months :", total_months)

# Adds all values in Revenue column
total_amount=budget["Revenue"].sum()
print("Total revenue:",total_amount)
 

change = 0                                                      # Keeps track of the total change between months
min_change = budget['Revenue'][0]
max_change = budget['Revenue'][0]
for x in range(0,total_months-1):
    monthly_change = budget['Revenue'][x + 1] - budget['Revenue'][x]
    change +=  monthly_change                                   # Second row - First row 
    if monthly_change < min_change:
        min_change = x + 1
    if monthly_change > max_change:
        max_change = x + 1
    
average_change = change / total_months
print("average :", average_change)

# Not the most efficient way of doin it, but it works. 
print("Greatest Increase in Revenue:", budget['Date'][max_change], "($", budget['Revenue'][max_change] - budget['Revenue'][max_change - 1], ")")
print("Greatest Decrease in Revenue:", budget['Date'][min_change], "($", budget['Revenue'][min_change] - budget['Revenue'][min_change - 1], ")")




