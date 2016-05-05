def add_logging(message):
    def logging_decorator(f):
        def wrapper(*args, **kwargs):
            print("{} f:{} args:{} kwargs: {} ".format(message, f, args, kwargs))
            x = f(*args, **kwargs)
            return x.upper()
        return wrapper
    return logging_decorator
        

@add_logging("Entering foo:\n")
def foo(fname):
    return fname
    
    
print(foo("joe"))
print(foo("mary"))
    
    
    

    