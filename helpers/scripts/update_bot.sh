#!/bin/bash

CONTAINER_NAME="PalworldDiscordBot"
IMAGE_NAME="headbanggang/palworld-discord-bot"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

docker pull $IMAGE_NAME

docker run -d \
  --name $CONTAINER_NAME \
  -v /mnt/user/appdata/palworld/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini:/docs/PalWorldSettings.ini \
  -v /mnt/user/appdata/palworld-discord-bot/.env:/.env \
  -v /mnt/user/appdata/palworld-discord-bot/ssh_key:/docs/ssh_key \
  $IMAGE_NAME