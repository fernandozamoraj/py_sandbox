
from subprocess import call

LINE_TYPE_INDEX = 0
ACCOUNT_INDEX = 1
BALANCE_INDEX = 2
APR_INDEX = 3
PAYMENT_INDEX = 4
EXTRA_AMOUNT_INDEX = 1
EXTRA_MONTH_NO_INDEX = 2 

def add_logging(message):
    def loggin_decorator(func):
        def wrapper(*args, **kargs):
            #print(x)
            return func(*args, **kargs)
	
        return wrapper
    return loggin_decorator

@add_logging("executing read_bills_file")
def read_bills_file(filename):
    bills = []
    extra_funds = dict()
    
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
            print(line)
            line_type = line[LINE_TYPE_INDEX]
            if(line_type == "bill"):
                bill = []
                bill.append(line_type)
                set_account_name(line[ACCOUNT_INDEX], bill)
                convert_fields_to_numbers(line[BALANCE_INDEX:], bill)
                bills.append(bill)
            if(line_type == "extra"):
                extra_funds[int(line[EXTRA_MONTH_NO_INDEX])] = int(line[EXTRA_AMOUNT_INDEX])            
        
    return bills, extra_funds

@add_logging("executing set_account_name")
def set_account_name(account_name, target_list):
    target_list.append(account_name)

#convert the fields to integers 
#the first field is the account name so that's a string.
#Hence why the first field is ignored
@add_logging("executing convert_fields_to_numbers")
def convert_fields_to_numbers(source_list, target_list):
    for field in source_list:
        target_list.append(float(field))

@add_logging("executing print_bill")
def print_bill(bill):
    print(" {:12} ${:5d} {:5.1f}% ${:5d}/month".format(bill[ACCOUNT_INDEX], int(bill[BALANCE_INDEX]), float(bill[APR_INDEX]), int(bill[PAYMENT_INDEX])))
    
@add_logging("executing print_bills")    
def print_bills():
    print("");
    print("********Bills**********")
    print("")
    
    for bill in bills:
        print_bill(bill)
        
@add_logging("executing compute_snowball")        
def compute_snowball():
    snowball = 0
    
    for bill in bills:
        if(bill[BALANCE_INDEX] < 1):
            snowball += bill[PAYMENT_INDEX]
  
    return snowball
        
@add_logging("compute_balance")        
def compute_balance(bills):
    balance = 0
    for bill in bills:
        balance += bill[BALANCE_INDEX]
        
    return balance

@add_logging("executing adjust_balance")
def adjust_balance(bill, snowball):
    
    payment = 0
    if(bill[BALANCE_INDEX] < 1):
        return snowball, payment
        
    balance = bill[BALANCE_INDEX]    
    interest_rate = (bill[APR_INDEX]/100.0)/12.0
    interest_charges = balance*interest_rate;
    bill[BALANCE_INDEX] += interest_charges
  
    monthly_payment = bill[PAYMENT_INDEX]
        
    snowball, payment = \
          calculate_payment_and_snowball(balance, monthly_payment, snowball)
    
    bill[BALANCE_INDEX] = int(bill[BALANCE_INDEX] - payment) #deduct payment
   
    return snowball, payment

@add_logging("executing calculate_payment_and_snowball")
def calculate_payment_and_snowball(balance, monthly_payment, snowball):
    
    payment = 0
    
    if(balance >= monthly_payment):
        payment += monthly_payment
    else:
        payment += balance
        snowball += (monthly_payment - payment)
    
    if(snowball > 0 and balance >= snowball):
        payment += snowball
        snowball = 0
    elif(snowball > 0 and balance > 0):
        payment += balance
        snowball = snowball - balance 

    return int(snowball), int(payment)

@add_logging("executing create_header")
def create_header(payoff, bills):
    header_line = "".ljust(4)
    
    for bill in bills:
        header_line += '{}'.format(bill[ACCOUNT_INDEX][:11]).center(10)
    
    header_line += "Balance".center(10)    
    header_line += "\n"
    header_line += ("-"*((len(bills)+1)*10))     
    payoff.append("")
    payoff.append(header_line)


@add_logging("executing get_payoff")
def get_payoff():

    payoff = []
    create_header(payoff, bills)
    
    remaining_balance = compute_balance(bills)

    line_number = 0

    MAX_LOOPS = 100    
    while(remaining_balance > 1 and line_number < MAX_LOOPS):
        line_number += 1
        
        print_line = "{}. ".format(line_number).ljust(4)
        snowball = compute_snowball()
        
        if(line_number in extra_funds):
            snowball += extra_funds[line_number]
        
        for bill in bills:
            snowball, payment = adjust_balance(bill, snowball)
            if(payment > 0):
                print_line += "{:5,.0f} ".format(payment).rjust(10)
            else:
                print_line += ("."*10)
       
        remaining_balance = compute_balance(bills)
        print_line += "{:7,.0f}".format(remaining_balance).rjust(10)
        payoff.append("\n"+print_line)
    
    return payoff

@add_logging("executing run")
def run(bills_file, outfile):
    global bills
    global extra_funds
    
    bills, extra_funds = read_bills_file(bills_file)

    bills.sort(key=lambda record: record[BALANCE_INDEX])
    print_bills()
        
    with open(outfile, "w") as f:    
        f.writelines(get_payoff())
 
    call(["notepad.exe", outfile], shell=False)   
    
#change these files(file paths) to meet your needs
#bills_file should have the following format:
#bill,account-name,balance,apr,monthly-payment
#extra,amouunt,month-number
#bill,auto,15020,3.29,320
#bill,mastercard,2500,9.45,471
#bill,capital_one,4100,0,200
#extra,350,1
#extra,350,2
#extra,1700,3
#
#Everything marked "bill" indicates a debt.
#Everything marked "extra" is an extra payment for that row indicated 
#by the last field.
bills_file = "c:/temp/bills.dat"
outfile = "c:/temp/snowball_results.dat"   
    
if(__name__ == "__main__"):
    run(bills_file, outfile)    