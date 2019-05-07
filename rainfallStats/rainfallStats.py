#Logan Passi
#10/19/2016
#CIS1400-003
#rainfallStats.py
#This program is used to determine the most, least
#and total amount from rain for the data entered

def main():
    index = int()
    total = float()
    average = float()
    monthsArray = ["January", "February", "March", "April", "May", "June",\
    "July", "August", "September", "October", "November", "December"]
    rainfallArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    size = len(monthsArray)
    for index in range(0, size):
        rainfallArray[index] = float(input("Enter in the amount of rainfall in inches for "\
    + monthsArray[index]+ ":"))
        total = rainfallArray[index] + total

    largestIndex = int(GetLargestRainfall(rainfallArray, size))
    smallestIndex = int(GetSmallestRainfall(rainfallArray, size))
    average = total/size

    print("The largest amount of rain was", rainfallArray[largestIndex],"in", monthsArray[largestIndex],".")
    print("The smallest amount of rain was", rainfallArray[smallestIndex],"in", monthsArray[smallestIndex],".")
    print("The monthly average amount of rain is",format(average, ".2f"),".")
    print("The total amount of rain is", format(total, ".2f"),".")
    

def GetLargestRainfall(array, size):
    index = int()
    largest = array[0]
    for index in range(0, size):
        if largest < array[index]:
            largest = array[index]
            largestIndex = index
    return largestIndex

def GetSmallestRainfall(array, size):
    index = int()
    smallest = array[0]
    for index in range(0, size):
        if smallest > array[index]:
            smallest = array[index]
            smallestIndex = index
    return smallestIndex

main()


##Enter in the amount of rainfall in inches for January:48
##Enter in the amount of rainfall in inches for February:25.24
##Enter in the amount of rainfall in inches for March:56.48
##Enter in the amount of rainfall in inches for April:65.45
##Enter in the amount of rainfall in inches for May:41.12
##Enter in the amount of rainfall in inches for June:23.14
##Enter in the amount of rainfall in inches for July:65.36
##Enter in the amount of rainfall in inches for August:483.14
##Enter in the amount of rainfall in inches for September:52.36
##Enter in the amount of rainfall in inches for October:3.25
##Enter in the amount of rainfall in inches for November:4.36
##Enter in the amount of rainfall in inches for December:52.36
##The largest amount of rain was 483.14 in August .
##The smallest amount of rain was 3.25 in October .
##The monthly average amount of rain is 76.69 .
##The total amount of rain is 920.26 .
