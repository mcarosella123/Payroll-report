# Mark Carosella
# proj_01.py

# CPS 311 - Fall, 2016
# Project 1

"""Program to calculate employee pay and display it
in tabular format.
"""
file_name = input("Name of file: ")	# Prompt user for file name
read_file = open(file_name,"r")
for each_line in read_file:		# Read and print each line
    print(each_line)
read_file.close()

