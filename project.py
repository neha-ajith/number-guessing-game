import random
message = {1 : "Keep going. You've got this!!", 2 : 'Keep up the spirit!', 3 : 'GG!!', 4 : "Don't you give up soon!!", 5 : "You're almost there!!"}
print('Meow there!!')
print("I'm Smudge Lord, the coolest meme cat in business. Your name please! ^_^",end=' ')
name = input()
print('Hi '+name+'! Glad meeting you.')
print('Lemme tell you the rules of this game.')
print("You've got 100 points with you right at the beginning. You should guess a number from 1 to 100.")
print("You'll get 10 chances to guess the number with each chance costing you 10 points.")
res = input('Ready to play? ')
if(res == 'no' or res == 'No' or res == 'NO'):
    print('Adios!')
    exit()
while(1):
    point = 100
    x = random.randint(1, 100)
    i = 0
    for i in range(1,10):
        guess = int(input('Enter your guess: '))
        if x == guess:
            print('Purrfect! You guessed it right in ' +str(i) + ' tries. Your point: '+str(point))
            print('Now bring me some taters ;)')
            break
        elif x < guess:
            print('Oops! You guessed it too high.')
            mes = random.randint(1,5)
            print(message[mes])
            point-=10
        elif x > guess:
            print('Oops! You guessed it too low.')
            mes = random.randint(1,5)
            print(message[mes])
            point-=10
    if i >= 10:
        print("The number is "+x)
        print("Better Luck Next time!")
    res = input('Play again? ')
    if(res == 'no' or res == 'No' or res == 'NO'):
        print('Adios!')
        break
