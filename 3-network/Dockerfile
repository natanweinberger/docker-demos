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