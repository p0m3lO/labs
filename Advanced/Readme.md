# Advanced linux lab for linux

## 1. Task

### Basic Docker configuration

Install Docker, start the Docker service, and create a container using the 'nginx' image. The container should expose port 80 from the container to port 8080 on the host.

## 2. Task

### Confgiure a Basic Nginx reverse proxy and serve an application running in docker

Create a new Nginx site called ***gde-proxy***, that proxies requests to an application running as a ***docker-container*** called ***gde-app*** on ***port 3000*** and enable the new server block.