# Apache Spark

## Local setup on Mac Os
Setup to run Spark via Spark Submit, PySpark Console and Jupyter Notebooks

Therefore 3 parts are to install

1) Spark
2) Java 
3) Python with PySpark

My setup uses a local Spark installation, a Java SDK installation in Anaconda and Python in Anaconda. 

### Online Resources
https://towardsdatascience.com/how-to-use-pyspark-on-your-computer-9c7180075617
https://www.guru99.com/pyspark-tutorial.html

### 1) Install Anaconda

* Download the latest version from Anaconda 3 from https://www.anaconda.com/

* Install the dmg with default options

* Create a new environment with Python 3

![Anaconda Setups](../../images/s_spark_local_setup_1.png "Anaconda Setup")
![Anaconda Setup](../../images/s_spark_local_setup_2.png "Anaconda Setup")
![Anaconda Setup](../../images/s_spark_local_setup_3.png "Anaconda Setup")

* Open a terminal in this environment and install java via conda
```
conda install -c cyclus java-jdk
```
* Then install PySpark into the enviornment with conda 
```
conda install y4j -y
conda install pytz -y
conda install pyspark -y
``` 
or pip
```
python3 -m pip install pypandoc
python3 -m pip install py4j pytz
python3 -m pip install pyspark --no-cache-dir
``


### 2) Install Spark 

* Download latest version of Spark from http://spark.apache.org/downloads.html

* Unzip and move to /opt folder
```
tar -xzf spark-2.4.3-bin-hadoop2.7.tgz
mv spark-2.4.3-bin-hadoop2.7 /opt/spark-x.x.x
```
* Create a symbolic link in the /opt folder
```
ln -s /opt/spark-2.4.3-bin-hadoop2.7 /opt/spark
```

* Add the path to the `$PATH` variables 
in order that /opt/spark is automatically added on every start of a terminal call to the standart path variable from Spark it has to be added to the `~/.bashrc` file. Add the following on the end of the file
```
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```


### 3) PySpark console
Go to environment terminal and start pyspark via `pyspark`
something like this should appear
```
$pyspark 

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.3
      /_/

Using Python version 3.7.3 (default, Mar 27 2019 16:54:48)
SparkSession available as 'spark'.
>>> 
```

### 4) Scala console
Go to the enviornment terminal and start scala via `spark-shell` 
something like this should appear
```
Spark context Web UI available at http://192.168.114.15:4042
Spark context available as 'sc' (master = local[*], app id = local-1569392478864).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.3
      /_/
         
Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 12.0.2)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 

```



### 5) PySpark in Jupyter 
open a Jupyter notebook in the enviornment, load pyspark and create a spark session

```
conf = SparkConf().setAppName("SimpleExample").setMaster("local")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4])
print(rdd.sum())
print(rdd.count())
```
if `count()` and `sum()` works then all the paths where found correctly

### 6) Spark-submit command
just run 
```
spark-submit 
	--packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 
	--jars=/home/hadoop/jars/postgresql-42.2.6.jar  
	etl3_spark_ec2.py

```

### 7) Pyspark with Juypyter driver
this is needed for correct loading of some packages like the graphframe library. It works much more robust starting pyspark with Jupyter as editor instead of starting Jupyter connecting Pyspark execution to Pyspark backwards.
The trick is to set the enviornment variables for Pyspark accordingly
``` 
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS=notebook
```
and then start **PySpark** with the parameters needed
``` 
pyspark --packages graphframes:graphframes:0.6.0-spark2.3-s_2.11
``` 
### 8) Spark SQL connector to Postgres
official documentation https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html
download jar: https://jdbc.postgresql.org/download.html
hint that worked on ec2: https://www.postgresql.org/message-id/987726984.3adf84884de1a@www.netspace.net.au
here the postgres.jar file is moved directly into the java base directory like /usr/java/jdk8/jre/lib/ext

* Download latest jdbc postgres driver jar 

```
wget https://jdbc.postgresql.org/download/postgresql-42.2.6.jar
``` 
* Move to /jars folder

```
# local
mv postgresql-42.2.6.jar /opt/spark-2.4.3-bin-hadoop2.7/jars/
# emr 
mv postgresql-42.2.6.jar /home/hadoop/jars/
```

* Add as extraClassPath` into SparkSession cofig in the python code

