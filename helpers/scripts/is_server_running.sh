#!/bin/bash

docker ps --format '{{.Names}}' | grep -q "^Palworld$" && echo "true" || echo "false"
