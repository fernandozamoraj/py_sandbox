#generator example
def persons():
	yield 'Fernando'
	yield 'Linda'
	yield 'Mario'
	
	
person_list = persons()

print ('{0}'.format(type(person_list)))

for person in person_list:
	print(person)
    
print('any p(.. {0}'.format(any(p == 'Fernando' for p in persons())))
print('all(len(p) > 4 ..) {0}'.format(all(len(p) > 4 for p in persons())))
print('[p for p in persons() {0}'.format([p for p in persons() if len(p) > 4]))

a, b = 5, 10

print(a)
print(b)

print(zip(['linda', 'fernando', 'mario'], ['brown', 'zamora']))
print({x[0]: x.title() for x in ['joe', 'dana', 'mario']})
