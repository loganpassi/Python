#Logan Passi
#09/17/19
#powRecursion.py
#Short program to calculate the a value to a given exponent via recursion. For practice.

def powRecN(num, exp): #takes n steps
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * powRecN(num, exp - 1)

    return num

def powRecLogN(num, exp): #takes log(n) steps
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0: #rather than iterating through the exponent, cut it in half and
        temp = exp // 2
        num *= num
        return powRecLogN(num, temp)
    else:
        temp = exp - 1 #if the exponent is negative subtract one so it will be positive
        return num * powRecLogN(num, temp)

print(powRecN(5, 2))
print(powRecLogN(2, 5))