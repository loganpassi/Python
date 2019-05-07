#Logan Passi
#09/14/2016
#CIS1400-003
#This program is used to determine the rate depending on pounds of the package.

def main():

#get input from user
    weight = float(input('Enter the weight of your package in pounds: '))
    calcAndDisplay(weight)
#calculate shipping charge
def calcAndDisplay(weight):   
    if weight <=2:
        rate = float(1.10)
    elif 2 < weight <=6:
        rate = float(2.20)
    elif 6 < weight <=10:
        rate = float(3.70)
    elif weight > 10:
        rate = float(3.80)
    shippingCharge = float(rate * weight)
    print('Your shipping charge is $',shippingCharge)
main()

##Enter the weight of your package in pounds: 6.1
##Your shipping charge is $ 22.57
