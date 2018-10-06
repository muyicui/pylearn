def information(name, address, street, city, state, postcode, country):
    print(name, end=',')
    print(address, end=',')
    print(street, end=',')
    print(city,end=',')
    if state !='':
        print(state,end=',')
    else:
        print(" ",end=',')
    print(postcode,end=',')
    print(country)

information("Huanran","Minglong","Xibeijiao","Tianjin","TIanjin","300040","China")