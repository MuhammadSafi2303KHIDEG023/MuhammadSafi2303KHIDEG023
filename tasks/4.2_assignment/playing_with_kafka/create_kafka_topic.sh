#!/bin/bash


# Commands to create topics 

docker-compose exec broker kafka-topics --create --topic events_initial --bootstrap-server broker:9092
docker-compose exec broker kafka-topics --create --topic events_urgent --bootstrap-server broker:9092
docker-compose exec broker kafka-topics --create --topic events_consumer --bootstrap-server broker:9092 --partitions 4
# /////////////////


# Commmand to list all Topics
docker-compose exec broker kafka-topics --bootstrap-server broker:9092 --list
