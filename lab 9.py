#Logan Passi
#11/6/2016
#CIS 1400-003
#This program will take the array and rearrange it in alphabetical order,
#it will also check if the name entered is in the list

def main():
    num = int(1)
    guess = ""
    names = ["Ross Harrison","Hannah Beauregard", "Bob White", "Ava Fischer"\
, "Chris Rich", "Xavier Adams", "Sasha Ricci", "Danielle Porter", "Gordon Pike", "Matt Hoyle"]
    display(names, num)
    num = sortNames(names)
    display(names, num)
    check, guess = search(names, guess)
    if  check == -1:
        print("The name",guess,"is not in the list.")
    else:
        print("The name",guess,"was found at position",check + 1,".")
    restart()

def sortNames(names):
    maxElement = int()
    for maxElement in range(len(names) - 1, -1, -1):
        for index in range(0, maxElement):
            if names[index] > names[index + 1]:
                temp = names[index]
                names[index] = names[index + 1]
                names[index + 1] = temp
    return 2

def display(names, num):
    if num == 1:
        print("These are the names unsorted:\n\n",names,"\n")
    elif num == 2:
        print("These are the names sorted:\n\n",names,"\n")

def search(names, guess):
    index = int()
    guess = input("Enter in the name that you would like to search for:")
    for index in range(0, len(names)):
        if guess == names[index]:
            return index, guess
    return -1, guess


def restart():
    restart = input("Would you like to check for another name? y/n:")
    if restart == "y" or restart == "Y":
        main()
    else:
        exit()
main()
    

