##Author:   Carolyn England
##Date:     10/03/2016
##Program:  SalesCommission.py
##Descr:
##    In class exercise to create the Python implementation
##    of a program to calculate sales commissions with the
##    inclusion of advanced pay.

##10/05/2016 LAP -> added validation for user input
##Logan Passi

# getSales will get the sales amount from the user
def getSales():
    monthlySales = ""
    monthlySales = input('Enter the salesperson\'s monthly sales: ')
    #include the validation loop
    while invalidSales(monthlySales):
        print("ERROR! Valid sales are numeric values greater than or equal to 0.")
        monthlySales = input("Re-enter the salesperson montly sales:")
    return float(monthlySales)

#validation function for sales
#input value should be numeric and > 0
def invalidSales(sales):
    status = True
    if not sales.replace('.', '', 1).isnumeric() or float(sales) < 0:
        status = True
    else:
        status = False
    return status

# getAdvanced will get the advanced pay amount from the user
def getAdvanced():
    advanced = ""
    advanced = input('Enter the amount of advanced pay, or 0 if no \
advanced pay was given: ')
    while invalidAdvanced(advanced):
        advanced = input('Enter the amount of advanced pay, or 0 if no \
advanced pay was given: ')
    return float(advanced)

#validation function for advanced pay
#input value should be numeric and between 0 and 2000
def invalidAdvanced(advanced):
    #Python use of exception handling
    try:
        value = float(advanced) #will raise ValueError
        if value < 0 or value > 2000: #range check
            print("ERROR! Entered value not in range of 0 to 2000.")
            status = True
        else:
            status = False #value is numeric and in range
    except ValueError:
        print("ERROR!Entered value was not numeric.")
        status = True
    return status

# determineCommissionRate will take a sales amount as a parameter and
# return the rate for that sales amount
def determineCommissionRate(sales):
    rate = float()
    # determine rate amount based upon sales ranges
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000.00 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000.00 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate

# main controlling module
def main():
    sales = float(); commissionRate = float()
    advancedPay = float(); pay = float()
    # get program input
    sales = getSales()
    advancedPay = getAdvanced()
    # determine rate
    commissionRate = determineCommissionRate(sales)
    # calclate the pay
    pay = sales * commissionRate - advancedPay
    print('The pay is $', format(pay, '.2f'))
    # determine if money is owed
    if pay < 0:
        print('The salesperson must reimburse the company!')
##Enter the amount of advanced pay, or 0 if no advanced pay was given: 20003
##ERROR! Entered value not in range of 0 to 2000.
##Enter the amount of advanced pay, or 0 if no advanced pay was given: 1999
##1999.0


