#!/bin/sh

# Return a non-zero exit code if a successful connection to MySQL cannot be opened
is_mysql_running() {
    HOST=$HOST PORT=$PORT USER=$USER PASSWORD=$PASSWORD mysql -h "$HOST" --port="$PORT" -u "$USER" -p"$PASSWORD" -e '\q' >/dev/null 2>&1;
}

cmd="$@"

until is_mysql_running; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "MySQL is up - executing command"
exec $cmd