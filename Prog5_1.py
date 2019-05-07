#Logan Passi
#09/21/2016
#Prog5_1.py
#In class exercise to create the Python
#implementation of Progmram 5-1 which calculates commision

def main():
    #local variables
    sales = float(); commission = float(); keepGoing = 'y'
    #local names constant
    COMMISSION_RATE = 0.10
    #pre-test loop while calculating commissions
    while keepGoing == 'y' or keepGoing == 'Y':
        sales = float(input('Enter the amount of sales:'))
        commission = sales * COMMISSION_RATE
        print('The commission is $', commission)
        keepGoing = input('Do you wish to calculate another commission? (y for yes)')

#call main to begin program
main()
