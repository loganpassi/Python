# Author:  Logan Passi
# Date:    11/07/2016
# Program: Prog9_8.py
# Descr:
# In-class exercise to create the Python implementation
# of Binary Search Program 9-8 in Gaddis
def main():
    # Constant for the array size
    SIZE = 6
    # array of instructor names, already sorted in
    # ascending order
    names = ['Hall', 'Harrison', 'Hoyle', 'Kimura', 'Lopez', 'Pike']
    # parallel array of instructor phone numbers
    phones = ['555-6783', '555-0199', '555-9974', '555-2377', '555-7772', '555-1716']
    # variable to hold the name to search for
    searchName = ''
    # variable to hold the subscript of the name
    index = int()
    # variable to control the loop
    again = 'Y'
    while again == 'Y' or again == 'y':
        # get the name to search for
        searchName = input('Enter a name to search for: ')
        # search for the last name
        index = binarySearch(names, searchName, SIZE)
        if index != -1:
            # display the phone number
            print('The phone number is ' + str(phones[index]))
        else:
            # the name was not found in the array
            print(searchName + ' was not found.')
        again = input('Do you want to search again? (Y=Yes, N=No) ')

# The binarySearch function accepts as arguments a String
# array, a value to search the array for, and the size 
# of the array.  If the value is found in the array, its
# subscript is returned.  Otherwise, -1 is returned,
# indicating that the value was not found in the array.
def binarySearch(array, value, arraySize):
    # Position of the search value
    position = -1
    first = 0 #index of the first array element
    last = arraySize - 1 #index of the last array element
    found = False
    middle = int() #index of the middle array element\
    #loop while not found and array first and last are valid
    while not found and first <= last:
        #calculate the middle element index
        middle = int((first + last) / 2)
        #see if value at middle element
        if array[middle] == value:
            found = True
            position = middle
        #else, if the value is in the lower half
        elif array[middle] > value:
            last = middle - 1#retting the last element
        #else the value is in the upper half...
        else:
            first = middle + 1#resetting the first element
    # return the position of the item, or -1
    # if the item was not found
    return position

# start program
main()
