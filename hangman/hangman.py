#Logan Passi
#10/24/2016
#CIS1400-003
#hangman game
import random
import linecache
def main():
    counter = int()
    index = int()
    error = int()
    guessCount = int()
    guessIndex = int()
    guessTotal = int()
    allGuessCounter = int()
    guess = ""
    guessArray = [0]
    index = int()
    guessEnumerate = [0]
    word = ""
    word = choice(word)
    word = word[:-1] #takes off the \n at the end of each word in the text file
    code = input("Enter in the dev code to see the word or press enter to skip:")
    if code == "apple":
        print(word)
    length = len(word) #finds the length of the word
    underArray = ["_"] * length
    jointWordLength = len(list(set(word))) #amount of different letters in the array
    guessArray = ["_"] * (jointWordLength + 5)
    print ("\nThe length of the word is",length,"letters.")
    print("\nThere are",jointWordLength,"different letters.")  
    print("\nYou have 6 misguesses until you lose.")
    while counter in range(0,jointWordLength):
        guessTotal = counter + error + 1
        guess = input("\nPlease input a single letter:")
        guess = guess.lower() #converts guess to lowercase
        guess, index = guessMultipleCheck(guess, allGuessCounter, guessArray, index, word)
        index += 1
        guessCount = (word.count(guess)) #counts how many times the guessed letter is found in the word
        if guessCount >= 1:
            if guessCount == 1:
                print("\nNice, there is 1 \"",guess,"\" .")
            else:    
                print("\nNice, there are",guessCount,"\"",guess,"\"'s.")
            counter += 1
        else:
            print("\nSorry, the letter \"",guess,"\" is not in the",length,"letter word.")
            error += 1 #error increment
        allGuessCounter += 1
        errorDisplay(error, word)
        underScore(word, length, guess, underArray)
        print("\nPrevious guesses:")
        print(guessArray)
    if counter == jointWordLength:
        print("Congratulations!!\nYou have correctly guessed the word \"",word,"\" in",guessTotal,"tries .")
        restartValid()
    
def restartValid():
    restart = input("Would you like to play again? (y/n)") #determines whether they choose to restart the game or not
    print("**********************************************************")
    if restart == "y" or restart == "Y":
        main()
    else:
        exit()
def guessMultipleCheck(guess, allGuessCounter, guessArray, index, word): #checks if the guess entered is more than one character
    while len(guess) != 1 or guess == "" or guess == " ": #if not a single letter is entered it will display this --|
        guess = input("Please input a SINGLE letter:") # <----------------------------------------------------------|
    guess, index = guessDuplicateCheck(guessArray, guess, index, word, allGuessCounter)
    return guess, index

def guessDuplicateCheck(guessArray, guess, index, word, allGuessCounter): #checks if the guess entered had already been entered
        while guessArray.count(guess) >= 1 and index > 0:
            print("That letter has already been guessed,")
            guess = input("please guess another letter:")
        if len(guess) != 1 or guess == "" or guess == " ":
            guess, index = guessMultipleCheck(guess, allGuessCounter, guessArray, index, word)
        guessArray[index] = guess
        allGuessCounter += 1
        return guess, index
    
def extreme_list(word):
    print("\nYou have chosen extrememe difficulty.\nGood luck, you're going to need it.\n")
    num = int((random.randint(1,58109))) #randomly picks a number
    wordDatabase = open("words_extreme.txt", "r") #opens the file for read only
    word = linecache.getline("words_extreme.txt", num) #grabs the word on the randomly selected line
    wordDatabase.close() #closes external file
    return word

def hard_list(word):
    print("\nYou have chosen hard difficulty.\nIt is not to be taken lightly.\n")
    num = int((random.randint(1,100))) #randomly picks a number
    wordDatabase = open("words_hard.txt", "r") #opens the file for read only
    word = linecache.getline("words_hard.txt", num) #grabs the word on the randomly selected line
    wordDatabase.close() #closes external file
    return word
    
def medium_list(word):
    print("\nYou have chosen medium difficulty.\nThis is for the average player.\n")
    num = int((random.randint(1,45))) #randomly picks a number
    wordDatabase = open("words_medium.txt", "r") #opens the file for read only
    word = linecache.getline("words_medium.txt", num) #grabs the word on the randomly selected line
    wordDatabase.close() #closes external file
    return word
    
def easy_list(word):
    print("\nYou have chosen easy difficulty.\nYou better not lose.\n")
    num = int((random.randint(1,35))) #randomly picks a number
    wordDatabase = open("words_easy.txt", "r") #opens the file for read only
    word = linecache.getline("words_easy.txt", num) #grabs the word on the randomly selected line
    wordDatabase.close() #closes external file
    return word
    
def underScore(word, length, guess, underArray):
    for index in range(0, length):
        if guess == word[index]:
            underArray[index] = guess
    print(underArray)

def guessIndexFinder(word, guess, length):
    for index in range(0, length):
        if guess == word[index]:
            tempIndex = index
    return tempIndex

def errorDisplay(error, word): #pritns out hangman
    if error == 0:
        print(" _____")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("-----┴-----")
        
    elif error == 1:
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("-----┴-----")

    elif error == 2:
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("/    |")
        print("     |")
        print("     |")
        print("     |")
        print("-----┴-----")

    elif error == 3:
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("/ \  |")
        print("     |")
        print("     |")
        print("     |")
        print("-----┴-----")

    elif error == 4:
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print(" |   |")
        print("     |")
        print("     |")
        print("-----┴-----")

    elif error == 5:
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print(" |   |")
        print("/    |")
        print("     |")
        print("-----┴-----")
            
    elif error == 6:
        print("Sorry, the word was \"",word,"\" but you have guessed incorrectly too many times.")
        print(" _____")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print(" |   |")
        print("/ \  |")
        print("     |")
        print("-----┴-----")
        restartValid()

def choice(word):
    dif = input("Please choose a difficulty, (1)easy, (2)medium, (3)hard, (4)extreme:")
    while True:
        if dif == "1":
            word = easy_list(word)
            break
        elif dif == "2":
            word = medium_list(word)
            break
        elif dif == "3":
            word = hard_list(word)
            break
        elif dif == "4":
            word = extreme_list(word)
            break
        else:
            dif = input("Please choose a difficulty, (1)easy, (2)medium, (3)hard, (4)extreme:")
    return word
    
main()
