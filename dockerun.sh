#!/bin/sh

BASEDIR=$(cd $(dirname $0) && pwd)
docker run -i -t -p 8000:8000 -v $BASEDIR:/app uragf $@
