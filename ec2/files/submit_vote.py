#!/usr/bin/python

import requests
import time
import random
from datetime import datetime

url = "http://www.medemblikactueel.nl/wp-admin/admin-ajax.php"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100102 Firefox/42.0',
    'Referer': 'http://www.medemblikactueel.nl/2015/12/13/wie-wordt-de-medemblikker-van-het-jaar-2015-verkiezingen/'
}

payload = {
    'action': 'dyamar_polls_vote',
    'dyamar_poll_id': '1',
    'dyamar_poll_answer_ids[]': '3'
}

while True:
    if (23 >= datetime.now().hour >= 7):
        r = requests.post(url, headers=headers, data=payload)
        if r.status_code == requests.codes.ok:
            print "Another vote added"
            print r.text
        else:
            print "something wrong"
            exit()

        interval = random.randint(300,1500)

        print "waiting for %d seconds" % interval
        time.sleep(interval)
    else:
        print "let's wait for an hour"
        time.sleep(3600)

print "that's it"
exit()
