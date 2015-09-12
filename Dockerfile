FROM debian:jessie

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade google-api-python-client

RUN mkdir /credentials
COPY ./private/bigquery-bha-oauth2.json /credentials/
ENV GOOGLE_APPLICATION_CREDENTIALS /credentials/bigquery-bha-oauth2.json
WORKDIR /src
