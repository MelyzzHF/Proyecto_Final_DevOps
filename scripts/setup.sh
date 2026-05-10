#!/bin/bash
# Automatización para entornos Ubuntu
set -e

echo "Actualizando paquetes..."
sudo apt-get update -y

echo "Instalando paquetes esenciales..."
sudo apt-get install -y git vim python3 python3-pip curl

# Validar/Instalar Docker
if ! command -v docker &> /dev/null; then
    echo "Instalando Docker..."
    sudo apt-get install -y docker.io
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -aG docker $USER
fi

# Instalar boto3 para Python
pip3 install boto3 --break-system-packages || pip3 install boto3

echo "--- Verificación de versiones ---"
git --version
docker --version
python3 --version
