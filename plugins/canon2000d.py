import subprocess
import time
import pibooth
from pibooth.utils import LOGGER

@pibooth.hookimpl
def state_capture_do(app, cfg, win, events):
    """Capture avec Canon EOS 2000D via eosremoterelease."""
    LOGGER.info("Déclenchement Canon EOS 2000D via eosremoterelease")

    # Forcer la capture sur carte SD
    subprocess.call(["gphoto2", "--set-config", "capturetarget=1"])

    # Déclenchement immédiat
    subprocess.call(["gphoto2", "--set-config", "eosremoterelease=Immediate"])
    time.sleep(2)  # Attendre que la photo soit écrite

  # Télécharger la nouvelle photo dans le dossier raw de pibooth
    subprocess.call([
        "gphoto2", "--get-all-files", "--new",
        "--filename", app.dirname_capture + "/capture_%Y%m%d-%H%M%S.jpg"
    ])
