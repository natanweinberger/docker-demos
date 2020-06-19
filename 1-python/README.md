# Python project with dependencies

This Dockerfile creates a lightweight image for running a Python project.

- Python package requirements go in `requirements.txt`
- Project source code goes in `src/`

When the image is built, Docker will install the requirements and copy the project source code. The code will be ready to run when you start a container!

### 1. Build the image

```bash
~ > docker build -t 1-python -f Dockerfile .
Sending build context to Docker daemon  4.096kB
Step 1/7 : FROM python:3
 ---> fbf9f709ca9f
Step 2/7 : LABEL maintainer "your@email.com"
 ---> 810173b1607d
Step 3/7 : WORKDIR /home
 ---> 7d388fcbc176
Step 4/7 : COPY ./requirements.txt ./
 ---> d77ba6ba7810
Step 5/7 : RUN pip install -r requirements.txt
 ---> d79891acd7ce
Step 6/7 : ENV PYTHONPATH=/home
 ---> 31c3cc826b7e
Step 7/7 : COPY ./src ./src
 ---> 81977ce3526b
Successfully built 81977ce3526b
Successfully tagged 1-python:latest
```

### 2. Run a container
```bash
~ > docker run --rm -it 1-python bash
root@61ee92c144a1:/home# python src/hello.py
Hello, world!
```

### 3. Exit the container
```bash
root@61ee92c144a1:/home# exit
~ >
# The --rm flag in step 2 automatically removes the container upon exit
```
