#Logan Passi
#09/19/19
#findRecursion.py
#Implement a recursive function with signature find(path, filename) that
#reports all entries of the file system rooted at the given path having the
#given file name.

import os

def find(path, fName):

    if path == "":
        return

    if os.path.isdir(path):
        for entry in os.listdir(path):
            print(entry)
            if os.path.join(entry + fName) == os.path.join(path + fName):
                print("File found!")
                return
            else:
                find(os.path.join(path + "\\" + entry), fName)
    else:
        print("That is not a valid directory... Exiting program!")

fName = str(input("Please enter in the file name you are looking for: "))
path = str(input("Please enter in the path: "))
find(path, fName)
