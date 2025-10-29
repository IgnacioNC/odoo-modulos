#!/bin/bash
RUTA_PROYECTO="/home/Nacho/instalaciones-odo/custom-addons"
FLAG="$RUTA_PROYECTO/actualizar_odoo.sh"

if [ ! -f "$FLAG" ]; then
    cd "$RUTA_PROYECTO" || exit 1
    touch "$FLAG"
else
    cd "$RUTA_PROYECTO" || exit 1
    git pull origin main
fi
