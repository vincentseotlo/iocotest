# iocotest
This is an example python project, using flask to demonstate RESTFUL API
# howto run
1. clone the project: `git clone https://github.com/vincentseotlo/iocotest.git`
2. switch to this project's folder: `cd iocotest`
3. build the docker image: `docker build -t iocotech:latest .`
4. run the build image: `docker run --expose 5000 -p 15000:5000 iocotech`
5. On another terminal , you may try out the commands listed in test.sh. Please note that you will need to connect to port 15000 and not 5000. 
6. (us mac users, and everyone else having port-expose issues): please try out the following:
7. run `docker ps`, and copy the container-id for this project
8. ssh into the docker image: `docker exec -it 1fe9d0c541e9 /bin/sh`. Try out the commands from the test.sh using port 5000
```
vince@vinces-work iocotest % docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED        STATUS        PORTS                     NAMES
1fe9d0c541e9   15760e0feb10   "flask run"   10 hours ago   Up 10 hours   0.0.0.0:15000->5000/tcp   hello
```
