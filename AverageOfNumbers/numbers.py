#Logan Passi
#10/24/2016
#numberAverage.py
#program to calculate the average from an external file
def main():
    total = float()
    numbersFile = open("numbers.dat", "r")
    number = float(); total = float(); average = float(); counter = int()
    line = numbersFile.readline()
    while line != "":
        number = float(line)
        print(format(number, ".2f"))
        total = total + number
        line = numbersFile.readline()
        counter += 1
    numbersFile.close()
    average = total/counter
    print("The average value is",format(average, (".2f")),".")

main()
