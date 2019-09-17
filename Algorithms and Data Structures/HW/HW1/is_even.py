#Logan Passi
#CPSC-34000
#08/27/19
#is_even.py
#Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#use the multiplication, modulo, or division operators.

#function to check if the entered value is even
def is_even(k):
    isEven = 0
    binary_val = format(k, 'b') #convert the entered integer to binary
    string_val = str(binary_val) #convert the binary to a string
    last_val = int(string_val[len(string_val) - 1]) #get the last character of the string
    if last_val != 0: #if the last character is a 0, the number is even, if it is 1, the number is odd
        isEven = 1
    return isEven

entered_value = int(input("Please enter an integer value: "))
if is_even(entered_value) == 0:
    print("The entered value, " + str(entered_value) + ", is even.")
else:
    print("The entered value, " + str(entered_value) + ", is odd.")

#Please enter an integer value: 4
#The entered value, 4, is even.

#Please enter an integer value: 7
#The entered value, 7, is odd.