##Logan Passi
##10/17/2016
##Prog8_11.py
##In-class exersive to create the Python implementation of
##Program 8-11. This program finds the hightest value in
##an array.

#10/17/2016 LAP --> modify to include highest index
def main():
    SIZE = 5 #named constant to represent array size
    numbers = [8, 1, 12, 6, 2] #initialized list
    index = int(0)
    highest = numbers[0] #initialized highest to first array element
    highestIndex = int(0) #initialized highestIndex to first element index
    #determine highest value in array
    for index in range(1, SIZE):
        if numbers[index] > highest:
            highest = numbers[index]
            highestIndex = index
        #display highest
            print("The highest value in the array is ", numbers[highestIndex])#highest
            print("And it was found at index",highestIndex)
#start program by calling main module
main()

