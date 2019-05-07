from tkinter import *
class propertyTaxCalc_GUI:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Property Tax Calculator")
        self.mainWindow.geometry("200x110")

        
        #Property Value
        self.propertyValueLabel = Label(self.mainWindow, text =\
                            "Enter the property value:")
        self.propertyValueTextBox = Entry(self.mainWindow, width = 10)
        self.propertyValueLabel.grid(row = 0, column = 0)
        self.propertyValueTextBox.grid(row = 0, column = 1)

        
        #Assessment Value
        self.assessmentValueLabel = Label(self.mainWindow, text =\
                                          "Assessment Value:")
        self.assessmentValueDisplay = Label(self.mainWindow, text =\
                                            " ")
        self.assessmentValueLabel.grid(row = 1, column = 0)
        self.assessmentValueDisplay.grid(row = 1, column = 1)

        
        #Tax Value
        self.taxValueLabel = Label(self.mainWindow, text =\
                                   "Tax Value:")
        self.taxValueDisplay = Label(self.mainWindow, text =\
                                     " ")
        self.taxValueLabel.grid(row = 2, column = 0)
        self.taxValueDisplay.grid(row = 2, column = 1)

        
        #Calculate & Exit
        self.calcButton = Button(self.mainWindow, text = "Calculate",\
                                 command = self.calcButton_Click)
        self.exitButton = Button(self.mainWindow, text = "Exit",\
                                 command = self.mainWindow.destroy)
        self.calcButton.grid(row = 3, column = 0)
        self.exitButton.grid(row = 3, column = 1)
        
        #loop
        self.mainWindow.mainloop()

    def calcButton_Click(self):
        propertyValue = float(self.propertyValueTextBox.get())
        assessmentValue = float(propertyValue * .6)
        taxValue = float(assessmentValue * .0064)
        self.assessmentValueDisplay.configure(text = \
            format(assessmentValue, ".2f"))
        self.taxValueDisplay.configure(text = \
            format(taxValue, ".2f"))

def main():
    myPropertyTaxCalc = propertyTaxCalc_GUI()

main()
        
        

        
