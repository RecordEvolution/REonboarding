try {
   var autobahn = require('autobahn');
} catch (e) {
   // when running in browser, AutobahnJS will
   // be included without a module system
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'realm1'}
);

connection.onopen = function (session) {

   var counter = 0;

   setInterval(function () {
      console.log("publishing to topic 'com.myapp.host': " + "Hello World "+counter);
      session.publish('com.myapp.host', ['Message ' + counter]);
      document.getElementById('WAMPEvent').innerHTML =  "Event: Message "+counter;
      counter += 1;
   }, 1000);
};

connection.open();