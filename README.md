# Component

Multiple service on single server

ansible 2.1+
ubuntu 16.04
docker 1.12+
node 6.7+
mongodb 3.2+


vitrual hosts via docker-compose and `docker network`


## parts

 1. init setup balancer with letsecrypt and nginx
 2. virtual host deploy
 3. deploy node
 4. zero downtime deploy
 5. backups and restore
 6. green blue deployment
 7. monitoring
 4. docker swarm


### problems

 1. security
