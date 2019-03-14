import os
print('print join path')

print(os.path.join('usr','bin','spam'))
print('\n')
print('print get cwd')
print(os.getcwd())
print('\n')
#os.chdir('/')
#print(os.getcwd())

print(os.path.dirname(os.getcwd()))
print(os.path.basename(os.getcwd()))
print(os.getcwd().split(os.path.sep))
print(os.path.getsize(os.path.join(os.getcwd(),'ch03-11.py')))
print(os.listdir(os.getcwd()))

totalsize = 0
for filename in os.listdir(os.getcwd()):
    totalsize = totalsize + os.path.getsize(os.path.join(os.getcwd(),filename))

os.chdir('/Users/muyi')
helloFile = open(os.path.join(os.getcwd(),'helloworld.txt'))
print(helloFile.readlines())

helloFile = open(os.path.join(os.getcwd(),'helloworld.txt'), 'a')
helloFile.write("Huanran is Shafufu")
helloFile.close()
helloFile = open(os.path.join(os.getcwd(),'helloworld.txt'), 'r')
print(helloFile.read())
helloFile.close()