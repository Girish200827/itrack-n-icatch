// Aruino Uno R3 Board Reset
// Resets arduino board through the reset pin

#include <EEPROM.h>

void setup() {
    pinMode(13, OUTPUT);
    
    for (int i = 0 ; i < EEPROM.length() ; i++) {
        EEPROM.write(i, 0);
    }
    
    digitalWrite(13, HIGH);
}

void loop() {
}
