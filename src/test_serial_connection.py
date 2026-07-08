import serial
import time
import threading

s = serial.Serial()
s.port = 'COM3'
s.baudrate = 115200
s.timeout = 1
s.dtr = False
s.rts = False
s.open()

print("Connected. Waiting for Arduino...")
time.sleep(2)

def read_loop():
    while True:
        try:
            line = s.readline().decode('ascii', 'ignore').strip()
            if line:
                print(f"\nArduino: {line}")
                print("You: ", end='', flush=True)
        except:
            break

t = threading.Thread(target=read_loop, daemon=True)
t.start()

while True:
    msg = input("You: ")
    if msg == 'exit':
        break
    s.write((msg + '\r\n').encode())  # <-- \r\n instead of \n

s.close()