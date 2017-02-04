# Component

Multiple service on single server

ansible 2.1+
ubuntu 16.04
docker 1.12+
node 6.7+
mongodb 3.2+


vitrual hosts via docker-compose and `docker network`


## parts

 1. init setup balancer with letsencrypt and nginx
 2. virtual host deploy
 3. deploy node
 4. zero downtime deploy
 5. backups and restore
 6. green blue deployment
 7. monitoring
 4. docker swarm


### problems

 1. security

### zero downtime

normal run: docker-compose up

nginx.upstream file:

  server app_node:port


OPTION 1

deploy:
1. docker up with new names `app_node_new`
2. wait app_node_new
3. add upstream app_node_new
4. wait
5. mark old servers as down
6. repeat all instance

OPTION 2

1. rename current container
2. update upstream
3. reload nginx
4. docker-compose up

OPTION 3
