try {
   var autobahn = require('autobahn');
   const axios = require('axios');

} catch (e) {
   // when running in browser, AutobahnJS will
   // be included without a module system
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'realm1'}
);



var session1;
var myLabels =[0];
var myDatapoints=[203.80];

connection.onopen = function (session) {

   
   function price1(args) {
      console.log("Price 1:", args[0]);
      document.getElementById('box1').innerHTML = "$"+ args[0];
      myDatapoints.push(args[0]);
      //console.log(myDatapoints);
   }
   function price2(args) {
      console.log("Price 2:", args[0]);
      document.getElementById('box2').innerHTML = "$"+ args[0];
      myChartOptions.data.labels=myLabels;
      myChartOptions.data.datasets[0].data=myDatapoints;
      var myLineChart = new Chart(ctx,myChartOptions);
      console.log(myLabels);
      console.log(myDatapoints);
   }
   function alive(args) {
      console.log("Got Alive Message:", args[0]);
      document.getElementById('box3').innerHTML = args[0] + "s";
      document.getElementById('box4').style.width = args[0] +"%";
      myLabels.push(args[0]);
      
      //console.log(myLabels);
   }
   function usermessage(args) {
      console.log("Host Topic: " + args[0]);
      document.getElementById('box5').innerHTML = args[0];
   }

   session1=session;

   session.subscribe('com.myapp.apple_price', price1);
   session.subscribe('com.myapp.amazon_price', price2);
   session.subscribe('com.myapp.alive', alive);
   session.subscribe('com.myapp.host', usermessage);

   //

};


function sendMessage(session)
{  
   myMessage=document.getElementById("messageValue").value;
   session1.publish('com.myapp.host', [myMessage]);
   console.log("Published: " + myMessage);
   document.getElementById('box5').innerHTML = myMessage;
}


function getRestAPIData() {

   console.log("Start REST API call");

   var url = 'https://cors-anywhere.herokuapp.com/https://repods.io/api/alex.ortner/FreePod/reports/2601';

   var username = '6315f662-7144-4ef9-aa38-4b0cf47fd852';
   var password = '';
   var base64Credentials = btoa(username + ':' + password);

   var xhr = new XMLHttpRequest();
   xhr.open('GET', url, true);
   // xhr.setRequestHeader(‘Authorization’, ‘Basic 5c0339b0-031c-46f8-b284-1ed7e’);
   xhr.setRequestHeader('Authorization', 'Basic ' + base64Credentials);
   xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
   xhr.onload = function() {
       //alert(xhr.status + ' ' + xhr.statusText + '\n\n' + xhr.responseText);
       //result=xhr.responseText.replace('[','').replace(']','');
      result_JSON=JSON.parse(xhr.responseText);
      //console.log(result_JSON[result_JSON.length-1].tAvg_random);

      result_JSON.forEach(function(entry) {
         console.log("Create Row for: " + entry.tAvg_random);
         var table = document.getElementById("RepodsTable");
         var row = table.insertRow(-1);
         var cell1 = row.insertCell(0);
         var cell2 = row.insertCell(1);
         var cell3 = row.insertCell(2);
         var cell4 = row.insertCell(3);
         var cell5 = row.insertCell(4);

         cell1.innerHTML = entry.EVO_DATE.substring(0,10);
         cell2.innerHTML = Math.round(entry.tN_random);
         cell3.innerHTML = Math.round(entry.tAvg_random*1000)/1000;
         cell4.innerHTML = Math.round(entry.tMn_random);
         cell5.innerHTML = Math.round(entry.tMx_random);
      });

      


   };
   xhr.send();

    
    
}


getRestAPIData();
connection.open();







//console.log(myChartOptions.data.datasets[0].data);



