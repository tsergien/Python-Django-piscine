#! /bin/sh
if [ "$#" -eq  "0" ]
    then
    echo "No arguments supplied"
else
    curl -s $* | grep href | grep  http | cut -d '"' -f 2
fi