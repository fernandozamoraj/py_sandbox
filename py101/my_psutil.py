# Functions to get system values:
from psutil import cpu_percent, net_io_counters
# Functions to take a break:
from time import sleep
# Package for email services:
import smtplib
import string

def pollForAttacks():

    MAX_NET_USAGE = 400000
    MAX_ATTACKS = 4
    attack = 0
    counter = 0

    while attack <= MAX_ATTACKS:
        sleep(4)
        counter = counter + 1
        # Check the cpu usage
        if cpu_percent(interval = 1) > 70:
            attack = attack + 1
        # Check the net usage
        neti1 = net_io_counters()[1]
        neto1 = net_io_counters()[0]
        sleep(1)
        neti2 = net_io_counters()[1]
        neto2 = net_io_counters()[0]
        # Calculate the bytes per second
        net = ((neti2+neto2) - (neti1+neto1))/2
        print 'neti1 = {0}'.format(neti1)
        print 'neto1 = {0}'.format(neto1)
        print 'neti2 = {0}'.format(neti2)
        print 'neto2 = {0}'.format(neto2)
        
        print 'net = {0}'.format(net)
        if net > MAX_NET_USAGE:
            attack = attack + 1
        if counter > 25:
            attack = 0
            counter = 0

            # Write a very important email if attack is higher than 4
TO = "fernando.zamora.jimenez@gmail.com"
FROM = "fernando.zamora.jimenez@something.com"
SUBJECT = "Your domain is out of system resources!"
text = "Go and fix your server!"
BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
server = smtplib.SMTP('127.0.0.1')
server.sendmail(FROM, [TO], BODY)
server.quit()