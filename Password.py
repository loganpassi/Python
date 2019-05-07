##Name: Logan Passi
##File: Password.py
##Date: 09/14/2016
##Descr:
##    Compare user input password to see if equal.
def main():
    password = ''
    password = input("Enter the password: ")
    # see if correct password entered
    if password == 'prospero':
        print('Password accepted')
    else:
        print('Sorry, that is the wrong password.')
    print('Thankyou for using the password checker.')

#must call module to begin program execution
main()
