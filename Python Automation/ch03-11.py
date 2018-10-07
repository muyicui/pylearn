def collatz(num):
    if num % 2 == 0:
        return (num // 2)
    else:
        return (num * 3 + 1)

number = int(input('give me a number'))

while number != 1:
    number = collatz(number)
    print(number)
