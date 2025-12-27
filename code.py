import time
import board
import digitalio
import usb_hid

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

pin = digitalio.DigitalInOut(board.GP7)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

last_input = 0.0
delay_s = 0.4  # secondes

while True:
    now = time.monotonic()
    if not pin.value and (now - last_input > delay_s):
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        last_input = now
    time.sleep(0.0005)
