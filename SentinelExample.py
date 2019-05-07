#Logan Passi
#9/26/2016
#SentinelExample.py
# In class exersise to demonstrate the use of sentinel to control
# user input. Add all input numbers until the sentinel value
# is read.

def main():
    number = int(); total = int() #local variables: initialize accumulator
    print('This program calculates the total of all input numbers.')
    print('A value of 0 will end input and display the total.')
    #get the starting number
    number = int(input('Enter a starting number (0 end input): '))
    #loop while sentinel has not been input
    while number != 0:
        total = total + number #accumulate user input
        #get next number
        number = int(input('Enter another number (0 will end the input): '))

    #display the total
    print('The total of all input numbers is', total)

main()

##This program calculates the total of all input numbers.
##A value of 0 will end input and display the total.
##Enter a starting number (0 end input): 5
##Enter another number (0 will end the input): 1
##Enter another number (0 will end the input): 6
##Enter another number (0 will end the input): 2
##Enter another number (0 will end the input): 8
##Enter another number (0 will end the input): 4
##Enter another number (0 will end the input): 1
##Enter another number (0 will end the input): 6
##Enter another number (0 will end the input): 9
##Enter another number (0 will end the input): 5
##Enter another number (0 will end the input): 4
##Enter another number (0 will end the input): 1
##Enter another number (0 will end the input): 3
##Enter another number (0 will end the input): 0
##The total of all input numbers is  55
