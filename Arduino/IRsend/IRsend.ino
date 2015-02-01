#include <IRremote.h>
#include <IRremoteInt.h>

/*
 * IRremote: IRsendDemo - demonstrates sending IR codes with IRsend
 * An IR LED must be connected to Arduino PWM pin 3.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */



IRsend irsend;
int khz=38; //NB Change this default value as neccessary to the correct modulation frequency
unsigned tv_off[] = {8950, 4350, 650, 450, 650, 450, 650, 500, 600, 550, 550, 500, 650, 450, 650, 1550, 650, 500, 650, 1550, 650, 1600, 600, 1600, 650, 1550, 650, 1600, 600, 1600, 650, 450, 650, 1550, 650, 500, 600, 1600, 650, 450, 650, 450, 650, 1600, 600, 500, 650, 450, 650, 450, 650, 1600, 650, 450, 600, 1600, 650, 1550, 650, 500, 650, 1550, 650, 1600, 600, 1600, 650};
unsigned long tv_off_nec = 50153655;
int incomingCmd = 0;

void setup()
{
  Serial.begin(9600);
}

void loop() {
 //     irsend.sendRaw(tv_off, sizeof(tv_off)/sizeof(int), khz); // Sony TV power code
  if (Serial.available() > 0) {
    irsend.sendNEC(tv_off_nec, 32);
    incomingCmd = Serial.read();
    Serial.print("I received: ");
    Serial.println(incomingCmd, DEC);
  //    delay(5000);
  }
}
