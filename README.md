# CTF DEMO 
This is a demo application and a simple CTF exercise.

## Fast follow along CTF (sponsored by Heroku Student Pack)
The fastest way to check the app is this link:


https://hacking-ctf0x1-fils.herokuapp.com/CTF-WebApp-1.0-SNAPSHOT/

## Pre-requisite
- Burp Suite
- Docker & Docker Engine
- Java >=17 

## How to run
Pull the docker image
```
docker pull sebnae/docker-ctf
```
Run the container
```
docker run -p 80:8080 sebnae/docker-ctf
```
Go to this link http://localhost:80/CTF-WebApp-1.0-SNAPSHOT/


If you have the port 80 already in use please use another one and change the link accordingly
## All you need is command
Hello, you have a simple application that list the files from the server, can you find what you are looking for??

## CTF
This CTF contains multiple vulnerabilitis. All of those can be exploited using only basic commands and tools provided by Burp Suite.

## CTF - Capture the flag
The format for the flags is:<b>
BlackLabs{----x----x----x----}</b>
