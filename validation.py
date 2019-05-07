#Logan Passi
#10/03/2016
#Validation.py
#In class exercise to demonstrate the use of validation
#of input

def main():
    score = input("Enter a test score:")
    #check for valid input
    #while score < 0 or score > 100:
    while isInvalid(score):
        print("ERROR! The score cannot be less than 0 or greater than 100!")
        score = input("Enter the correct score:")
    #display the correct score
    print(score, "is a valid score.")

#check for invalid score
def isInvalid(score):
    #temporarily remove decimal point before numeric check
    if not score.replace(".", "").isnumeric() \
       or if score < 0 or score > 100:
            status = True
        else:
            status = False
    return status

main()
