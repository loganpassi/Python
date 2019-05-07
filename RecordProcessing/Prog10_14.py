##Author:   
##File:     Prog10_14.py
##Date:     MM/DD/YYYY
##Descr:
##    Python example of Program 10-14 to create a fundraiser report
##    using control break reporting.
##

def main():
    printHeader()
    printDetails()
    
def printHeader():
    print('Pinebrook Academy Fundraiser Report')
    print()
    print('Student ID       Donation Amount')
    print('===================================')

def printDetails():
    # local variables
    studentID = int()
    currentID = int()
    donation = float()
    studentTotal = float(0)
    total = float(0)
    # open file for read
    donationsFile = open('donations.dat', 'r')
    # read and process first line of file
    student = donationsFile.readline()
    # find occurrence of donation amount
    donationStart = student.find('$', 0)
    # extract student ID and donation amount from line
    # use Python string slicing by indicating
    # starting and ending character array indices
    # NOTE: Use $ character indicator for start of donation
    studentID = int(student[0:donationStart])
    donation = float(student[donationStart + 1:len(student)])
    # set control values
    currentID = studentID    
    # read while there are lines in file
    # for student in donationsFile:
    while student != '':
        if studentID != currentID:
            # print out student summary
            print('Total donations for student: $', format(studentTotal, '.2f'))
            # reset control fields
            currentID = studentID
            studentTotal = float(0)
        # display student donation
        print(format(studentID, '10d'), format(donation, '.2f'))
        # update accumulators
        studentTotal = studentTotal + donation
        total = total + donation
        # read and process next line in file
        student = donationsFile.readline()
        # only process non-empty line
        if student != '':
            # find occurrence of donation amount
            donationStart = student.find('$', 0)
            # extract student ID and donation amount from line
            # use Python string slicing by indicating
            # starting and ending character array indices
            # NOTE: Use $ character indicator for start of donation
            studentID = int(student[0:donationStart])
            donation = float(student[donationStart + 1:len(student)])
    # display totals for last student
    print('Total donations for student: $', format(studentTotal, '.2f'))
    donationsFile.close()

# run program
main()
