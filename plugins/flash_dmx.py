import serial
import time
import threading
import pibooth

__version__ = "1.0.0"

DMX_PORT = "/dev/ttyUSB0"
_dmx_thread = None
_running = False

def _send_loop(dimmer, strobe):
    global _running
    try:
        s = serial.Serial(DMX_PORT, baudrate=250000,
                          bytesize=8, parity='N', stopbits=2)
        while _running:
            s.break_condition = True; time.sleep(0.001)
            s.break_condition = False; time.sleep(0.0001)
            s.write(bytes([0, dimmer, strobe, 0]))
            time.sleep(0.025)
        for _ in range(20):
            s.break_condition = True; time.sleep(0.001)
            s.break_condition = False; time.sleep(0.0001)
            s.write(bytes([0, 0, 0, 0]))
            time.sleep(0.025)
        s.close()
    except Exception as e:
        print(f"[DMX] Erreur: {e}")

def flash_on(dimmer=255, strobe=0):
    global _dmx_thread, _running
    _running = True
    _dmx_thread = threading.Thread(target=_send_loop, args=(dimmer, strobe), daemon=True)
    _dmx_thread.start()

def flash_off():
    global _running
    _running = False
    if _dmx_thread:
        _dmx_thread.join(timeout=2)

@pibooth.hookimpl
def state_capture_enter():
    flash_on(dimmer=255, strobe=0)

@pibooth.hookimpl
def state_capture_exit():
    flash_off()

@pibooth.hookimpl
def pibooth_cleanup():
    flash_off()
