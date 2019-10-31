FROM python:3-slim

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install libyaml-dev
RUN apt-get clean

WORKDIR /app
COPY . .
RUN python3 setup.py install

ENTRYPOINT ["pippa"]
