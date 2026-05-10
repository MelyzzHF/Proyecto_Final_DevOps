#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

function mostrar_ayuda() {
    echo -e "${YELLOW}====================================================${NC}"
    echo -e "${GREEN}   SISTEMA DE GESTIÓN - SOLUCIONES TECNOLÓGICAS${NC}"
    echo -e "${YELLOW}====================================================${NC}"
    echo "Uso: $0 [comando] [argumentos]"
    echo ""
    echo "Comandos disponibles:"
    echo "  crear [nombre] [depto] - Crea usuario en depto (devops|dev|audit)"
    echo "  eliminar [nombre]      - Elimina usuario y su carpeta personal"
    echo "  listar                 - Muestra usuarios por departamento"
    echo "  ayuda                  - Muestra este menú"
    echo -e "${YELLOW}----------------------------------------------------${NC}"
}

comando=$1

case $comando in
    crear)
        user=$2
        dept=$3
        if [ -z "$user" ] || [ -z "$dept" ]; then
            echo -e "${RED}Error: Faltan argumentos.${NC}"
            mostrar_ayuda
            exit 1
        fi

        # Crear grupo de departamento si no existe
        sudo groupadd -f "$dept"

        # Crear usuario si no existe
        if ! id "$user" &>/dev/null; then
            # Se asigna el departamento como grupo primario (-g)
            sudo useradd -m -g "$dept" -s /bin/bash "$user"
            echo -e "${GREEN}✔ Usuario '$user' creado y asignado a '$dept'.${NC}" 
            # Asignación de permisos lógicos
            if [ "$dept" == "devops" ]; then
                sudo usermod -aG sudo "$user"
                echo -e "${YELLOW}  [!] Permisos de SUDO asignados.${NC}"
            fi
            if [ "$dept" == "audit" ] || [ "$dept" == "dev" ]; then
                sudo usermod -aG adm "$user"
                echo -e "${YELLOW}  [!] Permisos de lectura de LOGS asignados.${NC}"
            fi
        else
            echo -e "${RED}✘ El usuario '$user' ya existe en el sistema.${NC}"
        fi
        ;;

    eliminar)
        user=$2
        if [ -z "$user" ]; then
            echo -e "${RED}Error: Indica el usuario a eliminar.${NC}"
            exit 1
        fi
        sudo userdel -r "$user" 2>/dev/null
        echo -e "${GREEN}✔ Usuario '$user' y su directorio han sido eliminados.${NC}"
        ;;

    listar)
        echo -e "${GREEN}--- REPORTE DE USUARIOS POR DEPARTAMENTO ---${NC}"
        # Iteramos sobre los departamentos clave del caso de estudio
        for dept in devops dev audit; do
            echo -e "\nDepartamento: [${YELLOW}${dept}${NC}]"

            # Obtener el ID numérico (GID) del departamento
            GID=$(getent group "$dept" | cut -d: -f3)

            if [ -z "$GID" ]; then
                echo "  (El departamento aún no tiene usuarios)"
            else
                # Buscar usuarios cuyo grupo primario coincida con el GID
                awk -v gid="$GID" -F: '$4 == gid {print "  - " $1}' /etc/passwd

                # Buscar usuarios secundarios agregados al grupo
                getent group "$dept" | cut -d: -f4 | tr ',' '\n' | sed '/^$/d' | sed 's/^/  - /'
            fi
        done
        echo -e "\n${GREEN}--------------------------------------------${NC}"
        ;;

    ayuda|*)
        mostrar_ayuda
        ;;
esac
