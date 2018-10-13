number = int(input("Which multiplication table would you like?"))
length = int(input("How high do you want to go?"))
for i in range(1,length+1):
    print(number,'*',i ,'=',number*i)