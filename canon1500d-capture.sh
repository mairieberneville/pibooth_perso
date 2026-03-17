#!/bin/bash
#!/bin/bash
set -x

# Script de capture Canon EOS 1500D pour Pibooth
# Usage: canon1500d-capture.sh <output_dir> <basename>

OUTDIR="$1"
BASENAME="$2"

# Si pas de dossier de sortie, utiliser ~/Pictures/pibooth
[ -z "$OUTDIR" ] && OUTDIR="$HOME/Pictures/pibooth"
mkdir -p "$OUTDIR"

# Capture avec séquence viewfinder ON -> trigger -> download -> viewfinder OFF
gphoto2 --set-config actions/viewfinder=1 \
        --trigger-capture \
        --wait-event-and-download=1s --filename "${OUTDIR}/${BASENAME}-%Y%m%d-%H%M%S.%C" \
        --set-config actions/viewfinder=0
