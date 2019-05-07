#Logan Passi
#10/30/2016
#TestAve.py
#In class exersize to create a test average calculator
#using "from" allows use of class name directly
#without need for filename and dot.
from tkinter import *
class TestAvg_GUI:
    def __init__(self):
        #create window and set title
        self.mainWindow = Tk()
        self.mainWindow.title("Test Average")
        self.mainWindow.geometry("200x110")

        #create the test labels and text boxes
        self.test1Label = Label(self.mainWindow, \
                                text = "Enter the score for test 1")
        self.test1TextBox = Entry(self.mainWindow, width= 10)
        #place components in grid
        self.test1Label.grid(row = 0, column = 0)
        self.test1TextBox.grid(row = 0, column = 1)

        self.test2Label = Label(self.mainWindow, \
                                text = "Enter the score for test 2")
        self.test2TextBox = Entry(self.mainWindow, width= 10)
        #place components in grid
        self.test2Label.grid(row = 1, column = 0)
        self.test2TextBox.grid(row = 1, column = 1)

        self.test3Label = Label(self.mainWindow, \
                                text = "Enter the score for test 3")
        self.test3TextBox = Entry(self.mainWindow, width= 10)
        #place components in grid
        self.test3Label.grid(row = 2, column = 0)
        self.test3TextBox.grid(row = 2, column = 1)

        #average labels
        self.resultLabel1 = Label(self.mainWindow, text = "Average")
        self.averageLabel = Label(self.mainWindow, text = " ")

        self.resultLabel1.grid(row = 3, column = 0)
        self.averageLabel.grid(row = 3, column =1)

        #buttons
        self.calcButton = Button(self.mainWindow, text = "Calculate Average", \
                                 command = self.calcButton_Click)
        self.exitButton = Button(self.mainWindow, text = "ʇᴉxƎ", \
                                 command = self.mainWindow.destroy)
        self.calcButton.grid(row = 4, column = 0)
        self.exitButton.grid(row = 4, column = 1)
        
        #Enter the main loop
        self.mainWindow.mainloop()
    
    #event handler to execute when the
    #calc button is clicked
    def calcButton_Click(self):
        #get test
        test1 = float(self.test1TextBox.get())
        test2 = float(self.test2TextBox.get())
        test3 = float(self.test3TextBox.get())
        #calculate the average
        average = (test1 + test2 + test3) / 3
        #update the display with calculated average
        self.averageLabel.configure(text = format(average, ".2f"))
        
        
#main module
def main():
    myTestAvg = TestAvg_GUI()

main()
