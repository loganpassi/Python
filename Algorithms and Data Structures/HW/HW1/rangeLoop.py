#Logan Passi
#CPSC-34000
#08/28/19
#rangeLoop.py
#Modify the declaration of the first for loop in the CreditCard tests, from
#Code Fragment 2.3, so that it will eventually cause exactly one of the three
#credit cards to go over its credit limit. Which credit card is it?

from CreditCard import CreditCard

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309 2500', 2500))
    wallet.append(CreditCard('John Bowman', 'California Savings', '3485 0399 3395 1954 3500', 3500))
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309 5000', 5000))

    for val in range(1, 80):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

#wallet[2] will max out first