#Logan Passi
#CPSC-34000
#08/27/19
#vowelCount.py
#Write a short Python function that counts the number of vowels in a given
#character string.

def countVowels(inpStr, length):
    vowelList = ['a', 'e', 'i', 'o', 'u'] #list of vowels
    vowelListLength = len(vowelList)
    numVowels = 0
    for i in range(length): #loop through the entered string
        currentChar = inpStr[i]
        for j in range(vowelListLength): #loop through the vowel list
            if currentChar == vowelList[j]:
                numVowels += 1
    print("The number of vowels in the entered string is " + str(numVowels) + ".")

inpStr = str(input("Please enter a string of characters: "))
length = len(inpStr)
countVowels(inpStr, length)

#Please enter a string of characters: paragraph
#The number of vowels in the entered string is 3.

#Please enter a string of characters: frog
#The number of vowels in the entered string is 1.