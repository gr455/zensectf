#!/bin/bash

#only redeploys all the images

docker stop $(docker ps -aq)

$(cd web/ ; ./reset.sh) & $(cd misc/ ; ./reset.sh);