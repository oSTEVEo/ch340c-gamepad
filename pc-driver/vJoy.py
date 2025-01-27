import serial
import vgamepad as vg
import time
import joylib

DEBUG = True    # with debug data string is DEBUG_DATA 
DEBUG_DATA = "128:256;780:350;0;0;0"
class dbgClass():
    def readline(self):
        return DEBUG_DATA.encode()
def reform(inp : str): # from "X:Y" to (x, y)
    return tuple(map(int, inp.split(":")))

if not DEBUG:
    arduino = serial.Serial("COM3", 115200)
else:
    arduino = dbgClass()

pad = vg.VDS4Gamepad()
pad.reset()
cameraJoy = joylib.Gamepad(pad)
moveJoy = joylib.Gamepad(pad)
try:
    while True:
        seg_data = arduino.readline().decode("utf-8").split(';')
        print(seg_data)

        x, y = cameraJoy.getComputed(reform(seg_data[0]))
        pad.left_joystick_float(x,y)
        x, y = cameraJoy.getComputed(reform(seg_data[1]))
        pad.right_joystick_float(x,y)
        pad.update()
except KeyboardInterrupt as e:
    pad.reset()
    print("done")
    exit()