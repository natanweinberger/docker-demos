FROM mysql:5.7
LABEL maintainer "your@email.com"

# Set the root password
ENV MYSQL_ROOT_PASSWORD=password

# SQL files in this directory are run when the container is started for the first time
COPY ./setup.sql /docker-entrypoint-initdb.d/
