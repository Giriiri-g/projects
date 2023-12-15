from random import*
luc = randint(1,25)
chances=10
print("you have 10 chances to guess the number")
while chances > 0 :
    num = int(input("enter your guess (1-25) :"))
    if num == luc :
        print("""your guess is corret
you won the game
you won 50 rupees""")
        break
    elif num > luc :
        print("your guess is high")
        chances -= 1
        print(chances,"chances is left")
    elif num < luc :
        print("your guess is low")
        chances -= 1
        print(chances,"chances is left")
    if chances == 0 :
        print("you lost")
        print("The lucky nummber was",luc)
