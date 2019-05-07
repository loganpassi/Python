#Logan Passi
#10/03/2016
#SalesCommission.py
#In class exercise to create the Python implementation of a program
#to calculate sales commissions with the inclusion of advanced pay

# getSales will get the sales amount from the user
def getSales():
    monthlySales = float()
    monthlySales = float(input("Enter the salesperson\'s monthly sales: "))
    return monthlySales

#get advanced sales from user
def getAdvanced():
    advanced = float()
    advanced = float(input("Enter the amount of advanced pay, or 0 if no \
advanced pay was given:"))
    return advanced
#determineCommissionRate will take a sales amount as a parameter and
#return the rate for that sales amount
def determineCommissionRate(sales):
    rate = float()
    #determine rate amount bases upon sales ranges
    if sales < 10000.00:
        rate = .10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = .12
    elif sales >= 15000 and sales <+ 17999.99:
        rate = .14
    elif sales >= 18000 and sales <= 2199.99:
        rate = .16
    else:
        rate = .18
    return rate

#main controlling module
def main():
    sales = float(); commissionRate = float()
    advancedPay = float(); pay = float()
    #get program input
    sales = getSales()
    advancedPay = getAdvanced()
    #determine rate
    commissionRate = determineCommissionRate(sales)
    #calculate pay
    pay = sales * commissionRate - advancedPay
    print("The pay is $", format(pay, '.2f'))
    #determine if money is owed
    if pay < 0:
        print("The salesperson must reimburse the company!")
main()
