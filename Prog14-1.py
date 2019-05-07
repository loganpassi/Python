#Logan Passi
#11/14/2016
#Prog14_2.py
#In class exercise to create a CellPhone class
#and use this class to create an object in a
#small program.

#define CellPhone class
class CellPhone:
    #constructor to initialize attributes when object is created
    #python uses __init__method to
    #automatically invoke and initialize attributes
    def __init__(self, manufact, model, retail):
        self.__manufacturer = manufact
        self.__modelNumber = model
        self.__retailPrice = retail

    #create methods/setter methods
    def setManufacturer(self, manufact):
        #NOTE: "self" refers to the object upon
        #       which the function is called
        self.__manufacturer = manufact
        #NOTE: Python convention uses two
        #       underscores to indicate "private"
        #       for attribute
    def setModelNumber(self, model):
        self.__modelNumber = model

    def setRetailPrice(self, retail):
        self.__retailPrice = retail

    #create accessors/getter methods
    def getManufacturer(self):
        return self.__manufacturer

    def getModelNumber(self):
        return self.__modelNumber

    def getRetailPrice(self):
        return self.__retailPrice

def main():
    #create an object of the type CellPhone class
    #use constructor to initialize object attributes
    myPhone = CellPhone("Motorolla", "M1000", 199.99)
    phoneArr = [CellPhone("Motorola", "M1000", 199.99),
                CellPhone("Samsung", "S6", 700.00),
                CellPhone("Apple", "7", 700.00)]
    #set attributes using mutators/setters
##    myPhone.setManufacturer("Motorola")
##    myPhone.setModelNumber("M1000")
##    myPhone.setRetailPrice(199.99)

    #display attributes using accessors/gettors
    print("The manufacturer is", myPhone.getManufacturer())
    print("The model number is", myPhone.getModelNumber())
    print("The retail price is", myPhone.getRetailPrice())

    #display phoneArr
    for cntr in range(0, 3):
                print("Manufacturer:", phoneArr[cntr].getManufacturer())
                print("Model Number:", phoneArr[cntr].getModelNumber())
                print("Retail Price:", phoneArr[cntr].getRetailPrice())

main()
