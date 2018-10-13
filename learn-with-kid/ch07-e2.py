sex = input('tell me your gender?(m/f)')
if sex == 'm':
    print('sorry it is girl\'s game')
else:
    age = int(input("tell me your age?"))
    if 10<= age <= 12:
        print('welcome to the team')
    else:
        print("your age is not eligible for the game")