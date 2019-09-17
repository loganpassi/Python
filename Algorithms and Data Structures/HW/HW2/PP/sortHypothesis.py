#Logan Passi
#CPSC-34000
#09/09/19
#sortHypothesis.py
#Chapter 3 -Programming Project [P-3.57]: Perform experimental analysis to
#test the hypothesis that Python’s sortedmethod runs in O(nlog n) time on average.

import time
size = 60000000



def fillList(list):
    j = 0
    for i in range(len(list), 0, -1):
        list[j] = i
        j += 1
    calcAndPrint(list)

def calcAndPrint(list):
    startTime = time.time()
    list = sorted(list)
    endTime = time.time()
    print("\nList Size: " + str(len(list)) +"\nTotal Run Time: " + str(endTime - startTime))

for i in range(10):
    myList = [0] * int(size)
    fillList(myList)
    size /= 2


#List Size: 60000000
#Total Run Time: 0.92867112159729
#
#List Size: 30000000
#Total Run Time: 0.47452473640441895
#
#List Size: 15000000
#Total Run Time: 0.23140573501586914
#
#List Size: 7500000
#Total Run Time: 0.11895012855529785
#
#List Size: 3750000
#Total Run Time: 0.05571269989013672
#
#List Size: 1875000
#Total Run Time: 0.02892279624938965
#
#List Size: 937500
#Total Run Time: 0.013849735260009766
#
#List Size: 468750
#Total Run Time: 0.006011247634887695
#
#List Size: 234375
#Total Run Time: 0.003989458084106445
#
#List Size: 117187
#Total Run Time: 0.0019981861114501953