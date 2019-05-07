def main():
    firstAge = int(); secondAge = int(); total = int()
    firstAge = int(input("Enter the first age:"))
    secondAge = int(input("Enter the second age:"))
    total = sum2num(firstAge, secondAge)
    print("Sum of the two ages is", total)

def sum2num(num1, num2):
    result = int()
    result = num1 + num2
    return result
main()
    
