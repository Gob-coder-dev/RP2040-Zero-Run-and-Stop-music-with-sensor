# Play/Pause Music (Raspberry Pi Pico)

The Pico emulates a multimedia Play/Pause key via HID Consumer Control.

## Hardware
- One RP2040-Zero
- Small breadboard
- 3 jumper wires
- One sensor (e.g., IR presence sensor)
- One Usb-C cable
![base_image](https://github.com/user-attachments/assets/0359f5d5-0bb3-450b-bb21-cfeb137caf0b)

## Flash CircuitPython + libraries (first-time setup)
1. Unplug the board. Hold the **BOOT**/**BOOTSEL** button while connecting USB; a `RPI-RP2` drive appears.
2. Copy `adafruit-circuitpython-waveshare_rp2040_zero-fr-10.0.3.uf2` to `RPI-RP2`; the board reboots as a `CIRCUITPY` drive.
3. Copy `code.py` and `boot.py` to the root of `CIRCUITPY`.
4. Create `CIRCUITPY/lib` (if missing) and copy the `lib/adafruit_hid` folder there (the only external dependency used by `code.py`).
5. Eject the drive; the Pico is now ready to wire and test.

## Wiring
- `GP7` with internal pull-up: connect your sensor output so it pulls the pin low to trigger Play/Pause (e.g., IR presence sensor OUT pin).
- `GP15` (boot.py): tie to 3V3 when plugging in if you want to keep the USB drive mounted. Leaving it floating or to ground disables storage.

## Sensor configuration
- In `code.py:13`, `pin.pull = digitalio.Pull.UP` assumes the sensor drives the line low when triggered (as with the IR presence sensor used here). If your sensor drives high when active, change this to `Pull.DOWN`.
- In `code.py:20`, the check `if not pin.value` matches that active-low behavior. Flip the condition to `if pin.value` if your sensor outputs high when active.

## Behavior (code.py)
- Sets up the USB media key controller (`ConsumerControl`).
- Loop reads `GP7`; when the sensor output goes low it sends the `PLAY_PAUSE` command.
- 0.4 s debounce to avoid double presses.
- 0.5 ms pause between reads.

## Boot (boot.py)
- `GP15` is an input with pull-down.
- If `GP15` is not high on startup, `storage.disable_usb_drive()` turns off the USB drive.

USB drive off and program running :
![cable_location_running](https://github.com/user-attachments/assets/5ecf06bb-7a3f-41c0-a3d1-6693df7056a0)

USB drive on and program disabled :
![cable_location_debbug](https://github.com/user-attachments/assets/f64b90ba-2a3b-41fd-9a6c-356e74fb9694)

## Usage
1. Hook up your sensor: OUT to `GP7`, VCC to 3V3 (or 5V), GND to GND.
2. Optional: hold `GP15` at 3V3 before connecting USB to keep storage accessible.
3. Power the Pico from the target device; each sensor trigger sends Play/Pause to a HID-compatible host.
