# Python + MySQL using docker-compose


## Overview
In this unit, we'll spin up two containers using `docker-compose`. Specifically, one container will use the MySQL image from [2-mysql](../2-mysql), and the other container will be a Python app that communicates with the MySQL instance, like we did in [3-network](../3-network).

The file `docker-compose.yml` defines the two containers and their configuration.


Effectively, this setup achieves the same result as our two containers from [3-network](../3-network), but `docker-compose` elegantly handles starting and stopping both containers together. Additionally, with docker-compose, both containers are on the same network by default.


## Code

Similar to the setup from [1-python](../1-python):

- Python package requirements go in `requirements.txt`
- Project source code goes in `src/`

You'll also need to first follow the instructions from [2-mysql](../2-mysql) to build that image on your machine.

### 1. Build the two images

Because two images are listed in our `docker-compose.yml`, let's make sure those two images are built and exist on our machine.

```bash
~/4-compose > docker-compose build
mysql uses an image, skipping
Building app
Step 1/10 : FROM python:3
 ---> 7f5b6ccd03e9
Step 2/10 : LABEL maintainer "your@email.com"
 ---> dad1b3416fa1
Step 3/10 : WORKDIR /home
 ---> a6be62931ea7
Step 4/10 : COPY ./requirements.txt ./
 ---> 31f566105502
Step 5/10 : RUN pip install -r requirements.txt
 ---> a9e53307cd57
Step 6/10 : ENV PYTHONPATH=/home
 ---> 342c84623777
Step 7/10 : COPY ./src ./src
 ---> 64f745914d87
Step 8/10 : COPY ./wait-for-mysql.sh ./wait-for-mysql.sh
 ---> 51f5833a1c98
Step 9/10 : RUN chmod +x ./wait-for-mysql.sh
 ---> 6c374a2d84d1
Step 10/10 : RUN apt-get update   && apt-get install -y default-mysql-server
 ---> aecad1945bd2
Successfully built aecad1945bd2
Successfully tagged 4-compose_app:latest
```

### 2. Bring up the containers

We're ready to spin up the containers. When we do, Docker will first start up the MySQL database container, then the Python app container. The Python app will wait for MySQL to begin accepting connections, and then it will query for a list of databases and print it to stdout.

```bash
~ > docker-compose up
```

You should see output from both containers in your console now. Most of the initial output will be MySQL logs, indicating where it's at in its startup sequence. You'll also occasionally see a message from the Python app, indicating that it's trying to connect to MySQL, but can't just yet.

Finally, you'll see the Python app successfully connect to the MySQL instance and print the list of databases:
```bash
...
mysql_1  | 2020-07-03T22:41:52.872132Z 0 [Note] mysqld: ready for connections.
mysql_1  | Version: '5.7.30'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
app_1    | MySQL is up - executing command
app_1    | INFO:root:Connecting to DB with config: {'user': 'root', 'password': 'password', 'host': 'mysql', 'port': '3306', 'database': 'demo'}
app_1    | INFO:root:[('information_schema',), ('demo',), ('mysql',), ('performance_schema',), ('sys',)]
4-compose_app_1 exited with code 0
```

#### Running in detached mode

There was a lot of output here, and we were really only interested in the app's logs rather than MySQL's. To remedy that, we can have Docker run both containers in detached mode, so output won't be printed to the shell.

```bash
~ > docker-compose up -d
```

To see the logs for the Python app, we can run `docker-compose logs` and specify that we only want to see logs for the container called "app", as we named it in `docker-compose.yml`.


```bash
~ > docker-compose logs -f app  # The -f flag tails the log - it will continuously print new output
```

### 3. Clean up

In the same shell (if you ran in detached mode) or from a new shell, in the `4-compose` directory, run:

```bash
~ > docker-compose down
```

This will stop and remove all containers that `docker-compose up` started. It will also delete the logs associated with those containers.
