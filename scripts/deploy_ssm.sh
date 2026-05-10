#!/bin/bash
cd /home/ubuntu/environment/proyecto-st
git pull origin develop
docker-compose down
docker-compose up -d --build
echo "Despliegue ejecutado con éxito"
