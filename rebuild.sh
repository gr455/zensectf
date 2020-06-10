#!/bin/bash

# rebuilds all docker images and redeploys containers

docker stop $(docker ps -aq)

$(cd web/ ;  docker-compose build);
$(cd misc/ ; docker-compose build);

$(cd web/ ; ./reset.sh) & $(cd misc/ ; ./reset.sh);
