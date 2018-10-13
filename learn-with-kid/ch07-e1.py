price = int(input('give me your price'))
if price <= 10:
    price = price * 0.9
    print('you got 10% off, your price is',price)
else:
    price = price * 0.8
    print('you get 20% off, your price is', price)