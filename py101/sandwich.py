
def make_me_a_sandwich():
    get_bread()
    get_butter_knife()
    get_peanut_butter()
    spread_pb_on_bread()
    get_bread()
    get_butter_knife()
    get_peanut_butter()
    spread_jelly_on_bread()
    put_on_other_bread()

def cleanup():
    print("Put away peanut butter")
    print("put away jelly")
    print("put away butter knife")
    print("put away bread")
    
    
def get_bread():
    print("Got bread")

def get_butter_knife():
    print("Got butterknife")
    
def get_peanut_butter():
    print("Got peanut butter")
    
def spread_pb_on_bread():
    print("Spread peanut butter on bread")
    
def spread_jelly_on_bread():
    print("Spread spread jelly on bread")
    
def put_on_other_bread():
    print("Put on other bread")

for i in range(0, 1):
    make_me_a_sandwich()
    print("****made {} sandwiches so far....".format(i))

cleanup()



    
    