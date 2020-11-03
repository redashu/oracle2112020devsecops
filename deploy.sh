#!/bin/bash

container_name=`docker ps -a |  grep -i ashuxccc1 |  wc -l`

if  [  $container_name -ge 1  ]
then
 	docker rm ashuxccc1  -f
	docker run --name ashuxccc1 -d -p 9988:5000 ashupyflask:oraclev001

else 
	echo "THis will for first time only.."
	docker run --name ashuxccc1 -d -p 9988:5000 ashupyflask:oraclev001
fi
