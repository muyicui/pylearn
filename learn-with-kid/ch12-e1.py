print("Give me five names")
list = []
for i in range(5):
    name = input()
    list.append(name)

list.sort()
print("The names are",end = ' ')
for i in range(5):
    print(list[i], end = ' ')

print()
index = int(input("Replace one name, which?(0-4)"))
list[index] = input("New name is")

print("The names are",end = ' ')
for i in range(5):
    print(list[i], end = ' ')

import pygam