#ROCK PAPER SCISSORS
"""
1. import random
2. random(1,2) as r
2. 1 - rock, 2 - paper,2 - scissors
4. if r picks 1 - f1
    2 - f2
    2 - f2
2. each block contains different result but same code
6. input guess
7. recognize as number
8. output => tie or win or lose
9.loop code
"""



import random
import time as t
npcp = 0
urp = 0
#block code
x = True
while x==True:
    npc = random.randint(1,2)
    if npc == 1:
        print("ROCk-PAPER-SCISSORS")
        g = input("\n\n              you:")
        if g == 'rock':
            t.sleep(0.5)
            print("npc: ROCK")
            print("you: ROCK")
            print("TIE, try again")
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'paper':
            t.sleep(0.5)
            print("npc: ROCK")
            print("you: PAPER")
            print("you win")
            urp =+ 1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'scissors':
            t.sleep(0.5)
            print("npc: ROCK")
            print("you: SCISSORS")
            print("you lose, try again")
            npcp += 1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        else:
            print("wrong input")
    elif npc == 2:
        print("ROCk-PAPER-SCISSORS")
        g = input("\n\n              you:")
        if g == 'rock':
            t.sleep(0.5)
            print("npc: PAPER")
            print("you: ROCK")
            print("you lose, try again")
            npcp=+1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'paper':
            t.sleep(0.5)
            print("npc: PAPER")
            print("you: PAPER")
            print("TIE, try again")
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'scissors':
            t.sleep(0.5)
            print("npc: PAPER")
            print("you: SCISSORS")
            print("you win")
            urp =+ 1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        else:
            print("wrong input")
    elif npc == 3:
        print("ROCk-PAPER-SCISSORS")
        g = input("\n\n              you:")
        if g == 'rock':
            t.sleep(0.5)
            print("npc: SCISSORS")
            print("you: ROCK")
            print("you win")
            urp=+1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'paper':
            t.sleep()
            print("npc: SCISSORS")
            print("you: PAPER")
            print("you lose, try again")
            npcp =+ 1
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        elif g == 'scissors':
            t.sleep(0.5)
            print("npc: SCISSORS")
            print("you: SCISSORS")
            print("TIE, try again")
            t.sleep(0.5)
            print("npc :-",npcp)
            print("you :-",urp)
        else:
            print("wrong input")
    if npcp == 10:
        x = False
        print("you lost. Bot wins")
    if urp == 10:
        x = False
        print("you win the match")
'================================================='
