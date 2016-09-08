# Mark Carosella
# proj_01.py

# CPS 311 - Fall, 2016
# Project 1

"""Program to calculate employee pay and display it
in tabular format.
"""
file_name = input("Name of file: ")
read_file = open(file_name,"r")
csv_lists = []
for line in read_file:
    current_list = line.split()
    current_list[1] = float(current_list[1])
    current_list[2] = float(current_list[2])
    csv_lists.append(current_list)
print("Employee     Hours    Pay")
print("--------     -----    --------")
avg_worked = 0
count = 0
highest_wage = 0
for each_employee in csv_lists:
    hourly_rate = each_employee[1]
    hours_worked = each_employee[2]
    avg_worked += hours_worked
    count += 1
    if hours_worked <= 40:
        wages_paid = hourly_rate * hours_worked
    else:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate + hourly_rate/2)
        wages_paid = hourly_rate * 40 + overtime_pay
        print("%-13s%5.2f    $%7.2f"%(each_employee[0],each_employee[2],wages_paid,))
    if wages_paid > highest_wage:	# Determine highest wage
        highest_wage = wages_paid

print("")
print("Highest pay awarded = $%.2f"% (highest_wage))
print("Average hrs worked = %.2f"%(avg_worked/count))	# Avg the hours

read_file.close()

