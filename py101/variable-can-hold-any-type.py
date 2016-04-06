x = 'joe'

print x

x = 10

print x

x = None

print x

x = 'joe'
y = 5

#run time error
try:
    z = x + 5
except:
    print 'cannot add int to str'


#here is a gotcha about strong typing
#python can perform and on variables of different types
isTrue = x and y

print 'isTrue = {0} and {1} results in {2}'.format(x, y, isTrue)

if isTrue == True:
    print 'isTrue is True'
else:
    print 'isTrue is False'
    
y = 0

isTrue = x and y

print 'isTrue = {0} and {1} results in {2}'.format(x, y, isTrue)

if isTrue == True:
    print 'isTrue is True'
else:
    print 'isTrue is False'

#interesting that a string will evaluate to true    
if 'hey':
    print 'hey is True'
else:
    print 'hey is False'
    
if '':
    print 'empty string is True'
else:
    print 'empty string is False'
    
if None:
    print 'None is True'
else:
    print 'None is False'
    