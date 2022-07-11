# project_nlp_with_nltk
This repository is trying to explain how to use natural language toolkit in order to do natural language processing

## Table of Contents
* [Docker image](#docker-image)
* [Docker build](#docker-build)
* [Docker run and execute](#docker-run-and-execute)

## Docker image
First of all we are going to use docker to prepare the environment.

This is the Dockerfile were we can see how to install python and library vaderSentiment.
```sh
FROM ubuntu:latest

COPY . /tmp/

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install nltk && \
    python3 -m nltk.downloader all
```

## Docker build
We need to create the docker image in order to launch / execute the code. This is the way to create the docker image
```sh
docker build -t python_nlp_nltk .
```

## Docker run and execute
Now we are able to use the image with the next command
```sh
docker run -it python_nlp_nltk /bin/bash
```