// Arduino Uno 12V DC Stepper Motor
// Receives commands from TrackObject algorithm and controls the motor
//
// Wiring:
// Yellow --> RPWM
// Red --> LPWM
// 


// Motor A(1) PWM Pins
const int RPWM1 = 5;
const int LPWM1 = 6;

// Motor B(2) PWM Pins
const int RPWM2 = 9;
const int LPWM2 = 10;

// Motor C(3) PWM Pins
const int RPWM3 = 3;
const int LPWM3 = 11;

void setup() {

    // Motor A(1) Pin setup
    pinMode(RPWM1, OUTPUT);
    pinMode(LPWM1, OUTPUT);
    
    // Motor A(2) Pin setup
    pinMode(RPWM2, OUTPUT);
    pinMode(LPWM2, OUTPUT);
    
    // Motor A(3) Pin setup
    pinMode(RPWM3, OUTPUT);
    pinMode(LPWM3, OUTPUT);
}

void loop() {
    
    // Run the motor 360 degrees clockwise
    analogWrite(RPWM1, 255);
    analogWrite(LPWM1, 0);
    analogWrite(RPWM2, 255);
    analogWrite(LPWM2, 0);
    analogWrite(RPWM3, 255);
    analogWrite(LPWM3, 0);
    delay(10);
    
    // Run the motor 360 degrees counter-closkwise
    analogWrite(RPWM1, 0);
    analogWrite(LPWM1, 255);
    analogWrite(RPWM2, 0);
    analogWrite(LPWM2, 255);
    analogWrite(RPWM2, 0);
    analogWrite(LPWM2, 255);
    delay(10);
    
    // Stop the motor and exit the loop
    analogWrite(LPWM1, 0);
    analogWrite(LPWM2, 0);
    analogWrite(LPWM3, 0);
    exit(0);
}
