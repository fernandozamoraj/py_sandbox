def add_logging(x):
    def loggin_decorator(func):
        def wrapper(*args, **kargs):
            if x == 1:
                return
            print 'Loggin some information prior to executing function'
            return func(*args, **kargs)
	
        return wrapper
    return loggin_decorator

x = 2   
@add_logging(x)
def foo(name):
    print 'Hello {0}'.format(name)

foo('Joe')	