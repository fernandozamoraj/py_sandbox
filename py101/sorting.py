from util import reverse

names = ['jesse', 'mike', 'joe', 'marco']

print "Names:"
print names

x = reverse(names)
print ""
print "Names Reversed: "
print x

x = sorted(x)
print ""
print "Sorted:"
print x

x = reverse(x)
print ""
print "Sorted Descending:"
print x

#sort in place
x.sort();
print ""
print "x.sort()"
print x

x = sorted(x, reverse=True)
print ""
print "Sorted in reverse"
print x

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
	#this is equivalent to .toString in other languages like Java and C#
    #this will help print out the object how you want it to be printed out 	
    def __repr__(self):
        return repr((self.firstName, self.lastName))
		
		
		
persons = [
    Person('Mike', 'Jones'),
	Person('OShea', 'Jackson'),
	Person('Calvin', 'Broadus'),
	Person('Curtis', 'Jackson'),
	Person('James', 'Smith'),
]		

persons = sorted(persons, key=lambda student: student.lastName)
print ""
print "Persons sorted by lastName:"
print persons

persons = sorted(persons, key=lambda student: student.firstName)
print ""
print "Persons sorted by firstName:"
print persons
