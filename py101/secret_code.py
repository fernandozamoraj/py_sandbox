secret_codes = {"nana": "1234", "jahleel": "1999", "fernando": "1777", "peewee":"2243"}

def ask_secret_code():
    print("Enter secret code")
    return input()
    
def ask_name():
    print("Enter your name")
    return input()
    
def get_secret_code(name):
    if(name in secret_codes.keys()):
        return secret_codes[name]
    return "$$$$$$"
    
attempts = {"":""}


while(True):
    name = ask_name()
    name_in_system = False
    
    if(name in secret_codes.keys()):
        secret_code = ask_secret_code()
        name_in_system = True
       
    
    if(name in attempts.keys() and attempts[name] > 2):
        print("ACCESSS DENIED. TOO MANY ATTEMPTS")
    
    if(name_in_system == True and secret_code == get_secret_code(name)):
        print("You have entered the secret area")
        if(name in attempts.keys()):
            attempts[name] = 0
    else:
        if(name in attempts.keys()):
            attempts[name] = attempts[name] + 1
        else:
            attempts[name] = 1
        print("You cannot enter without the secret code")
        
    print(attempts)
     
    if( name in attempts.keys() and attempts[name] > 1):
        print("You are about to be locked out")   
        
           
    