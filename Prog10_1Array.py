##Logan Passi
##10/26/2016
##Prog10_1Array.py
##In class exercise to write out elements from an array to a file

def main():
    #array of names
    names = ['Logan Passi', 'Usman Effendi', 'Michael McGough', 'Nick Mares']
    #named constant
    MAX_NAMES = 4
    #file open for output --> full pathname
    myFile = open("C:\\Insight Files\\philosophers.dat", "w")
    #write data from array to file
    for counter in range(0, MAX_NAMES):
        myFile.write(names[counter] + "\n")
    #close file
    myFile.close()
    print("Output written to file.")
main()
