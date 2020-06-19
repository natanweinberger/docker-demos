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



### FAQ

#### Are there any analogies for the Docker workflow?

I find it helpful to think of Docker's images and containers like having an operating system install disc and a computer.

| Action | Equivalent |
| --- | --- |
| Writing a Dockerfile | writing the code that will generate an OS install disc |
| Building an image | using that code to create an OS install disc |
| Removing an image | destroying the OS install disc |
| Creating a container | installing an OS onto a computer |
| Starting a container | turning on the computer |
| Stopping a container | shutting down the computer |
| Removing a container | uninstalling the OS |

#### What is the difference between stopping a container and removing a container?

Stopping a container shuts down all processes running in it and transitions the container to a "stopped" state. It will no longer show in the Docker active processlist, but it still exists. It can be restarted while preserving its state and any modifications you've made to the container since originally starting it.

On the other hand, removing a container deletes all state related to it and resources allocated to it. You can create a new container based on the same image, but the new container will be entirely oblivious to any changes you made in the last container.

Stopping a container is analagous to shutting down your computer. Removing a container is analogous to uninstalling the operating system.