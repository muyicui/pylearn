size =int(input('Please input the size of your tank'))
percent = int(input("Please input the percentage of the current gas capacity"))
meter = int(input("Please let me know how many kilometer per liter"))
buffer = 5
dist = 200
drive = (size*percent/100-buffer)*meter
print('you can drive another', drive, 'km')
print('next station is', dist, 'km')

if drive > dist:
    print('Please fill in the next station')
else:
    print("get some gas!")