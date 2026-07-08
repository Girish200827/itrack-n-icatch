#include <SoftwareSerial.h>

SoftwareSerial espSerial(7, 8);

String response = "";

void sendAT(String cmd, int waitMs) {
    espSerial.println(cmd);
    delay(waitMs);
    while (espSerial.available()) {
        char c = espSerial.read();
        response += c;
        Serial.write(c);
    }
    response = "";
}

void setup() {
    Serial.begin(115200);
    espSerial.begin(115200);
    delay(1000);

    Serial.println("Configuring ESP...");
    sendAT("AT", 1000);
    sendAT("AT+CWMODE=1", 1000);
    sendAT("AT+CWJAP=\"YourWiFiName\",\"YourWiFiPassword\"", 5000);
    sendAT("AT+CIFSR", 1000);
    sendAT("AT+CIPMUX=1", 1000);
    sendAT("AT+CIPSERVER=1,8080", 1000);  // Open port 8080

    Serial.println("SERVER READY - disconnect USB now");
}

void loop() {
    // Read incoming WiFi data from ESP
    if (espSerial.available()) {
        String msg = espSerial.readStringUntil('\n');
        msg.trim();
        Serial.println("WIFI_RX: " + msg);

        // Parse +IPD message from ESP
        // Format: +IPD,0,10:MOVE,1000
        if (msg.startsWith("+IPD")) {
            int colonIdx = msg.indexOf(':');
            if (colonIdx != -1) {
                String cmd = msg.substring(colonIdx + 1);
                cmd.trim();
                Serial.println("CMD: " + cmd);
                // ADD YOUR MOTOR CONTROL LOGIC HERE
            }
        }
    }
}
