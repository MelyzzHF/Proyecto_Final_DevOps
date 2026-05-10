#!/bin/bash
cd /home/ssm-user/proyecto-st
git pull origin develop
docker-compose down
docker-compose up -d --build
echo "Despliegue ejecutado con éxito"
