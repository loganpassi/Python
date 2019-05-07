#Logan Passi
#09/19/2016
#OvetimeCalc.py
#In class exercise to create the python implementation of an overtime pay calculator
#global named constant
BASE_HOURS = float(40.00)
def main():
    hoursWorked = float(input('Enter the number of hours worked:'))
    payRate = float(input('Enter the hourly pay rate:'))
    overtime = False
    if hoursWorked > BASE_HOURS:
        overtime = True

    if overtime:
        calcOTPay(hoursWorked, payRate)
    else:
        calcPay(hoursWorked, payRate)

#module to calculate the gross pay
def calcPay(hours, rate):
    grossPay = float(hours * rate)
    print('The gross pay is $', grossPay)

#module to calculate the gross pay with overtime
def calcOTPay(hours, rate):
    OT_MULTIPLIER = float(1.5)
    otHours = float(hours - BASE_HOURS)
    otPay = float(otHours * rate * OT_MULTIPLIER)
    grossPay = float(BASE_HOURS * rate + otPay)
    print('The gross pay with overtime is $', grossPay)

main()

##Enter the number of hours worked:24
##Enter the hourly pay rate:8.5
##The gross pay is $ 204.0
