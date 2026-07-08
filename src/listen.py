import serial, time
s = serial.Serial()
s.port = 'COM3'
s.baudrate = 115200
s.timeout = 1
s.dtr = False
s.rts = False
s.open()
print('Listening...')
while True:
    l = s.readline().decode('ascii', 'ignore').strip()
    if l: print(l)