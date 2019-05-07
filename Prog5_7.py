#Logan Passi
#09/21/2016
#Prog5_7.py

def main():
    password = ''
    while True:
        #get password
        password = input('Enter the password:')
        #verify password
        if password == 'prospero':
            break #breaks out of infinite loop
        else:
            print('Incorrect password')
    print('Password confirmed!')

#start program by calling the main function
main()
