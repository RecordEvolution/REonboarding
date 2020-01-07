# PostgreSQL

## Postgres via Docker

Create a postgreSQL container and forward port 

```
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=tingel postgres
```

Show all the details about the containe to find the volumes
```
docker inspect -f '{{ json .Mounts }}' c65137975039 | python -m json.tool 
```

### Postgres Shell 
```
# first open the bash form the sever
docker exec -it my-postgres bash

# then enter the psql shell
psql -U postgress

# then fire psql commands

# 1. list all databases
=# \l

# 2. connect to a database
=# \c dvdrental

# 3. check out this databse
=# \d

# 4. Quit the postgres shell
=# \q

```

### Connection Details

Connect via localhost from pgAdmin or Python to the database `locahlhost:5432`

## Connect via PG Admin

## Connect via Python 

Import the database adapter and Pandas
```
# Postgres database adapter 
import psycopg2 as pgsgl
# Pandas framework
import pandas as pd
```
Read SQL statement into Pandas dataframe
```
hostname = 'jumper1.repods.io'
username = 'tingel'
password = 'tingel'
database = 'reone'
port = '49161'

try:
    conn = pgsgl.connect( host=hostname, user=username, password=password, dbname=database, port=port )
    print("Yes!! connect to the database")
except:
    print("ERROR: I am unable to connect to the database")

try: 
    sqlquery='Select * from schema_abm.t_immoscout_2'
    df = pd.read_sql(sqlquery,con=conn)
    print("Hurra!! Data loaded into Dataframe")
except:
    print("ERROR: Data load failed")

conn.close()
```
Check the data and get some insights
```
df.head()
df.describe()
df.columns
```



## Connect via Metabase

## SQL JSON syntax


