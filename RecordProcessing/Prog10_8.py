##Author:   
##File:     Prog10_8.py
##Date:     MM/DD/YYYY
##Descr:
##    Python example of Program 10-8 to read record data from file.
##

def main():
    # local variables
    empName = str()
    empId = int()
    empDept = str()
    # open file for read
    employeeFile = open('employees.dat', 'r')
    # display message to user
    print('Here are the employee records.')
    # read while there are lines in file
    for employee in employeeFile:
        # find occurrence of employee id
        # (2 spaces between name and id)
        idStart = employee.find('  ', 0)
        # find occurrence of employee department
        # (2 spaces between id and department)
        deptStart = employee.find('  ', idStart + 1)
        # extract name, id, and department from line
        # use Python string slicing by indicating
        # starting and ending character array indices
        # NOTE: offset by 2 for spaces between fields
        #       could also use lstrip() to remove preceding spaces
        empName = employee[0:idStart]
        empId = int(employee[idStart + 2:deptStart])
        empDept = employee[deptStart + 2:len(employee)]
        # display each field of employee
        print(format('Name: ', '10s'), empName)
        print(format('ID: ', '10s'), empId)
        print(format('Dept: ', '10s'), empDept)
        
    employeeFile.close()

# run program
main()
