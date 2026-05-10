#!/bin/bash

echo " Error detectado en el despliegue. Iniciando Rollback automático..."

# 1. Retroceder un commit en el historial de Git para volver a la versión estable
git reset --hard HEAD~1

# 2. Apagar los contenedores actuales que están fallando
sudo docker compose down

# 3. Reconstruir y encender los contenedores con el código recuperado
sudo docker compose up -d --build

echo  " Rollback completado. El sistema S.T.F. ha sido restaurado a la última versión estable."
