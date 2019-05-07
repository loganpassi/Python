##Logan Passi
##10/24/2016
##Prog10_1.py
##In class excersize to open a file for output and
##write a few lines of data
def main():
    #open a file for output
    myFile = open("philosophers.dat", "w")
    #write the data to file\
    myFile.write("Nick Bashor\n")
    myFile.write("Anuj Mehta\n")
    myFile.write("Sam Tempestini\n")
    #close file
    myFile.close()

#run program
main()
