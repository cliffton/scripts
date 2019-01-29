import requests
from tiger.reqs import *
from threading import Thread
import sys
import urllib



def send_it(url):
    rep = requests.get(url, data=data, headers=headers, cookies=cookies)
    if rep.status_code == 200:
        print(rep.status_code)
        # sys.stdout.write(str(rep.status_code))
        

try:
    site = "https://tigercenter.rit.edu/tigerCenterEnrollment/api/checkout?"
    map_str = urllib.parse.urlencode(data)
    url = site + "map=" + map_str

    url = "https://tigercenter.rit.edu/tigerCenterEnrollment/api/checkout?map=%7B%22term%22:%222175%22,%22career%22:%22GRAD%22,%22ppids%22:%5B%22110801-1-2175-1-01-53852%22,%22103702-1-2175-1-01-54074%22,%22112972-1-2175-1-01-54167%22%5D,%22related1s%22:%5B%220%22,%220%22,%220%22%5D,%22related2s%22:%5B%220%22,%220%22,%220%22%5D,%22grading%22:%5B%22GRD%22,%22GRD%22,%22GRD%22%5D,%22waitList%22:%5Btrue,true,true%5D%7D"
    send_it(url)
    for x in range(10):
        t = Thread(target=send_it)
        # t.daemon = True
        t.start()
except Exception as e:
    print(e)

