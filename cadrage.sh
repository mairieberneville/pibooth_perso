#!/bin/bash

# 1) On arrête Pibooth s'il tourne encore
pkill -f pibooth 2>/dev/null
pkill -f start_pibooth.py 2>/dev/null
pkill -f python3 2>/dev/null

# 2) On libère l'écran graphique
export DISPLAY=:0

# 3) Lancer un aperçu simple avec gphoto2
#   (on commence par --capture-preview, plus simple que la vidéo)
echo "Lancement du cadrage caméra (aperçu)..."
echo "Ctrl+C dans la fenêtre pour quitter."

gphoto2 --capture-preview --stdout | display -
