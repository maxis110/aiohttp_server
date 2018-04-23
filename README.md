## Sendify Server

### Description:
This server based on aiohttp framework which automatically deployed to 3 docker container(DB, DB Viewer, Server API).
Server provide is one route `/proposals` which give shipments proposals from all carriers  based on input data in headers.  

### Requirements:

1. Install `Python 3.6`, if not yet installed (https://www.python.org/downloads/).
2. Have latest possible `pip` installed.
3. Have latest possible `virtualenv` installed (`pip3 install virtualenv`).
4. Have latest possible `make` installed.
5. Have latest possible `docker` and `docker-compose` installed.

### How to check that required tools installed

#### Python

You may check that Python 3.6 installed by running 

```python --version```

You should see something like:

```
Python 3.6.1
```

Run:

```python3 --version```

You should get something like:

```
Python 3.6.4
```

#### pip

Run:
```pip3 --version```

And you will see something like:
```pip 9.0.1 from /usr/lib/python3.6/site-packages (python 3.6)```

#### Docker
Please run:

```docker --version```

You should see something like:

```Docker version 17.09.1-ce, build 19e2cf6```


#### Docker-compose

Please run:
```docker-compose --version```

You should see something like:

```docker-compose version 1.17.1, build 6d101fb0```


#### Make
Please run:
```make --version```

You should see something like:

```
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-pc-mingw32
```

### Environment:

#### Components

Application contains such docker containers:

* PostgresDB
* Adminer(viewer for postgres db)
* Sendify Server API

#### Initialization

In case when you have installed modern version of docker (plus docker-compose) and make, all that should be done is:

```
make build_environment
```

This command will start containers on ports:

* 5432 - PostgresDB
* 8080 - Adminer
* 5858 - Sendify Server API

If containers up successfully then you will be able to execute request:

```
http://0.0.0.0:5858/
```
and ger response:
```
Welcome to Sendify test server
```


Then you should execute GET request with headers like below.Application automatically create DB and fill it with default data.

```
http://0.0.0.0:5858/proposals
```

Mandatory headers:
```
origin_city = (Stockholm or Kiev or Krakow)
destination_city = (Stockholm or Kiev or Krakow)
product_type = (letter or package or pallet)
```

Additional headers(each of package type already have default values of this parameters but you can specify it):
```
weight
height
leight
width
```

DB structures and default data you can find by the rout :

```
http://0.0.0.0:8080/
```

Credentials:

```
System = PostgrSQL
Server = dbPostgres
Username = user_sendify
Password = password
Database = sendify_db
```

### Example request and response: 

Request:
```
http://0.0.0.0:5858/proposals
origin_city = Stockholm
destination_city = Kiev
product_type = letter
```

Response:

```
[
    {
        "_carrier_name": "DHL Express",
        "_product_type": "letter",
        "_price": 48000,
        "_expected_transit_time": "20 hours"
    },
    {
        "_carrier_name": "FedEx Corporation",
        "_product_type": "letter",
        "_price": 24000,
        "_expected_transit_time": "30 hours"
    },
    {
        "_carrier_name": "Royal Mail",
        "_product_type": "letter",
        "_price": 12000,
        "_expected_transit_time": "40 hours"
    }
]
```
