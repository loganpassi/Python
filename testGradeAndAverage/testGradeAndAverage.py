#Logan Passi
#09/28/2016
#testGradeAndAverage.py
#CIS1400-003
#This program will take your test scores and give you a letter grade
#for each score aswell as the average of all the scores

def main():
    score1 = float(getValidScore())
    grade = determineGrade(score1)
    print("\t\t\t\tGRADE")
    print("\t\t\t\t-----")
    print("\t\t\t\t ",grade)
    
    score2 = float(getValidScore())
    grade = determineGrade(score2)
    print("\t\t\t\tGRADE")
    print("\t\t\t\t-----")
    print("\t\t\t\t ",grade)
    
    score3 = float(getValidScore())
    grade = determineGrade(score3)
    print("\t\t\t\tGRADE")
    print("\t\t\t\t-----")
    print("\t\t\t\t ",grade)
    
    score4 = float(getValidScore())
    grade = determineGrade(score4)
    print("\t\t\t\tGRADE")
    print("\t\t\t\t-----")
    print("\t\t\t\t ",grade)
    
    score5 = float(getValidScore())
    grade = determineGrade(score5)
    print("\t\t\t\tGRADE")
    print("\t\t\t\t-----")
    print("\t\t\t\t ",grade)
    
    average = float(calcAverage(score1, score2, score3, score4, score5))
    print("The average grade is", format(average, ".2f"),"% .")

def getValidScore():
    score = input("Enter in your score:")
    while isInvalidScore(score):
        score = input("Enter in a valid score (a value 1-100):")
    return float(score)

def isInvalidScore(score):
    if not score.replace(".", "").isnumeric() \
        or float(score) < 0 or float(score) > 100:
        status = True
    else:
        status = False
    return status

def determineGrade(score):
    if score <= 100 and score >= 90:
        grade ="A"
    elif score <= 89.99 and score >= 80:
        grade ="B"
    elif score <=79.99 and score >= 70:
        grade ="C"
    elif score <=69.99 and score >= 60:
        grade ="D"
    else:
        grade ="F"
    return grade

def calcAverage(score1, score2, score3, score4, score5):
   average = (score1 + score2 + score3 + score4 + score5)/5
   return average

main()

##Enter in your score:58.65
##				GRADE
##				-----
##				 F
##Enter in your score:86.54
##				GRADE
##				-----
##				 B
##Enter in your score:205
##Enter in a valid score (a value 1-100):ljj
##Enter in a valid score (a value 1-100):65.24
##				GRADE
##				-----
##				 D
##Enter in your score:71.25
##				GRADE
##				-----
##				 C
##Enter in your score:-99
##Enter in a valid score (a value 1-100):99.15
##				GRADE
##				-----
##				 A
##The average grade is 76.17 % .
