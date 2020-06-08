#!/bin/bash

while true;
do
	docker-compose kill -s SIGINT
	docker-compose up

	sleep 100

done;