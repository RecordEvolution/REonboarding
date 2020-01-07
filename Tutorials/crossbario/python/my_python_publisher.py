from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
import os
import argparse
import six
import time
from datetime import datetime

# installation needed when docker image is not prepared
#installCMD = 'pip3 install yahoo_fin'
#os.system(installCMD)

#installCMD = 'pip3 install requests'
#os.system(installCMD)

#installCMD = 'pip3 install pandas'
#os.system(installCMD)

from yahoo_fin import stock_info as si
import random


#url = os.environ.get('CBURL', u'ws://localhost:8080/ws')
url = os.environ.get('CBURL', u'ws://104.199.76.81:8081/ws')


realmv = os.environ.get('CBREALM', u'realm1')
topic1a = os.environ.get('CBTOPIC', u'com.myapp.hello')
topic1b  = os.environ.get('CBTOPIC', u'com.myapp.alive')
topic2a = os.environ.get('CBTOPIC', u'com.myapp.apple')
topic3a = os.environ.get('CBTOPIC', u'com.myapp.amazon')
topic2b = os.environ.get('CBTOPIC', u'com.myapp.apple_price')
topic3b = os.environ.get('CBTOPIC', u'com.myapp.amazon_price')
topic4a = os.environ.get('CBTOPIC', u'com.myapp.host')
topic5a = os.environ.get('CBTOPIC', u'com.myapp.random')


print(str(datetime.now()) + " URL connecting: " + url)
print(str(datetime.now()) + " Realm used: " + realmv)

component = Component(transports=url, realm=realmv)


@component.on_join
@inlineCallbacks
def joined(session, details):
    print("Publisher running")
    counter = 0
    while True:
        # publish() only returns a Deferred if we asked for an acknowledgement
        session.publish(topic1a, "Alive Counter: %d"%counter)
        session.publish(topic1b, str(counter))
        session.publish(topic2a, "Latest Stock Price from Apple: " + str(si.get_live_price("aapl")))
        session.publish(topic2b, str(round(si.get_live_price("aapl"),4)))
        session.publish(topic3a, "Latest Stock Price from Amazon: " + str(si.get_live_price("amzn")))
        session.publish(topic3b, str(round(si.get_live_price("amzn"),4)))
        session.publish(topic5a, random.randint(60,120))
        #session.publish(topic4a, str(os.system("hostname")))
        #session.publish(topic4b, str(os.system("hostname -i")))
        counter += 1
        if counter>100:
        	counter=0
        	
        yield sleep(1)


if __name__ == "__main__":
    run([component])        