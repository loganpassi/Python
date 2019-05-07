##Logan Passi
##10/24/2016
##Prog10_3.py
##In class excersize to open a file for output and
##write a user specified number of lines.

def main():
    numDays = int(input("How many days of input?:"))
    totalSales = float()
    #open a file for output
    salesFile = open("sales.txt", "w")
    #write sales data to file
    for count in range(0, numDays):
        sales = float(input("Enter the sales for day #" + str(count + 1) + ":"))
        totalSales = totalSales + sales
        salesFile.write(str(sales) + "\n")
    #close file
    salesFile.close()
    print("total sales =", totalSales)
    print("data written to file")

main()
