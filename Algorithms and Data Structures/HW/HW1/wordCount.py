#Logan Passi
#CPSC-34000
#08/30/19
#wordCount.py
#P-1.36: Write a Python program that inputs a list of words, separated by whitespace,and outputs how many times
#each word appears in the list. You need not worry about efficiency at this point, however, as this topic
#is something that will be addressed later in this book.

wordList = []
currentWordList = []
currentWordStr = ""
count = 0

def wordCheck(i, wordList, currentWordStr): #function to check if the current word has already been printed,
    for a in range(0, i): #loop through the first and position of the current word
        if ''.join(wordList[a]) == currentWordStr:
            return False

    return True


inpString = str(input("Please enter in a list of words, each word should be separated by a space:"))
for n in range(len(inpString)): #loop through the entire string and convert individual words into a single string
    if inpString[n] != ' ':
        currentWordList.append(inpString[n]) #loop through the characters that are not spaces and append them to a list
    else:
        currentWordStr = ''.join(currentWordList) #convert the list of characters into a string
        currentWordList.clear() #clear the list so it can be populated by the next word
        wordList.append(currentWordStr) #append the string of the word to a single element of a new list

currentWordStr = ''.join(currentWordList)
currentWordList.clear()
wordList.append(currentWordStr)

print("Number of times each word was used")

for i in range(len(wordList)): #loop through the list of words
    currentWordStr = ''.join(wordList[i])
    for j in range(len(wordList)):
        if wordList[i] == wordList[j]: #count how many times each word appears
            count += 1

    if i == 0 or wordCheck(i, wordList, currentWordStr) == True:
        print(currentWordStr + ": " + str(count)) #print each word only once with how many times it appears
    count = 0

#Please enter in a list of words, each word should be separated by a space:big big small large large small big small
#Number of times each word was used
#big: 3
#small: 3
#large: 2