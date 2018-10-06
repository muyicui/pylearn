def count(quarters, dimes,nickels,pennies):
    total = quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
    print('$',total, sep='')

count(3,4,12,2)