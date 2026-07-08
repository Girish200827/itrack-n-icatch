#include <SoftwareSerial.h>

SoftwareSerial espSerial(7, 8);  // RX=7, TX=8

void setup() {
    Serial.begin(115200);        // USB <--> PC
    espSerial.begin(9600);       // Arduino <--> ESP (9600 is safe)
    delay(2000);
    Serial.println("READY");
}

void loop() {
    // USB --> ESP (one byte at a time)
    if (Serial.available()) {
        char c = Serial.read();
        espSerial.write(c);
    }

    // ESP --> USB (one byte at a time)  
    if (espSerial.available()) {
        char c = espSerial.read();
        Serial.write(c);
    }
}
