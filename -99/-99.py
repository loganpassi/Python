#Logan Passi
#09/21/2016
#CIS1400-003
#This program will take the smallest value and the largest value
#entered and then display them when the value -99 is entered
def main():
    intro()
    calc()

def intro():
    print("This program will show you the largest and smallest value that is entered.")
    print("To end type in the value -99.")

def calc():
    high = float(); low = float();num = float()
    num = float(input("Enter a value:"))
    low = num; high = num
    while num != -99:
        num = float(input("Enter another value:"))
        if high < num:
            high = num
        elif low > num:
            low = num

    display(low, high)

def display(low, high):
    print("The lowest value entered is", low,".")
    print("The highest value entered is", high,".")

main()

##This program will show you the largest and smallest value that is entered.
##To finish type in the value -99.
##Enter a value:-9
##Enter another value:-99
##The lowest value entered is -99.0 .
##The highest value entered is -9.0 .
