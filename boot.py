import board, digitalio, storage

gp15 = digitalio.DigitalInOut(board.GP15)
gp15.direction = digitalio.Direction.INPUT
gp15.pull = digitalio.Pull.DOWN

# Si GP15 n'est PAS à la masse => pas de lecteur USB
if not gp15.value:
    storage.disable_usb_drive()
