#!/bin/bash

source docker_tag.sh
docker run \
    -d \
    --restart always \
    --name $name \
    -v $(pwd)/log.txt:/code/log.txt \
    $name:$tag