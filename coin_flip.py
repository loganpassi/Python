##Logan Passi
##09/28/2016
##Prog6_5.py
##In class exercise to demonstrate the use of
##the random function when simulating a coin toss.

import random #make random functions accessible
def main():
    NUM_FLIPS = 10 #Python named constant
    counter  = int() #counter variable
    numHeads = int(); numTails = int()
    headPer = int(); tailPer = int()
    # toss coin specific number of times
    for counter in range(1, NUM_FLIPS + 1):
        # 'flip' coin
        if random.randint(1, 2) == 1:
            print('HEADS')
            numHeads += 1
        else:
            print('TAILS')
            numTails += 1

    headPer = numHeads * 10
    tailPer = numTails * 10
    print('Heads:', numHeads, '\t%',headPer,'\nTails:', numTails, '\t%',tailPer)

    

main()
