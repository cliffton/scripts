import requests
from secs import *
import smtplib


def send_sms():
    print "Sending SMS"
    try:
        requests.get(GUPSHUP_SMS_URL)
    except Exception, e:
        print e
        pass


def send_email(date_str):
    try:
        fromaddr = cliff
        toaddrs = kev
        msg = 'Appointment Available for %s' % date_str
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(cliff, pwd)

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        print "Sending send_email"
    except Exception, e:
        print e
        pass


cookies = {
    "BrowserId": "i_rspoYiQ-KUfFYKZ6z1Sw",
    "__utma": "1.363385147.1462907492.1462907492.1462996462.2",
    "__utmb": "1.9.10.1462996462",
    "__utmc": "1",
    "__utmt": "1",
    "__utmz": "1.1462907492.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=https%3A%2F%2Fcgifederal.secure.force.com%2F",
    "apex__aa-time": "KeNHnxhHDNBY1uLE_2F6f4wg_3D_3D",
    "autocomplete": "1",
    "clientSrc": "27.4.199.208",
    "inst": "APP_1A",
    "lloopch_loid": "00DC0000000PhuP",
    "lloopch_lpid": "060C0000000QwL9",
    "oid": "00DC0000000PhuP",
    "oinfo": "c3RhdHVzPUFDVElWRSZ0eXBlPTYmb2lkPTAwREMwMDAwMDAwUGh1UA==",
    "sid": "00DC0000000PhuP!ARwAQHqzr0IS3Cfzi9qTGLJGlxZLJ29oBkXSX.dfT88BV4bzQlOUS7GY91t4WNVXl_28jApcNWeK8OuZu8QyPTnjG3Ob7vez",
    "sid_Client": "A00000BHCSe0000000PhuP"
}

resp = requests.get(
    'https://cgifederal.secure.force.com/applicanthome', cookies=cookies)

index = resp.content.find('First Available Appointment Is ')
date_str = resp.content[index:index + 53]
print date_str
value = date_str.find('May')
if value > 0:
    send_email(date_str)
    send_sms()
