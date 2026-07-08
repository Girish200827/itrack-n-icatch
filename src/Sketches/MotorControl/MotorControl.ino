// Motor Position Control using Encoder Feedback 
// Arduino Uno + 12V DC motors with encoders + ESP-01S
//  
// Robot moves until encoder count reaches 1000
// then stops automatically.
//
// Wiring:
// Yellow --> RPWM
// Red --> LPWM
// Green --> Channel B
// Yellow --> Channel A


// Motor PWM Pins
const int RPWM1 = 5, LPWM1 = 6; //  A(1) top 
const int RPWM2 = 9, LPWM2 = 10; // B(2) bottom-right
const int RPWM3 = 3, LPWM3 = 11; // C(3) bottom-left 

const int SPD     = 255; // set to max speed
const int RUN_MS  = 1500; // more will execute the test for longer
const int PAUSE_MS = 0; // no pause

void motora(int fwd, int rev) { analogWrite(RPWM1, fwd); analogWrite(LPWM1, rev); }
void motorb(int fwd, int rev) { analogWrite(RPWM2, fwd); analogWrite(LPWM2, rev); }
void motorc(int fwd, int rev) { analogWrite(RPWM3, fwd); analogWrite(LPWM3, rev); }

void stopall() {
    motora(0, 0);
    motorb(0, 0);
    motorc(0, 0);
    delay(PAUSE_MS);
}

void moveforward()      { motora(0,   SPD); motorb(SPD, 0);   motorc(SPD, 0);   }
void movebackward()     { motora(SPD, 0);   motorb(0,   SPD); motorc(0,   SPD); }
void moveleft()         { motora(SPD, 0);   motorb(SPD, 0);   motorc(0,   SPD); }
void moveright()        { motora(0,   SPD); motorb(0,   SPD); motorc(SPD, 0);   }
void diagfwdleft()      { motora(0,   0);   motorb(SPD, 0);   motorc(0,   SPD); }
void diagfwdright()     { motora(0,   0);   motorb(0,   SPD); motorc(SPD, 0);   }
void diagbwdleft()      { motora(SPD, 0);   motorb(0,   SPD); motorc(0,   0);   }
void diagbwdright()     { motora(0,   SPD); motorb(0,   0);   motorc(SPD, 0);   }
void rotatecw()         { motora(SPD, 0);   motorb(SPD, 0);   motorc(SPD, 0);   }
void rotateccw()        { motora(0, SPD);   motorb(0,   SPD); motorc(0,   SPD); }

void runtest(const char* name, void (*fn)()) {
    Serial.print("Moving: ");
    Serial.println(name);
    fn();
    delay(RUN_MS);
    stopall();
}

void setup() {
    Serial.begin(115200);
    pinMode(RPWM1, OUTPUT); pinMode(LPWM1, OUTPUT);
    pinMode(RPWM2, OUTPUT); pinMode(LPWM2, OUTPUT);
    pinMode(RPWM3, OUTPUT); pinMode(LPWM3, OUTPUT);
    stopall();
    delay(2000);
    Serial.println("Starting motion test...");
}

void loop() {
    runtest("Diag fwd-left",   diagfwdleft);
    runtest("Diag fwd-right",  diagfwdright);
    runtest("Diag bwd-left",   diagbwdleft);
    runtest("Diag bwd-right",  diagbwdright);
    runtest("Rotate CW",       rotatecw);
    runtest("Rotate CCW",      rotateccw);
    runtest("Forward",         moveforward);
    runtest("Backward",        movebackward);
    runtest("Left",            moveleft);
    runtest("Right",           moveright);
    Serial.println("Test complete. Restarting in 3s...");
    delay(3000);
}
