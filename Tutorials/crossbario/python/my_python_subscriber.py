###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Crossbar.io Technologies GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
import os

#url = os.environ.get('CBURL', u'ws://localhost:8080/ws')
url = os.environ.get('CBURL', u'ws://104.199.76.81:8081/ws')

realmvalue = os.environ.get('CBREALM', u'realm1')
topic1  = os.environ.get('CBTOPIC', u'com.myapp.hello')
topic2  = os.environ.get('CBTOPIC', u'com.myapp.apple')
topic3  = os.environ.get('CBTOPIC', u'com.myapp.amazon')
topic4  = os.environ.get('CBTOPIC', u'com.myapp.host')
topic5  = os.environ.get('CBTOPIC', u'com.myapp.random')
topic6  = os.environ.get('CBTOPIC', u'com.immoscraper.json')
topic7  = os.environ.get('CBTOPIC', u'com.immoscraper.alive')




component = Component(transports=url, realm=realmvalue)


@component.on_join
@inlineCallbacks
def joined(session, details):
    print("session ready")

    def oncounter(count):
        print("event received: ", count)

    try:
        yield session.subscribe(oncounter, topic1)
        print("subscribed to topic: " + topic1)
        yield session.subscribe(oncounter, topic2)
        print("subscribed to topic: " + topic2)
        yield session.subscribe(oncounter, topic3)
        print("subscribed to topic: " + topic3)
        yield session.subscribe(oncounter, topic4)
        print("subscribed to topic: " + topic4)
        yield session.subscribe(oncounter, topic5)
        print("subscribed to topic: " + topic5)
        yield session.subscribe(oncounter, topic6)
        print("subscribed to topic: " + topic6)
        yield session.subscribe(oncounter, topic7)
        print("subscribed to topic: " + topic7)
    except Exception as e:
        print("could not subscribe to topic: {0}".format(e))


if __name__ == "__main__":
    run([component])        



