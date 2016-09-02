# CPS 311 - Fall, 2016 - Project #1
## Employee payroll report

This project is designed to help you review basic text file
manipulation and output formatting in Python.

This project is based on [LM] Project #6, pp. 37.

The Payroll Department keeps a list of employee information for each pay 
period in a text file. The format of each line of the file is 

`<last name> <hourly wage> <hours worked>`

Write a program (named `proj_01.py`) that inputs a filename from the user, and
then prints a report to the terminal of the wages paid to all employees for 
the given period. The data should be read from the file specified by the user.
 
The report should be in tabular format with the appropriate header. 
Each line should contain an employee’s name, the hours worked, and the 
wages paid for that period.

Pay calculation should include the hourly rate for every hour worked
up to and including 40, with "time-and-a-half" award for each hour
worked over 40.

At the end of the report, two additional lines should report

1. the highest pay awarded for the period, and 
2. the avearge number of hours worked by all employees

**Sample input:**

The sample input file named `payroll.txt` can be used to test your code.

**Sample output:**

Sample output (based on the sample input) is shown in `sample-output.txt`.
Make certain that you also test your code with a data file you create.

### Branching requirements

You are to submit this project using multiple branches in GitHub. Do **not** merge your commits. I want to see 3 separate branches, as indicated (and named) below. Note that my sample output file shows what the output from the 3rd branch should look like.

* Branch 1 ("master")
  * Branch 1 should contain a basic program that can successfully open the file for reading, after prompting the user for the filename. It should read the lines of the file and merely echo them back out to the screen, line by line.
  
* Branch 2 ("pretty")
  * Branch 2 should replace the basic output with the formatted output, which displays the employee's name, hours worked, and calculated wages paid for that period.
  
* Branch 3 ("summary")
  * Branch 3 should include all of the modifications from Branch 2, but should also include the two additional lines that report the highest pay awarded for the period, as well as the average number of hours worked by all employees.