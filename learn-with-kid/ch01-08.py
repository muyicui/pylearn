import random
secret = random.randint(1,100)
guess = 0
tries = 0
print("I have a secret!")
print("It is a number between 1 to 99, I will give you 6 tries")
while guess != secret and tries < 6:
    guess = int(input("give me your try?"))
    if guess > secret:
        print("too high")
    elif guess< secret:
        print("too low")
    tries = tries + 1
if guess == secret:
    print("you got it")
else:
    print("you failed it")
    print("my secret is", secret)