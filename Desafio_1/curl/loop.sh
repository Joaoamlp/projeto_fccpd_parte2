#!/bin/sh

URL="http://flask:8080/"
INTERVALO=10

while true
do
    echo "Realizando requisição em $(date)"
    curl -s "$URL"
    echo "\n"
    sleep $INTERVALO
done
