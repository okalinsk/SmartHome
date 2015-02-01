import serial


ser = None


def init():
    # Takes ~2 secs to open the connection (non blocking), so made global
    global ser
    ser = serial.Serial('/dev/ttyUSB1', 9600)


def send_power():
    ser.write('2')
