import serial
import vgamepad as vg
import time


arduino = serial.Serial("COM3", 115200)
pad = vg.VDS4Gamepad()
print("\n123\n123\nstart")
pad.reset()
try:
    while True:
        data = arduino.readline().decode("utf-8").split(';')
        print(data)

        value = data[0].split(':')[0]
        pad.left_joystick_float((int(value, 16)-512)/512, 0)
        pad.update()
except KeyboardInterrupt as e:
    pad.reset()
    print("done")
    exit()