def printing(list):
    str = ''
    for i in range(0, len(list)-1):
        str += list[i]+', '
    str += 'and '+ list[len(list)-1]
    return  str

l = ['hello', 'shit', 'who', 'where']
s = printing(l)
print(s)