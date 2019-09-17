#Logan Passi
#CPSC-34000
#08/27/19
#getSumSqInt.py
#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.

def getSumSqInt (n):
    ttl = 0
    for x in range(n): #loop through the entered value
        x = x**2 #square the current number
        ttl += x #add the current squared number to the total
    return ttl

while True:
   input_int = int(input("Please input a positive integer: "))
   if input_int < 0:
       print("The entered value is not positive.\n")
   else:
       break

print("The sum of the squared numbers smaller than " + str(input_int)
      + " is " + str(getSumSqInt(input_int)) + ".")

#Please input a positive integer: 3
#The sum of the squared numbers smaller than 3 is 5.



#Please input a positive integer: -2
#The entered value is not positive.
#
#
#Please input a positive integer: 8
#The sum of the squared numbers smaller than 8 is 140.