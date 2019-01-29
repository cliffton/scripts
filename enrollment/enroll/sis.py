import requests
from r import *
from threading import Thread
import sys
import urllib
# import urllib2
import urllib.request

url = "https://campus.rit.edu/psc/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL"

def send_it():
    rep = requests.post(url, data=data, headers=headers, cookies=cookies)
    if rep.status_code == 200:
        print(rep.status_code)
        # sys.stdout.write(str(rep.status_code))
        
def send_it1():
    d = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, d, headers=headers)
    response = urllib.request.urlopen(req)
    print(response.code)

try:
    url = "https://campus.rit.edu/psc/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL"
    send_it1()
    for x in range(10000):
        t = Thread(target=send_it1)
        # t.daemon = True
        t.start()
except Exception as e:
    print(e)

