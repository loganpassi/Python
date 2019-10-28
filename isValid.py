#Logan Passi
#10/28/19
#isValid.py
#Short Program to check if a mathematical statement is valid regarding its parenthesis
from queue import LifoQueue

def main():
    exprStr = "1+2"
    print(isValid(exprStr))
    exprStr = "(1+2))"
    print(isValid(exprStr))

def isValid(exprStr):
    myStack = LifoQueue()
    for i in range(len(exprStr)):
        if exprStr[i] == "(":
            myStack.put(exprStr[i])
        elif exprStr[i] == ")":
            if myStack.get() != "(" or myStack.empty() == True:
                return False
    if myStack.empty() != True:
        return False
    return True

main()