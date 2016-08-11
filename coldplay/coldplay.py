import requests
from secs import *
import smtplib


def send_sms():
    print "Sending SMS"
    try:
        for num in numbers:
            print "Sending %s" % num
            sms_url = GUPSHUP_SMS_URL.format(mobile_no=num)
            requests.get(sms_url)
    except Exception, e:
        print e
        pass


def send_email():
    try:
        fromaddr = cliff
        toaddrs = cliff
        msg = "Check Now !!"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(cliff, pwd)

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        print "Sending send_email"
    except Exception, e:
        print e
        pass


resp = requests.get('http://coldplay.com/tour/')
print "got resp"
value = resp.content.find('Australia')

if value > 0:
    send_email()
    send_sms()
