import time

count = int(input("Count down for:"))

for i in range(count,0,-1):
    print(i, end=' ')
    for j in range(i):
        print('*', end=' '),
    print()
    time.sleep(1)