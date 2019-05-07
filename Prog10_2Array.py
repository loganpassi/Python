##Logan Passi
##10/26/2016
##Prog10_2Array.py
##In class exercise to read in elements from frile
##into a frixed size array
def main():
    MAX_NAMES = 4
    names = [0]*MAX_NAMES
    line = ""
    counter = int()
    #open file for input
    myFile = open("C:\\Insight Files\\philosophers.dat", "r")
    # read fro mfile into array
    line = myFile.readline()
    while line != "" and counter < MAX_NAMES:
        names[counter] = line.rstrip("\n")
        counter += 1
        line = myFile.readline()
    #close file
    myFile.close()
    #diplay the names
    for index in range(0, MAX_NAMES):
        print(names[index])
main()
