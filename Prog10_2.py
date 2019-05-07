##Logan Passi
##10/24/2016
##Prog10_2.py
##In class excersize to open a file for input and
##read a few lines of data
def main():
    #create and open file for input
    myFile = open("philosophers.dat", "r")
    # variables to hold data read from the file
    name1 = ""; name2 = ""; name3 = ""
    # read the data from file
    name1 = myFile.readline()
    name2 = myFile.readline()
    name3 = myFile.readline()
    #close file
    myFile.close()
    #display data read from file
    print("Data read from file:\n")
    print(name1)
    print(name2)
    print(name3)
main()
