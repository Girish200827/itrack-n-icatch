import serial
import time

print("Attempting to connect to COM3")

try:
    ser = serial.Serial()
    ser.port = "COM3"
    ser.baudrate = 115200
    ser.timeout = 1
    ser.dtr = False
    ser.rts = False
    ser.open()
    print("Port opened successfully")
except Exception as e:
    print(f"FAILED to open port: {e}")
    exit()

time.sleep(3)

print("Sending MOVE,1000")
ser.write(b"MOVE,1000\n")

last_received = time.time()
FREEZE_TIMEOUT = 5 # seconds with no data = frozen

while True:
    try:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        
        if line:
            print(f"[{time.strftime('%H:%M:%S')}] {line}")
            last_received = time.time()
        else:
            elapsed = time.time() - last_received
            if elapsed > FREEZE_TIMEOUT:
                print(f"WARNING: No data for {elapsed:.1f}s. Arduino may be frozen or not running sketch")
                last_received = time.time()
            
    except KeyboardInterrupt:
        print("Exiting")
        ser.close()
        break
    except Exception as e:
        print("Error:", e)