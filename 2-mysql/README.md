# MySQL database

This Dockerfile creates an image for running a MySQL 5.7 instance.

- There is a place for you to set your desired password for the MySQL root user in the Dockerfile
- You can include SQL commands to be executed on the container's first run in `setup.sql`
- Inside the container, MySQL runs on port 3306, but you can map the container's port 3306 to any port on your computer

When the image is built, Docker will build from the mysql:5.7 image and will run any files in `setup.sql` to initialize the database.

### 1. Build the image

```bash
~ > docker build -t 2-mysql -f Dockerfile .
Sending build context to Docker daemon  3.584kB
Step 1/4 : FROM mysql:5.7
 ---> 9cfcce23593a
Step 2/4 : LABEL maintainer "your@email.com"
 ---> c8f93427e219
Step 3/4 : ENV MYSQL_ROOT_PASSWORD=password
 ---> Running in 16a3305f2b33
Removing intermediate container 16a3305f2b33
 ---> 2d9c124d5feb
Step 4/4 : COPY ./setup.sql /docker-entrypoint-initdb.d/
 ---> 76cd8a42e401
Successfully built 76cd8a42e401
Successfully tagged 2-mysql:latest
```

### 2. Run a container

The flags:

- `--rm` removes the container when you stop it
- `-d` runs the container detached, or in the background (try it without this flag and see the MySQL logging output!)
- `-p 3307:3306` maps the container's port 3306 to your computer's port 3307

```bash
# Let's map the container's port 3306 to local port 3307
~ > docker run --rm -d -p 3307:3306 2-mysql
aabe0cddc9fde1e404072eb2f8300b5c270b6e3cf927d07f1a779ef2b08c52da
~ > mysql --port=3307 --protocol=tcp -u root -ppassword
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| demo               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

```

### 3. Exit the container
```bash
~ > docker stop aabe0cd
# The container is automatically removed because we used --rm in the last step
```