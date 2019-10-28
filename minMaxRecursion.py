#Logan Passi
#09/17/19
#minMaxRecursion.py
#Write a short recursive Python function that finds the minimum and maximum
#values in a sequence without using any loops.

def minMax(list, l):

    #base case
    if l <= 1 or l > len(list):
        return

    if list[l - 1] < list[l - 2]:
        temp = list[l - 1]
        list[l - 1] = list[l - 2]
        list[l - 2] = temp
        minMax(list, l + 1)

    minMax(list, l - 1)

myList = [67, -30, 6, 105, 2, 8, 46, -22, 42, 90, 6, 18, 17, 46, 17, 500, -432, 26, 54, -45, 80, -8, 64, 21, 87, -9, 18, 62, 98, 100, 64, -90, 93, 18]
l = len(myList)
minMax(myList, l)
print("The min value is: " + str(myList[0]))
print("The max value is: " + str(myList[l - 1]))

#The min value is: -432
#The max value is: 500