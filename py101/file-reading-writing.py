myfile = open('names.txt', 'w', 0)

myfile.write('joe\n')
myfile.write('jane\n')
myfile.write('mary\n')
myfile.write('dan\n')
myfile.write('william\n')
myfile.write('john\n')

myfile.close()


newfile = open('names.txt', 'r')

names = newfile.readlines()

newfile.close()

print names 