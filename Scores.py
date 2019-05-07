def main():
    score = float(input('Enter the test score: '))
    if score < 60:
        print('Your grade is F.')
    elif score < 70:
        print('Your grade is D.')
    elif score < 80:
        print('Your grade is C.')
    elif score < 90:
        print('Your grade is B.')
    elif score >=90:
        print('Your grade is an A.')

#call main to start
main()
