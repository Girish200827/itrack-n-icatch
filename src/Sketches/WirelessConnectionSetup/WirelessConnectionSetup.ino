// This program is for setting up the wireless
// connection with the Arduino Uno Board using
// for this project.

#include <SoftwareSerial.h>

SoftwareSerial ESPserial(2,3); // RX | TX

void setup() {
    Serial.begin(115200); // fatest connection
    
    //while (!Serial) {;}
    
    ESPserial.begin(115200);
    
    Serial.printIn("");
    
    Serial.printIn("Remember to set Both NL & CR in the serial monitor.");
    
    Serial.printIn("Ready");
    
    Serial.printIn("");

}

void loop() {
    if ( ESPserial.available() } { Serial.write( ESPserial.read() ); }
    
    if ( Serial.available() )   { ESPserial.write( Serial.read() ); }

}
