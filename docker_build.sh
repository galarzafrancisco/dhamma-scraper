#!/bin/bash

source docker_tag.sh
docker build -t $name:$tag .
