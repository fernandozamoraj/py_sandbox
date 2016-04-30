def read_bills_file(filename):
    bills = []
    with open(filename, 'r') as f:

        #open the file and create a list of field lists
        #e.g. [["visa", "1500", "7",  "100"], ["car", "15999", "5.5", "100"]]
        #file expecations
        #account,balance,apr,monthly-payment
        #e.g.
        #visa,1500,5.7,85
        #
        lines = [i.strip().split(',') for i in f.readlines()]
        
        for line in lines:
            bill = []
            set_account_name(line[0], bill)
            convert_fields_to_numbers(line[1:], bill)
            bills.append(bill)
        
    return bills

def set_account_name(account_name, target_list):
    target_list.append(account_name)

#convert the fields to integers 
#the first field is the account name so that's a string.
#Hence why the first field is ignored
def convert_fields_to_numbers(source_list, target_list):
    for field in source_list:
        target_list.append(float(field))

def print_bill(bill):
    print(" {:12} ${:5d} {:5.1f}% ${:5d}/month".format(bill[0], int(bill[1]), float(bill[2]), int(bill[3])))
    
def print_bills():
    print("");
    print("********Bills**********")
    print("")
    
    for bill in bills:
        print_bill(bill)
        
def compute_snowball():
    snowball = 0
    
    for bill in bills:
        if(bill[1] <= 1):
            snowball += bill[3]
  
    return snowball
        
def compute_balance(bills):
    balance = 0
    for bill in bills:
        balance += bill[1]
        
    return balance

def adjust_balance(bill, snowball):
    
    payment = 0
    if(bill[1] < 1):
        return snowball, payment
        
    balance = bill[1]    
    interest = (bill[2]/100.0)/12.0
    interest_charges = balance*interest;
    bill[1] += interest_charges
  
    monthly_payment = bill[3]
        
    snowball, payment = \
          calculate_payment_and_snowball(balance, monthly_payment, snowball)
    
    bill[1] = int(bill[1] - payment) #deduct payment
   
    return snowball, payment

def calculate_payment_and_snowball(balance, monthly_payment, snowball):
    
    payment = 0
    
    if(balance >= monthly_payment):
        payment += monthly_payment
    else:
        payment += balance
        snowball += (monthly_payment - payment)
    
    if(snowball > 0 \
       and balance >= snowball):
        payment += snowball
        snowball = 0
    elif(snowball > 0 and balance > 0):
        payment += balance
        snowball = snowball - balance 

    return int(snowball), int(payment)

def create_header(payoff, bills):
    header_line = "".ljust(4)
    for bill in bills:
        header_line += '{}'.format(bill[0][:11]).center(10)
    header_line += "Balance".center(10)    
    header_line += "\n"
    header_line += ("-"*((len(bills)+1)*10))     
    payoff.append("")
    payoff.append(header_line)

def get_payoff():

    payoff = []
    create_header(payoff, bills)
    
    remaining_balance = compute_balance(bills)

    line_number = 0
    while(remaining_balance > 1):
    
        #safety valve to prevent infinite loop
        if(line_number > 100):
            break
            
        line_number += 1
        
        print_line = "{}. ".format(line_number).ljust(4)
        snowball = compute_snowball()
        
        for bill in bills:
            snowball, payment = adjust_balance(bill, snowball)
            if(payment > 0):
                print_line += "{0} ".format(payment).rjust(10)
            else:
                print_line += ("."*10)
       
        remaining_balance = compute_balance(bills)
        print_line += '{}'.format(remaining_balance).rjust(10)
        payoff.append(print_line)
    
    return payoff

bills = read_bills_file("bills.dat")
bills.sort(key=lambda tup: tup[1])
print_bills()
    
with open("results.dat", "w") as f:    
    for line in get_payoff():
        f.write(line)
        f.write("\n")
 
print("")
print("")
print("check the file results.dat for the results")    