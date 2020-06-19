# Docker demos

This repo contains examples of common Docker setups. Each directory is a standalone example with full instructions for getting started. You can use them as references or as a template!

For an intro to Docker, check out [this great post](https://www.rubytapas.com/2020/02/11/trying-stuff-in-docker-2/).


### Overview of Docker workflow and commands

A typical workflow in any directory:
- Write a Dockerfile
- Build the image
- Run a container

Familiarize yourself with these commands before diving in!

```bash
~ > docker build -t my-image -f ./Dockerfile .
# -t: after building, tag the image with the name "my-image"
# -f: use the file "./Dockerfile" to build the image
# .: Build from the current directory - any relative paths in the Dockerfile start from here
```

```bash
~ > docker run --rm -it my-image bash
# --rm: when we exit the container, remove it instead of keeping it in a stopped state
# my-image: use the image called my-image
# bash: this is the start-up function for the container - we want to be dropped into a bash shell
```
