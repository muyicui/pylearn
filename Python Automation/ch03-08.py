import random
secret = random.randint(1,20)
print('I am thinking a number from 1 to 20')

for guessTaken in range(1,7):
    guess = int(input('Take a guess!'))

    if guess < secret:
        print('Your guess is too low')
    elif guess > secret:
        print('Your guess is too high')
    else:
        break

if guess == secret:
    print('Good job, you guess my number in '+str(guessTaken)+' 10guesses!')
else:
    print('Nope, the number I was thinking number '+str(secret))