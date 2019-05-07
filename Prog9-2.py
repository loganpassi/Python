# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Prog9_2.py
# Descr:
# In-class exercise to create the Python implementation
# of Bubble Sort Program 9-2 in Gaddis.

def main():
    # Constant for the array size
    SIZE = 6

    # Array to hold test scores
    testScores = [0, 0, 0, 0, 0, 0]
    # Get the test scores
    getTestScores(testScores, SIZE)
    # Sort the test scores
    bubbleSort(testScores, SIZE)
    # Display the test scores
    print('Here are the test scores sorted from lowest to highest.')
    showTestScores(testScores, SIZE)

# The getTestScores module prompts the user
# to enter test scores into the array that is
# passed as an argument.
def getTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Get the test scores
    for index in range (0, arraySize):
        array[index] = int(input('Enter score number ' + str(index + 1) + ' as integer: '))

# The showTestScores module displays the contents
# of the array that is passed as an argument.
def showTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Display the test scores
    for index in range (0, arraySize):
        print(array[index])

# The bubbleSort module accepts an array of Integers
# and the array's size as arguments.  When the module
# is finished, the values in the array will be sorted
# in ascending order.
def bubbleSort(array, arraySize):
    maxElement = int() #max element in array
    index = int() #loop index variable
    #decrementing loop to go from last element to first
    for maxElement in range(arraySize - 1, -1, -1):
        #incrementing loop to go from fist elemnent to max element
        for index in range(0, maxElement):
            #compare current with nex element and swap if out of order
            if array[index] > array[index +1]:
                temp = array[index]
                array[index] = array[index +1]
                array[index + 1] = temp
    return


# start program
main()
