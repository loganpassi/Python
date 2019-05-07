# Author:  Logan Passi
# Date:    11/21/2016
# Program: Grade.py
# Descr:
# Python class definition for
# superclass GradedActivity and
# subclass FinalExam.

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
 
# create subclass of GradedActivity
class FinalExam(GradedActivity):
    # conststructor
    def __init__(self, questions, missed):
        # set private data members
        self.__numQuestions = questions
        self.__numMissed = missed
        self.__pointsEach = 100.0/questions
        # set inherited score-->use public mutator/setter
        self.setScore(100 - (missed * self.__pointsEach))
    # accessor methods
    def getPointsEach(self):
        return self.__pointsEach
    def getNumMissed(self):
        return self.__numMissed
    #override the method from the parent class
    def getGrade(self):
        if self.getScore() >= 95:
            grade = "A"
        elif self.getScore() >= 85:
            grade = "B"
        elif self.getScore() >= 75:
            grade = "C"
        elif self.getScore() >= 65:
            grade = "D"
        else:
            grade = "F"

#create subclass of graded activity
#Lab class has maximum 10 points
#which is scaled to 100 for
#grade calculatoin from GradedActivity
class LabAssign(GradedActivity):
    #consctructor (Python initializer)
    def __init__(self, points):
        #set private attributer of GradedActivity
        self.setScore(points * 10)
        
