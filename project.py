import random
import time

message = {1 : "Keep going. You've got this!!", 2 : 'Keep up the spirit!', 3 : 'GG!!', 4 : "Don't you give up soon!!", 5 : "You're almost there!!"}
time.sleep(1)
print('Whomst has summoned the almighty one...')
time.sleep(1)
print("Smudge Lord here, the coolest meme cat in business. Your name please! ^_^ : ",end=' ')
name = input()
print('Hi '+name+'! Glad meeting you.')
time.sleep(1)
print('Lemme make it clear for you.')
time.sleep(1)
print("You've got to guess a number from 1 to 100.")
time.sleep(1)
print("You're granted 100 points and 10 chances to guess the number with each chance costing you 10 points.")
time.sleep(1)
res = input('Ready to play? ')
if(res == 'no' or res == 'No' or res == 'NO'):
    print('Adios!')
    time.sleep(1)
    exit()
while(1):
    point = 100
    x = random.randint(1, 100)
    i = 0
    for i in range(1,10):
        time.sleep(1)
        guess = int(input('Enter your guess: '))
        if x == guess:
            print('Purrfect! You guessed it right in ' +str(i) + ' tries.')
            time.sleep(1)
            print('--------- '+name+"'s score: "+str(point)+' ---------')
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
        time.sleep(1)
        print("The number is "+x)
        print("Better Luck Next time!")
    time.sleep(1)
    res = input('Play again? ')
    if(res == 'no' or res == 'No' or res == 'NO'):
        print('Adios!')
        time.sleep(1)
        break
