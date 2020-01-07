# Repods Project 1: IoT Data Analysis


In order to learn RePods and understand for what it can be used and how to sell it I will implement several use cases with Repods and the tools

In this project I want basically extract data from sensors, store and visualize

![Data flow chart](../images/RePods_Project1.png "Data flow chart")

### Business goal - why?
1. visualize the time series of the sensor data in a line chart
2. get some meta informations to answer the following questions
	* do the data come regular or not over time
	* is the system robust over a longer time

### Technical goal - what?
| No | Link |To Do | status |
|----|:--------------------|-------|:----:|
| 1. |[Crossbar Sensors](#1._Crossbar_Sensor) | Implement some virtual sensors that send data via crossbar | ✔ |
| 2. |[Data Stream - Import](#2._Data_Stream_-_Import) | Import the data from the crossbar message router data via iot interface into Repods | ✔ |
| 3. |[Data Transformation - Pipe](#3._Data_Transformation_-_Pipe) | Transform the initial payload from JSON format into a table conform flat database structure using the postgres syntax | ✔ |
| 4. |[Data Master - Target](#4._Data_Master_-_Target) | Generate a master tabel with a proper history of the data  | ✔ |
| 5. |[Repods - Report](#5._Repods_-_Report) | Generate a Repods report to get some statistics about the data  | ✔ |
| 6. |[Repods - Workbook](#6._Repods_-_Workbook) | Generate a repods workbook to get time series data prepared for Infograph and REST API | ✗| 
| 7. |[Repods - Infograph](#7._Repods_-_Infograph) | Generate a line chart over time with D3.js | ✗| 
| 8. |[External access - pgAdmin](#8._External_access_-_pgAdmin) | Access the databasae directly via pgAdmin and run some queries  | ✔ |
| 9. |[Visualize data - Matabase](#9._Visualize_data_-_Matabase) | Connect a BI tool (PowerBI,Tableau,Metabase) to the database and generate a line chart over time   | ✔ |
| 10. |[Rest API - Postman](#10._Rest_API_-_Postman) | connect to Rest API via Postman and test all requests | ✔ |
| 11. |[Rest API - NodeJs](#11._Rest_API_-_NodeJs) | connect to Rest API via Nodejs and output to `console.log` | ✔ | 
| 12. |[Rest API - Browser](#12._Rest_API_-_Browser) | connect to Rest API via JavaScript directly fron a browser script and show on Web dashboard | ✗ | 



## 1. Crossbar Sensor
Using the same setup as in the the [Crossbar.io project](pages/p_crossbar.md). Below the compressed view the `my_python_publisher.py` code

```python
import all_other_stuff_for_autobahn
from yahoo_fin import stock_info as si
import random

#relevat topics
topic1b  = os.environ.get('CBTOPIC', u'com.myapp.alive')
topic2b = os.environ.get('CBTOPIC', u'com.myapp.apple_price')
topic4a = os.environ.get('CBTOPIC', u'com.myapp.host')
topic5a = os.environ.get('CBTOPIC', u'com.myapp.random')

component = Component(transports=url, realm=realmv)

@component.on_join
@inlineCallbacks
def joined(session, details):
    print("Publisher running")
    counter = 0
    while True:
        # relevant topics
        session.publish(topic1b, str(counter)) # counter
        session.publish(topic2b, str(round(si.get_live_price("aapl"),4))) # message
        session.publish(topic5a, random.randint(60,120)) # random

        counter += 1
        if counter>100:
        	counter=0
        	
        yield sleep(1)


if __name__ == "__main__":
    run([component])        

```

## 2. Data Stream - Import

Following the tutorial on the [Repods website](https://repods.io/docs/#/en/tutorials/iot_import). The main trick is access the local Crossbar router via the developer tool [Ngrok](https://ngrok.com/) which allows to open up the temporarly my localhost to an public url where I can hook in with the Repods connector. Geil!!

Setup until it run took me around 1h

![Repods import for crossbar router](../images/P_Repods_iot_import.png "Repods import for Crossbar router")

## 3. Data Transformation - Pipe 
Had to learn some Postgres SQL and Json tricks to extract the data. The pipe is somehow bugy and faily due to several reasons that are not clear to me.
Typical issues:
* Target table not correct (key missing, other column names)
* Pipe not executing, getting stuck etc
* values not shown in preview

SQL of the pip is
```sql
SELECT
    payload_kwargs,
    payload_args,
	package_id as "wamp_id",                              
	received_at as EVENT_DATE,                             
	SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) as "topic",                                
	NULL::text as "message",                                                            
	NULL::numeric as "counter"  
    ,payload_args[1]::text::numeric as "random"
FROM
S_IOTDATA r1 
WHERE SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) like '%random%'
UNION ALL
SELECT
    payload_kwargs
    , payload_args
	,package_id as "wamp_id"                             
	,received_at as EVENT_DATE                             
	,SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) as "topic"                               
	,NULL::text as "message"                                                          
	,REPLACE(payload_args[1]::text,'"','')::numeric as "counter"  
    ,NULL::numeric as "random"
FROM
S_IOTDATA r1 
WHERE SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) like '%alive%'
UNION ALL
SELECT
    payload_kwargs
    , payload_args
	,package_id as "wamp_id"                             
	,received_at as EVENT_DATE                             
	,SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) as "topic"                               
	,payload_args[1]::text as "message"                                                          
	,NULL::numeric as "counter"  
    ,NULL::numeric as "random"
FROM
S_IOTDATA r1 
WHERE SPLIT_PART(payload_kwargs->'details'->>'topic','.',3) like '%host%' 
```

## 4. Data Master - Target

I set up the master table manually as the automatic creation did work non intuitive and did not update automatically 

![Repods master table](../images/P_Repods_master.png "Repods master table")

## 5. Repods - Report

## 6. Repods - Workbook

## 7. Repods - Infograph

## 8. External Access - pgAdmin 
After setting up external access to the master tables in the Analysis section I could directly query on the database.

![Configuration of external access](../images/P_Repod_ext_config.png "configuration of external access")
![Query with pgAdmin](../images/P_Repods_external_pgAdmin.png "Query with pgAdmin")


## 9. Visualize Data - Matabase
I found a very cool open source BI tool [Metabase](https://metabase.com/). It runs completely local via docker image. 
Connection to the database worked directly and the visualization took me 1 minute to configure.

![Metabase](../images/P_Repods_metabase.png "Metabase")
![Metabase](../images/P_Repods_metabase2.png "Metabase")

Downloaded the docker image and started it via 
```bash
docker run -d -p 3000:3000 --name metabase metabase/metabase
```
afterwards the UI can be accessed via browser on port 3000 `locahlhost://3000`

The chart created for the `counter` and `random` value are

![Metabase Chart example](../images/P_Repods_metabase_chart.png "Metabase chart example")

![Metabase](../images/P_Repods_metabase3.png "Metabase")
![Metabase](../images/P_Repods_metabase4.png "Metabase")

## 10. Rest API - Postman

The Rest API can be access via some REST comands and basic authentication using a key.
API url is `https://repods.io/api/username/podname/restcomand`
[API documentation](https://repods.io/docs/#/en/API_reference)
```bash 
# show reports
https://repods.io/api/alex.ortner/FreePod/reports
# show workbooks
https://repods.io/api/alex.ortner/FreePod/workbooks

# select data from report
https://repods.io/api/alex.ortner/FreePod/reports/2601
# select data from workbook
https://repods.io/api/alex.ortner/FreePod/workbook_card/2753
```


![Postman access of the Rest API](../images/P_Repods_Postman.png "Postman")


## 11. Rest API - NodeJs
Rest API request works great with a simple script and instaling the request module
```bash
npm init
npm install request
npm index.js
```
code of index.js
```javascript
var request = require('request');
var options = {
    url: 'https://repods.io/api/alex.ortner/FreePod/reports/2601',
    auth: {
        'user': '6315f662-7144-4ef9-aa38-4b0cf47fd852',
        'pass': ''
    }
};
function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
        console.log("Rest API from Statics about Random");
        console.log("Date\t\t\t\tTotal\tAverage\t\t\tMin\tMax");
        myResult=JSON.parse(body);
        myResult.forEach(function(item){
        	console.log(item.EVO_DATE + "\t" + item.tN_random + "\t" + item.tAvg_random + "\t" + item.tMn_random + "\t" + item.tMx_random);
        })
        
    }
}
request(options, callback);
````
and the output
```bash
Rest API from Statics about Random
----------------------------------
Date						Total	Average				Min		Max
2019-07-14T21:59:59+00:00	null	null				null	null
2019-07-15T21:59:59+00:00	218		90.15137614678899	60		120
2019-07-16T21:59:59+00:00	262		90.1412213740458	60		120
```


## 12. Rest API - Browser
The main issue here is that query from a browser directly runs into the CORS issue and is blocked by the browser.

Warning! Access to XMLHttpRequest at 'https://repods.io/api/alex.ortner/FreePod/reports/2601' from origin 'http://website-js.test' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: It does not have HTTP ok status.

We solved this dirty by using a proxy inbetween following the recomendations from https://github.com/Freeboard/thingproxy

Added the function to my web dashboard from project 1. 

frontend.js
```javascript
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
```

The script creates autmaically new rows on the UI table 

![Browser frontent access Rest API](../images/P_Repods_CORS_API.png "Browser")





