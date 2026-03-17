"""
Plugin pibooth – Déclenchement du flash ESP au début du décompte
"""

import serial
import time
import pibooth
from pibooth.utils import LOGGER


__version__ = "1.3.2"



# === CONFIGURATION DU PORT SÉRIE ===
ESP_PORT = "/dev/espflash"   # ou /dev/ttyUSB1 selon ton udev
ESP_BAUDRATE = 115200
ESP_TIMEOUT = 2.0


@pibooth.hookimpl
def state_preview_enter(cfg, app, win):
    """
    Déclenche le flash ESP dès le début du compte à rebours (preview)
    """
    LOGGER.info("[ESP-FLASH] ⚡ Déclenchement anticipé du flash ESP (décompte en cours)...")

    try:
        ser = serial.Serial(ESP_PORT, ESP_BAUDRATE, timeout=ESP_TIMEOUT)
        time.sleep(0.2)  # délai de stabilisation du port série

        # --- Commande envoyée à l'ESP ---
        ser.write(b"START\n")
        ser.flush()
        LOGGER.info("[ESP-FLASH] Signal START envoyé à l’ESP ✅")

        time.sleep(0.1)
        ser.close()
        LOGGER.debug("[ESP-FLASH] Port série fermé proprement")

    except serial.SerialException as e:
        LOGGER.error(f"[ESP-FLASH] Erreur série : {e}")
    except Exception as e:
        LOGGER.error(f"[ESP-FLASH] Erreur inattendue : {e}")
