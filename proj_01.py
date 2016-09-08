# Mark Carosella
# proj_01.py

# CPS 311 - Fall, 2016
# Project 1

"""Program to calculate employee pay and display it
in tabular format.
"""
file_name = input("Name of file: ")
read_file = open(file_name,"r")		# Read text file
csv_lists = []
for line in read_file:		# Each line in text file
    current_list = line.split()		# Split on spaces
    current_list[1] = float(current_list[1])		# Float hourly pay
    current_list[2] = float(current_list[2])		# Float hours worked
    csv_lists.append(current_list)
print("Employee     Hours    Pay")
print("--------     -----    --------")
for each_employee in csv_lists:		# For each employee
    hourly_rate = each_employee[1]
    hours_worked = each_employee[2]
    if hours_worked <= 40:
        wages_paid = hourly_rate * hours_worked
    else:		# Calculate overtime hours
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate + hourly_rate/2)
        wages_paid = hourly_rate * 40 + overtime_pay
        print("%-13s%5.2f    $%7.2f"%(each_employee[0],each_employee[2],wages_paid))
read_file.close()