```
from  pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession \
    .builder \
    .config('spark.driver.extraClassPath', '/opt/spark/jars/postgresql-42.2.6.jar') \
    .appName("JdbcRds") \
    .getOrCreate()
sqlContext = SQLContext(spark)
```
or add as `--jars /opt/spark/jars/postgresql-42.2.6.jar` in `spark-submit` 

```
spark-submit --jars /opt/spark/jars/postgresql-42.2.6.jar myscript.py
``` 
and then load dataframe from database

```
db_connection_string={
    "url" : 'jdbc:postgresql://conti-rds.cszfu6r3kc2w.eu-central-1.rds.amazonaws.com/traceability',
    "properties" : 
        {
            "driver": "org.postgresql.Driver",
            "user" : 'tingel',
            "password" : 'swingdeiding'
        }
    }

my_df = spark.read.jdbc(url=conn['url'], table=main_sql, properties= conn['properties'])
my_df.limit(10).show() 

```

Warning! All jars that are copied in the root directory of Spark (`/opt/spark/jars`) are automatically loaded on `spark-submit` and do not have to be added in the config or submit command anymore.

Warning! Multible jars can be added by comma seperation in the spark-submit comand `spark-submit` with different parameters what works is: `--jars /fullpath/first.jar,/fullpath/second.jar\` and `--packages /fullpath/first.jar,/fullpath/second.jar\`

### 9) Spark SQL connector to Redshift
Poor documentation on https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html

* Download latet jdbc redshift driver jar 

```
wget https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/1.2.36.1060/RedshiftJDBC42-no-awssdk-1.2.36.1060.jar -P /home/hadoop/jars
```

* Move to /jars folder

```
# local
mv RedshiftJDBC42-no-awssdk-1.2.36.1060.jar /opt/spark-2.4.3-bin-hadoop2.7/jars/
# emr 
mv RedshiftJDBC42-no-awssdk-1.2.36.1060.jar /home/hadoop/jars/
```
on AWS EMR the driver is already available in the folder

```
/usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar
```
 
* Change connection string to 

```
db_connection_string={
    "url" : 'jdbc:redshift://redshift-conti.chouvjtpouxn.eu-central-1.redshift.amazonaws.com:5439/mdl',
    "properties" : 
        {
            "driver": "com.amazon.redshift.jdbc42.Driver",
            "user" : 'tingel',
            "password" : 'SwingDeiDing34'
        }
    }

my_df = spark.read.jdbc(url=conn['url'], table=main_sql, properties= conn['properties'])
my_df.limit(10).show() 

```

`spark-submit` has to be started with the driver jar

```
# downloaded file 
spark-submit --jars path/RedshiftJDBC42-no-awssdk-1.2.36.1060.jar myscript.py

# on emr driver is already available
spark-submit --jars /usr/share/aws/redshift/jdbc/RedshiftJDBC42.jar myscript.py

``` 

## EMR Setup on AWS
a cluster can be setup via aws cli or online web UI. 

### 1. Create Cluster
This creates a cluster that constantly runs afterwards (!!! Attention can be expensive)
```
aws emr create-cluster  \
	--applications Name=Hadoop Name=Spark Name=Ganglia Name=Zeppelin \
	--release-label emr-5.26.0  \
	--name "Spark4Conti_"${USER}  \
	--log-uri s3://conti-traceability/logs/install_log.log \
	--service-role EMR_DefaultRole \
	--instance-groups '[
			{
				"InstanceCount":2,
				"InstanceGroupType":"CORE",
				"InstanceType":"r3.xlarge",
				"Name":"Core Instance Group"
			},
			{
				"InstanceCount":1,
				"InstanceGroupType":"MASTER",
				"InstanceType":"r3.xlarge",
				"Name":"Master Instance Group"
			}
		]' \
	--ec2-attributes '
			{
				"InstanceProfile":"EMR_EC2_DefaultRole",
				"SubnetId":"subnet-54e36d2e",
				"EmrManagedSlaveSecurityGroup":"sg-ba459dd1",
				"EmrManagedMasterSecurityGroup":"sg-42469e29",
				"KeyName":"alex_aws_keys"
			}'  \
	--configurations '[
			{
				"Classification":"spark",
				"Properties":{"maximizeResourceAllocation":"true"}
			},
			{
				"Classification": "spark-log4j",
				"Properties": {"log4j.rootCategory": "WARN, console"}
			}
		]' \
	--bootstrap-actions Path=s3://conti-traceability/config/emr_ec2_install.sh, Name="Install python modules"  \
	--region eu-central-1 \
	--enable-debugging 
