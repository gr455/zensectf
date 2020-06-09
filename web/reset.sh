#!/bin/bash

while true;
do
	echo "Restarting instances"
	docker-compose down
	docker-compose up -d

	sleep 300

done;