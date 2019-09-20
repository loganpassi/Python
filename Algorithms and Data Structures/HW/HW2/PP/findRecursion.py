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


    for entry in os.listdir(path):
        if "." in entry:
            if entry == fName:
                print("File found!")
                for entry in os.listdir(path):
                    if "." in entry:
                        print(os.path.join(path + "\\" + entry))
                    else:
                        print(os.path.join(path + "\\" + entry + "\\"))
                exit(0)
        else:
            find(os.path.join(path + "\\" + entry), fName)
    print("File not found...")

fName = str(input("Please enter in the file name you are looking for: "))
path = str(input("Please enter in the path: "))
find(path, fName)

#Please enter in the file name you are looking for: Program.cs
#lease enter in the path: B:\Downloads\CIS2561
#File not found...
#File not found...
#File not found...
#File not found...
#File not found...
#File found!
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\App.config
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\bin\
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\ConsoleApplication3.csproj
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\obj\
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\Program.cs
#B:\Downloads\CIS2561\CIS2561\CompoundInterest\ConsoleApplication3\ConsoleApplication3\Properties\