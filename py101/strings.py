#              111111111122222222223333333333444      
#    0123456789012345678901234567890123456789012
# this process is called slicing
# slicing has the following values target[start:end]
# target: this can be anything that is a collection such as a list or a string
# start: this is the starting index of the sub collection
# end: this is the end of the substring (exclusive)
#      end can also be represented by a 
#      negative number which counts from the end of the string
# This is similar to the String.subString of C# and Java. 
# However this also works on other collections, not just strings
#
x = "The quick brown fox jumps over the lazy dog";

print ""
print "#               111111111122222222223333333333444"      
print "#     0123456789012345678901234567890123456789012"
print "x = \"The quick brown fox jumps over the lazy dog\"";


print ""
print "fox x[16:19]"
print x[16:19]

print ""
print "The lazy dog: x[31:]"
print x[31:]

print ""
print "The quick brown fox x[:-24]:"
print x[:-24]

#similar to x.contains("y") in Java and C#
if "quick brown" in x:
    print "x contains \"quick brown\""

if "slow brown" not in x:
    print "x does not contain \"slow brown\""
	
	
print ""
print "The quick brown fox x[:-24].upper()"
print x[:-24].upper()

print ""
print "The quick brown fox x[:-24].lower()"
print x[:-24].lower()

print ""
print "The quick brown fox x[:-24].capitalize()"
print x[:-24].capitalize()



print ""
print "String comparisons"
a = "joe"
b = "joe"
c = "mike"

if a == b:
    print "a equals b"
else:
    print "a does not equal b"
	
if a == c:
    print "a equals c"
else:
    print "a does not equal c"
	
if a is b:
    print "a is b"
else:
    print "a is not b"

if a is c:
    print "a is c"
else:
    print "a is not c"	
	
if a > c:
    print "a:" + a + " is greater than c:" + c
else: 
    print "a:" + a + " is not greater than c:" + c
	
#splits on ' '
print ""
print "x.split()"	
print x.split()

#splits on 'the'
print ""
print "x.lower().split(\'the\')"
print x.lower().split('the')

print ""
print "x.index(\'fox\')"
print x.index('fox')

print ""
print "len(x)"
print len(x)






