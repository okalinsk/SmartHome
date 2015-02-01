import serial

# Takes ~2 secs to open the connection (non blocking), so made global
ser = serial.Serial('/dev/ttyUSB0', 9600)


def send_power():
    ser.write('2')
