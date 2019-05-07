##Author:   
##File:     Prog10_7.py
##Date:     MM/DD/YYYY
##Descr:
##    Python example of Program 10-7 to write record data to file.
##

def main():
    # local variables
    empName = str()
    empId = int()
    empDept = str()
    numEmployees = int()
    counter = int()
    # open file for read
    employeeFile = open('employees.dat', 'w')
    # see how many records to write
    numEmployees = int(input('How many employee records do you want to create? '))
    # write employee records to file
    for counter in range (1, numEmployees + 1):
        # get employee data from user
        empName = input('\nEnter the the name of employee ' + str(counter) + ': ')
        empId = int(input('Enter the employee\'s ID number: '))
        empDept = input('Enter the the employee\'s department: ')
        # write employee data to file
        employeeFile.write(empName + '  ' + str(empId) + '  ' + empDept + '\n')
	
    # output message to user
    print('Employee records written to employees.dat.\n')
    employeeFile.close()

# run program
main()
