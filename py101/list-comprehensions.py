
capitalizedNames = [name.capitalize() for name in ['joe', 'jane', 'mary', 'dan']]

print 'Capitalized Names: {0}'.format(capitalizedNames)

#uses condition to filter out names that end with 'y'
#the logic is not right because it does not pick up jane... just an example
girlnames = [name.capitalize() for name in ['joe', 'jane', 'mary', 'dan'] if name[-1] == 'y']

print 'Girl Names: {0}'.format(girlnames)