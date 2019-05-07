#Logan Passi
#09/26/2016
#Prog5_9.py
#In class exercise to create the Python implementation
#using a determinate loop to calculate and display the
#square of numbers from one to ten

def main():
    #local varables and constant
    counter = int(); square = int()
    #add variables to hold starting and ending variables
    lowerLimit = int(); upperLimit = int()
    lowerLimit = int(input('Enter a starting value: '))
    upperLimit = int(input('Enter an ending value: '))
    MAX_VALUE = 10 #nnote python does not support constants
    #display headings
    print('Number\tSquare')
    print('------\t------')
    #display thier numbers and squares
    #for counter in range(1, MAX_VALUE + 1): #incrementing loop
    #for counter in range(MAX_VALUE, 0, -1): #decrementing loop
    for counter in range (lowerLimit, upperLimit + 1): #user defined range
        square = counter**2 #** is the exponent operator
        print(counter, '\t', square)

main()
