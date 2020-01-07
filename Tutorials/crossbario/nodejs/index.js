var autobahn = require('autobahn');
var http = require('http');

console.log("Running AutobahnJS " + autobahn.version);


const url = 'ws://104.199.76.81:8081/ws';
const realm = 'realm1';


var connection = new autobahn.Connection({url: url, realm: realm});

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Hello World from Test Script!');
}).listen(5555);

// .. and fire this code when we got a session
connection.onopen = function (session, details) {
   //console.log("session open!", details);
   console.log("session open!");

   
   // subscribe to the topics
   function onevent(args) {
      console.log("TouchEvent:", args[0]);
   }
   session.subscribe('com.iot.clapdata', onevent);
   session.subscribe('com.myapp.touch_event', onevent);
   session.subscribe('com.myapp.host', onevent);
   session.subscribe('com.myapp.alive', onevent);

   // publish a test message
   session.publish('com.myapp.host', ['Message from Nodejs  ']);

   //connection.close();
};

// .. and fire this code when our session has gone
connection.onclose = function (reason, details) {
   console.log("session closed: " + reason, details);
}

// Don't forget to actually trigger the opening of the connection!
connection.open();
