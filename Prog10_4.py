##Logan Passi
##10/24/2016
##Prog10_4.py
##In class excersize to open a file for input and
##read until no more lines are in file

def main():
    #open file for input
    salesFile = open("sales.txt", "r")
    #variables to hold and calculate read data
    sales = float(); totalSales = float()
    #read first line from file
    line = salesFile.readline()
    #read while there are lines to process
    while line != "":
        sales = float(line)
        print(format(sales, ".2f"))
        totalSales = totalSales + sales
        #read next line from file
        line = salesFile.readline()
    #close file
    salesFile.close()
    #display total
    print("total sales =", totalSales)
    
main()
