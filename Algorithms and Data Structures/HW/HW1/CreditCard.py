#Logan Passi
#CPSC-34000
#08/28/19
#CreditCard.py
#Use the techniques of Section 1.7, (exception handling), to revise the charge and make payment
#methods of the CreditCard class to ensure that the caller sends a number
#as a parameter.

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def charge(self, price):
        if not isinstance(price, (int, float)): #if the instance of the price is not a float or int raise an error
            raise TypeError("Price must be numeric!")
        elif price < 0: #if the value of the price is less than zero raise an error
            raise ValueError("Price cannot be negative!")

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)): #if the instance of the amount is not a float or int raise an error
            raise TypeError("Price must be numeric!")
        elif amount < 0: #if the value of the amount is less than zero raise an error
            raise ValueError("Price cannot be negative!")

        self._balance -= amount

#myCC = CreditCard('Logan Passi', 'Chase Bank', '1234 5678 9123 4567', 1000)
#myCC.charge('a')
#myCC.make_payment('34e')

#Traceback (most recent call last):
#  File "C:/Users/Logan/PycharmProjects/Proj1/CreditCard.py", line 39, in <module>
#    myCC.charge('a')
#  File "C:/Users/Logan/PycharmProjects/Proj1/CreditCard.py", line 20, in charge
#    raise TypeError("Price must be numeric!")
#TypeError: Price must be numeric!

#Traceback (most recent call last):
#  File "C:/Users/Logan/PycharmProjects/Proj1/CreditCard.py", line 40, in <module>
#    myCC.make_payment('34e')
#  File "C:/Users/Logan/PycharmProjects/Proj1/CreditCard.py", line 32, in make_payment
#    raise TypeError("Price must be numeric!")
#TypeError: Price must be numeric!