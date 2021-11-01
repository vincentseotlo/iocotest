# start from base
FROM ubuntu:latest
LABEL maintainer="Vincent Seotlo <vinceotlo@gmail.com>"
RUN apt-get update -y && \
apt-get install -y python3 python3-dev python3-pip curl

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install markupsafe
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD [ "flask", "run" ]

