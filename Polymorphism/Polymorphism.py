#Logan Passi
#Polymorphism.py
#In class exercise to demonstrate use of polymorphism
#in subclasses of GradedActivity
import Grade
def DisplayDetails(grAct):
    print("Score =", grAct.getScore())
    print("Grade =", grAct.getGrade())

def main():
    #get lab details
    labScore = float(input("Enter the lab score (on a 10 point scale):"))
    #create LabAssign object (aka instance)
    lab = Grade.LabAssign(labScore)

    #get exam details
    questions = int(input("Enter the number of exam questions:"))
    missed = int(input("Enter the amount of missed questions:"))
    #create a final exam object (aka instance)
    exam = Grade.FinalExam(questions, missed)

    #display grading details
    print("\nLab Details")
    DisplayDetails(lab)
    print("\nExam Details")
    DisplayDetails(exam)
    
main()
