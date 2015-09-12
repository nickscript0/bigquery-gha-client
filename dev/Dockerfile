FROM debian:jessie

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade google-api-python-client

RUN mkdir /credentials
COPY ./private/bigquery_bha_service_auth.json /credentials/
COPY ./private/project_id /credentials/
ENV GOOGLE_APPLICATION_CREDENTIALS /credentials/bigquery_bha_service_auth.json
WORKDIR /src
