# Python + MySQL

This Dockerfile illustrates how to run Python and MySQL in separate containers, allowing them to communicate with each other.

By default, containers are isolated from each other by running on different virtual networks. In this example, we'll create a common network using Docker that both containers are attached to.

Similar to the setup from [1-python](../1-python):

- Python package requirements go in `requirements.txt`
- Project source code goes in `src/`

You'll also need to first follow the instructions from [2-mysql](../2-mysql) to build that image on your machine.

### 1. Build the image containing the Python project

```bash
~ > docker build -t 3-network -f Dockerfile .
Sending build context to Docker daemon  8.192kB
Step 1/7 : FROM python:3
 ---> 7f5b6ccd03e9
Step 2/7 : LABEL maintainer "your@email.com"
 ---> dad1b3416fa1
Step 3/7 : WORKDIR /home
 ---> a6be62931ea7
Step 4/7 : COPY ./requirements.txt ./
 ---> 3fc4dff63685
Step 5/7 : RUN pip install -r requirements.txt
 ---> Running in daa7bf8c63a8
Collecting mysql-connector-python==8.0.20
  Downloading mysql_connector_python-8.0.20-cp38-cp38-manylinux1_x86_64.whl (14.8 MB)
Collecting protobuf>=3.0.0
  Downloading protobuf-3.12.2-cp38-cp38-manylinux1_x86_64.whl (1.3 MB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.8/site-packages (from protobuf>=3.0.0->mysql-connector-python==8.0.20->-r requirements.txt (line 1)) (47.1.1)
Collecting six>=1.9
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: six, protobuf, mysql-connector-python
Successfully installed mysql-connector-python-8.0.20 protobuf-3.12.2 six-1.15.0
Removing intermediate container daa7bf8c63a8
 ---> 1c4bbf414690
Step 6/7 : ENV PYTHONPATH=/home
 ---> Running in 9da455b22e6e
Removing intermediate container 9da455b22e6e
 ---> 0ecef5fde48b
Step 7/7 : COPY ./src ./src
 ---> 73e57fac18f9
Successfully built 73e57fac18f9
Successfully tagged 3-network:latest
```

### 2. Create a network

This sets up a virtual network that both the MySQL and Python containers will operate on. Instead of being on isolated networks now, they'll be able to communicate with each other. Note that because they're on the same network, they share the same ports.

```bash
~ > docker network create demo-network
```

### 3. Run a MySQL container

We'll start a container based on the [2-mysql](../2-mysql) image, but this time we'll also attach it to the network `demo-network` using the `--net` flag.

The flags:

- `--rm` removes the container when you stop it
- `-d` runs the container detached, or in the background (try it without this flag and see the MySQL logging output!)
- `-p 3307:3306` maps the container's port 3306 to your computer's port 3307 (useful if you want to try connecting from outside a container)
- `--net` attaches this container to the Docker network `demo-network`
- `--name` assigns the container a name instead of letting Docker choose a random name

```bash
~ > docker run --rm -d -p 3307:3306 --net demo-network --name demo-db 2-mysql
```

### 4. Run a container using the 3-network image

We'll start a container based on the image we just built, then connect to the other container's MySQL instance using a Python script.

The Python script at `src/db.py` will make the connection and output the results of the query `SHOW DATABASES;`. It requires the connection credentials to be defined as environment variables.

Here's where the environment variables in the command come from:
- `USER=root`: All MySQL instances are created with a default user called "root"
- `PASSWORD=password`: We defined this in the [2-mysql Dockerfile](../2-mysql/Dockerfile)
- `DATABASE=demo`: This database was created in the [2-mysql setup.sql](../2-mysql/setup.sql)
- `HOST=demo-db`: Docker containers are addressable both by their container name and by an internal IP assigned by Docker
- `PORT=3306`: MySQL is running on port 3306

Note that the mapping to port 3307 on our host machine still exists, but it's only useful to us when we try to connect to MySQL from outside of Docker. Because we're in a container that's on the same network as our MySQL container (and thus shares the same ports), it sees MySQL running directly on port 3306.

```bash
~ > docker run --rm -it --net demo-network 3-network bash
root@46e265030834:/home# USER=root PASSWORD=password DATABASE=demo PORT=3306 HOST=demo-db python src/db.py
INFO:root:Connecting to DB with config: {'user': 'root', 'password': 'password', 'host': 'demo-db', 'port': '3306', 'database': 'demo'}
INFO:root:[('information_schema',), ('demo',), ('mysql',), ('performance_schema',), ('sys',)]
root@46e265030834:/home# exit
~ >
```

### 5. Clean up
```bash
~ > docker stop demo-db
~ > docker network rm demo-network
```
