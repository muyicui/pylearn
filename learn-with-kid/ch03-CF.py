#convert between C and F
temp = 0
while temp != 'C' and temp != 'F':
    print("please tell me what you want C or F")
    temp = input("you have C or F(C/F)")
    print(type(temp))
number = int(input("give me your temprature"))
if temp == "F":
    number = 5/9*(number - 32)
else:
    number = 9/5*number + 32
print(number)

