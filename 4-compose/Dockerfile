FROM python:3
LABEL maintainer "your@email.com"

# Set working directory
WORKDIR /home

# Copy requirements
COPY ./requirements.txt ./

# Install requirements
RUN pip install -r requirements.txt

# Add PYTHONPATH
ENV PYTHONPATH=/home

# Copy source code
COPY ./src ./src
COPY ./wait-for-mysql.sh ./wait-for-mysql.sh
RUN chmod +x ./wait-for-mysql.sh

# Install MySQL for wait-for-mysql.sh
RUN apt-get update \
 && apt-get install -y default-mysql-server