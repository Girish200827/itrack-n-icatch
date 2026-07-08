//
// This script will perform a diagnostic test for
// stepper motor
//

#include <Stepper.h>

const int stepsPerRevolution = 2048;

Stepper myStepper = Stepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
    myStepper.setSpeed(5);
    
    Serial.begin(9600);
}

void loop() {
    Serial.println("clockwise");
    myStepper.step(stepsPerRevolution);
    delay(500);
    
    Serial.println("counter-clockwise");
    myStepper.step(-stepsPerRevolution);
    delay(500);
}