```

### 2. Configure Cluster (Boostrap actions)
The cluster has to be prepared in terms of installation and configuration that has to be done upfront.
AWS calls this installation and cofiguration boostrap actions.
The instruction can be handed in via the parameter `--bootstrap-actions Path=path_to_install_script.sh, Name="Boostrap Acton Name"`

for the current setupt the `emr_ec2_install.sh` has the following content
```
#!/bin/bash

# Install linux packages
sudo yum update -y
sudo yum install postgresql-devel -y
sudo yum groupinstall "Development Tools" -y


# Install pythopn modules
#python3 --version
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install numpy 
sudo python3 -m pip install pandas 
sudo python3 -m pip install boto3 s3fs 
sudo python3 -m pip install psycopg2
sudo python3 -m pip install psutil

# Install postgres driver for spark
mkdir jars
mkdir pyspark
wget https://jdbc.postgresql.org/download/postgresql-42.2.6.jar -P /home/hadoop/jars

# Set environemt to python3
# https://aws.amazon.com/premiumsupport/knowledge-center/emr-pyspark-python-3x/
sudo sed -i -e '$a\export PYSPARK_PYTHON=/usr/bin/python3' /etc/spark/conf/spark-env.sh

# Download pyspark script 
grep -Fq "\"isMaster\": true" /mnt/var/lib/info/instance.json
if [ $? -eq 0 ];
then
    echo "This is a master."

	aws s3 cp s3://conti-traceability/scripts/ /home/hadoop/pyspark --recursive

    # aws s3 cp s3://de.aitdt.hbs.sensebox/data/code/mypythoncode.py .
    # spark-submit mypythoncode.py

else
    echo "This is a slave."

fi
```

### 3. Cofigure Spark 

Spark can be configured in several ways.
The fundamental way is to set all parameters in the `spark-default.conf` 
This can either be done by editing the file directly or adding Configuration Classification into the aws cli create script for the emr 
https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-configure.html

Fiels are stored at: /etc/spark/conf/

### Cluster execution - submit Spark job from shell
First login to the cluster via ssh 

```
ssh -i ~/.ssh/alex_aws_keys.pem hadoop@ec2-54-93-228-251.eu-central-1.compute.amazonaws.com
```

and then call the python code with the additional parameter for the jar of the postgres driver 
```
spark-submit --jars=/home/hadoop/jars/postgresql-42.2.6.jar  etl3_spark_ec2.py 
```

to keep a job running in the background even if the ssh connectio times out use nohub

```
# remove old logfile
rm nohup.out

# start in the background
nohup spark-submit --jars=/home/hadoop/jars/postgresql-42.2.6.jar  etl3_spark_ec2.py &

# read in logfile while running
tail -f nohup.out 
# read in logfile after completion
less nohup.out

# check on system 
htop 

```



### Step execution - submit Spark job via aws cli
in this approach a cluster is ramped up only to execute one job (pytho script) and then automatically shut down again afterwards. This helps saving money but needs time for test and debugging as all the time the full boostrap actions run again.

The aws cli emr create statement changes slightly to 

```
#!/bin/bash
aws s3 cp emr_ec2_install.sh s3://conti-traceability/config/emr_ec2_install.sh
aws s3 cp /Users/aortner/git/Conti_traceability/python/pyspark  s3://conti-traceability/scripts/ --recursive

