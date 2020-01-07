# Docker
Tutorial: https://www.youtube.com/watch?v=MU8HUVlJTEY&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=7
Virtual Docker: https://labs.play-with-docker.com
Cheat Cheat: https://github.com/wsargent/docker-cheat-sheet

## Summary

**Image:** ready to run system that can be started one or several times in one or more containers

**Container:** one image that is started/loaded in docker

![Docker Architecture](../../images/Docker-architecture.png "High Level Docker Architecture")


## Basics Commands
Show details about docker installation `docker version`
Show only Version: `docker -v` or `docker  --version`
Show more information: `docker info`
Help page: `docker --help`

## Image Commands
Show local images: `docker images` 
Pull docker image from docker hub: `docker pull ubuntu`
Remove image: `docker rmi ubuntu`
Prune unused images: `docker images prune` 

## Container Commands
Show running containers: `docker ps` or `docker ps -a`
create and start container: `docker run ubuntu`
create amd start linux container and login as root on bash `docker run -it ubuntu`
create and start container and forward port `docker run -p 3001:8080 ubuntu`
stop a container: `docker stop ubuntu`
start a already created container `docker start ubuntu`
**login to the shell of a running linux container** `docker exec -it ubuntu /bin/bash`
pause a container: `docker pause/unpause ubuntu`
connect to a running container: `docker attach ubuntu`
remove a containter: `docker rm CONTAINER_ID/CONTAINER_NAME` 
remove all stoped containers: `docker container prune` 

## Usefull Commands
Need explicit port forwarding due to my Pow/Anwil web server
Command: `docker run -p 3001:8080 -d --name test jenkins`
Port forwarding: `-p portnumber on my mac:port where the docker app outputs`
Run as deamon in the background `-d`
Give it a dedicated name `--name`

## Build Docker Image
This is about how to build a own docker image either by creating it from the scratch or using an existing image like a ubuntu linux
https://github.com/wsargent/docker-cheat-sheet#dockerfile 

The basic approach is to create a dockerfile and insert the order
```
FROM
RUN
CMD
```
or as an example file Desktop/Dockerfile
```
# filename: Dockerfile

# getting base image ubuntu
FROM ubuntu

MAINTAINER Alex Ortner <alex.ortner@record-evolution.de>

RUN apt-get update

CMD ["echo", "My First Docker Image"]
```

built the image `docker built -t myimage1:mytag`
show the new image `docker images`
create container and start the new image `docker run myimage1/imageID`


## Docker Compose
Docker compose is used to start up several containers together with some configuration and scale it.
Example one Webserver and several databas server

The aproach to create a configuration yaml file that contains all containters that should be started

example file /Desktop/docker-compose.yml
```
# filename: docker-compose.yml

version: '3'

services:

  web:
    image: nginx
    ports:
    - 3002:80

  database:
    image: redis  

```
In a yaml file alway two spaces have to be used to tab into the next level 

Check if the confugration is correct `docker-compose cofig`

Run the composed setup `docker-compose up -d`
Stop the composed setup `docker-compose down`
Scale one of the containers on starting `docker-compose up -d --scale database=4`

## Docker Volume
Define a fixed volume on the docker host or somewhere in the network where the containers map the data in and out.
Can be used to load similar configurations to different containers or to store data out that where created in the container.
In general if a container is removed all data in the container are lost

Get Information: `docker volume`
Create a volume: `docker volume create MyVolume1 `
Check what volumes are available: `docker volume ls`
Remove a volume or all unused volumes: `docker volume rm MyVolume1` or `docker volume prune`
Start a container with using a docker volume: `docker run -v MyVolume1:/var/jenkins_home` 
Startt a container using a local folder `docker run -v /Users/tingel/Desktop:/var/jenkins_home`


## Docker Swarm
A swarm is a group of machines that are running Docker and joined into a cluster 
This swarm can be managed certain tools. This tools are Orchestration tools to mange and control multiple docker containers as a single service. Docker Swarm is one tool, other tools are Kubernetes or Apache Mesos

Example
You have 100 containers
You need to do 
- Health check on every container
- Ensure all containers are up on every system
- Scaling the containers up or down depending on the load
- Adding updates/changes to all the containers


## Usefull Images
a lot of images can be loaded directly from https://hub.docker.com/ 
I like the following images

| Image | Tag | Linux | Package Manger | Comment | Comand|
|-------|-----|-------|----------------|---------|---------|
|  python    |  3.7   |    Debian      | apt-get |   full Python available      | `FROM python:3.7` |
|  postgres  | latest |    Debian  	   | apt-get |   Postgres database          | `FROM postgreas`     | 
|  rabbitmq  | latest |       			|                |            |		|
|metabase/metabase| latest | | | Metabase BI tool | `FROM metabase/metabase` |



## Portainer.io
Portainer.io (https://www.portainer.io/) is a web based UI to manage docker containers

Can be started directly via a docker image  

```
docker volume create portainer_data

docker run -d -p 8000:8000 -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```
and then accessed via
http://localhost:9000 

![Portainer.io](../../images/s_docker_portainer1.png "Portainer.io")

![Portainer.io](../../images/s_docker_portainer2.png "Portainer.io")

![Portainer.io](../../images/s_docker_portainer3.png "Portainer.io")
![Portainer.io](../../images/s_docker_portainer4.png "Portainer.io")




