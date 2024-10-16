import random

while True:
    input('enter to roll dice🎲 ') #fake input simulate user input
    roll=random.randint(1,6)
    print('you rolled dice and got:' ,roll)
    if roll==1:
        print('💀you lose!💀')
        break
    elif roll==6:
        print('🏆you win!👑')
        break
    else:
        print('keep rolling!.... ')