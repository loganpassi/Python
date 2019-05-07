# Author:  Logan Passi
# Date:    11/16/2016
# Program: Grade.py
# Descr:
# Python class definition for
# Grade class.

class GradedActivity:
    def setScore(self, s):
        self.__score = s

    def getScore(self):
        return self.__score

    def getGrade(self):
        if self.__score >= 90:
            grade = 'A'
        elif self.__score >= 80:
            grade = 'B'
        elif self.__score >= 70:
            grade = 'C'
        elif self.__score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade

#create subclass of GradedActivity
class FinalExam(GradedActivity):
    #constructor
    def __init__(self, questions, missed):
        #set private data members
        self.__numQuestions = questions
        self.__numMissed = missed
        self.__pointsEach = 100.00/questions
        #set inherited score
        self.setScore(100 - (missed * self.__pointsEach))
    #accessor methods
    def getPointsEach(self):
        return self.__pointsEach
    def getNumMissed(self):
        return self.__numMissed

#main module to create a Final Exam object
def main():
    questions = int(input("Enter the number of questions on the exam:"))
    missed = int(input("Enter the number of questions missed:"))
    #create FinalExam object
    exam = FinalExam(questions, missed)
    #display points for each questions, score and grade
    print("Points each question:",exam.getPointsEach())
    print("Exam score",exam.getScore())
    print("Exam grade",exam.getGrade())

#start program by calling main module
main()
