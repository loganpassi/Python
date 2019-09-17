#Logan Passi
#CPSC-34000
#08/27/19
#distinctNums.py
#Write a Python function that takes a sequence of numbers and determines
#if all the numbers are different from each other (that is, they are distinct).

def isDistinct (list, numElem):
    count = 0
    for i in range(numElem):
        currentElem = list[i] #grab a character to compare to the rest of characters
        for j in range(numElem):
            if currentElem == list[j]: #loop through the rest of characters to check to see if there are duplicates
                count += 1
        if count > 1:
            return False
        else:
            count = 0
    return True



numList = [] #list to hold the numbers
numElements = int(input("Enter in the numbers of elements you wish to input: "))
print("Enter in your numbers")
for i in range(numElements): #loop through the length of the  list and append each new character entered
    element = int(input())
    numList.append(element)

if isDistinct(numList, numElements) == True:
    print("The list is distinct!")
else:
    print("The list is NOT distinct!")

#Enter in the numbers of elements you wish to input: 5
#Enter in your numbers
#1
#5
#3
#4
#5
#The list is NOT distinct!

#Enter in the numbers of elements you wish to input: 6
#Enter in your numbers
#1
#5
#8
#4
#6
#3
#The list is distinct!