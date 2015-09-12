FROM debian:jessie

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade google-api-python-client

WORKDIR /src