# setup to ramp up cluster for one jop and shut down afterwards again
aws emr create-cluster  \
--applications Name=Hadoop Name=Spark \
--release-label emr-5.26.0  \
--name "Spark4Conti_Step_"${USER}  \
--log-uri s3://conti-traceability/logs/install_log.log \
--service-role EMR_DefaultRole \
--instance-groups '[{"InstanceCount":10,"InstanceGroupType":"CORE","InstanceType":"r3.xlarge","Name":"Core Instance Group"},{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"r3.xlarge","Name":"Master Instance Group"}]' \
--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-54e36d2e","EmrManagedSlaveSecurityGroup":"sg-ba459dd1","EmrManagedMasterSecurityGroup":"sg-42469e29","KeyName":"alex_aws_keys"}'  \
--configurations '[{"Classification":"spark","Properties":{"maximizeResourceAllocation":"true"}}]' \
--bootstrap-actions Path=s3://conti-traceability/config/emr_ec2_install.sh,Name="Install python modules"  \
--region eu-central-1 \
--enable-debugging \
--steps '
	[{
		"Args":
			["spark-submit",
			"--deploy-mode","cluster",
			"--jars","/home/hadoop/jars/postgresql-42.2.6.jar",
			"s3://conti-traceability/scripts/etl3_spark_ec2.py"
			],
		"Type":"CUSTOM_JAR",
		"ActionOnFailure":"TERMINATE_CLUSTER",
		"Jar":"command-runner.jar",
		"Properties":"",
		"Name":"Spark application"
	}]' \
--auto-terminate \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION 
```


### Monitor Job via Spark UI 
For this ssh port forwarding has to be activated and a some proxy settings have to be set up in the browser

#### Step 1: Configure proxy tool
1. Download and install the standard version of FoxyProxy from:
http://foxyproxy.mozdev.org/downloads.html

2. Restart Chrome after installing FoxyProxy.

3. Using a text editor create a file named foxyproxy-settings.xml containing the following:
```
<?xml version="1.0" encoding="UTF-8"?>
<foxyproxy>
    <proxies>
        <proxy name="emr-socks-proxy" id="2322596116" notes="" fromSubscription="false" enabled="true" mode="manual" selectedTabIndex="2" lastresort="false" animatedIcons="true" includeInCycle="true" color="#0055E5" proxyDNS="true" noInternalIPs="false" autoconfMode="pac" clearCacheBeforeUse="false" disableCache="false" clearCookiesBeforeUse="false" rejectCookies="false">
            <matches>
                <match enabled="true" name="*ec2*.amazonaws.com*" pattern="*ec2*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*ec2*.compute*" pattern="*ec2*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="10.*" pattern="http://10.*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*10*.amazonaws.com*" pattern="*10*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*10*.compute*" pattern="*10*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*.compute.internal*" pattern="*.compute.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                <match enabled="true" name="*.ec2.internal*" pattern="*.ec2.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            </matches>
            <manualconf host="localhost" port="8157" socksversion="5" isSocks="true" username="" password="" domain="" />
        </proxy>
    </proxies>
</foxyproxy>
```
Notes:
	* Port 8157 is the local port number used to establish the SSH tunnel with the master node. This must match the port number you used in PuTTY or terminal.
	* The *ec2*.amazonaws.com* pattern matches the public DNS name of clusters in the us-east-1 region.
	* The *ec2*.compute* pattern matches the public DNS name of clusters in all other regions.
	* The 10.*pattern provides access to the JobTracker log files in Hadoop 1.x. Alter this filter if it conflicts with your network access plan.


4. Click on the FoxyProxy icon in the toolbar and select Options.

5. Click Import/Export.

6. Click Choose File, select foxyproxy-settings.xml, and click Open.

7. In the Import FoxyProxy Settings dialog, click Add.

8. At the top of the page, for Proxy mode, choose Use proxies based on their pre-defined patterns and priorities

9. To open the web interfaces, in your browser's address bar, type master-public-dns followed by the port number or URL.

#### Step 2: Enable port forwarding
```
ssh -i ~/.ssh/alex_aws_keys.pem -ND 8157 hadoop@ec2-18-194-91-229.eu-central-1.compute.amazonaws.com
```

#### Step 3: Open Spark UIs


## Tune Spark Performance

1) Use Tree Reduce over Reduce --> reduce combining load on driver
2) Use Broadcast join --> reduce shuffle operations
3) Use performant file format like Parquet 
4) use key and enhance to salted 
5) Optimize instances and cores https://www.youtube.com/watch?v=V9E-bWarMNw

