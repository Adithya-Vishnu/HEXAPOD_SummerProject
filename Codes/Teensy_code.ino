/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo coxa;
Servo femur;
Servo tibia;
const int coxa_pin=2;
const int femur_pin=3;
const int tibia_pin =4;   // variable to store the servo position

double alpha,beta,gamma;

const double Angles[41][3] = {
    {68.2, 136.66, 75.11},
    {67.67, 139.04, 75.8},
    {67.13, 141.32, 76.32},
    {66.56, 143.48, 76.66},
    {65.97, 145.54, 76.82},
    {65.36, 147.48, 76.81},
    {64.73, 149.3, 76.61},
    {64.06, 151.0, 76.24},
    {63.36, 152.56, 75.7},
    {62.63, 153.99, 74.97},
    {61.86, 155.29, 74.06},
    {61.04, 156.44, 72.97},
    {60.17, 157.45, 71.69},
    {59.23, 158.31, 70.22},
    {58.21, 159.01, 68.54},
    {57.09, 159.54, 66.67},
    {55.85, 159.9, 64.57},
    {54.42, 160.09, 62.24},
    {52.72, 160.08, 59.67},
    {50.47, 159.86, 56.81},
    {45.0, 159.43, 53.65},
    {39.53, 159.86, 56.81},
    {37.28, 160.08, 59.67},
    {35.58, 160.09, 62.24},
    {34.15, 159.9, 64.57},
    {32.91, 159.54, 66.67},
    {31.79, 159.01, 68.54},
    {30.77, 158.31, 70.22},
    {29.83, 157.45, 71.69},
    {28.96, 156.44, 72.97},
    {28.14, 155.29, 74.06},
    {27.37, 153.99, 74.97},
    {26.64, 152.56, 75.7},
    {25.94, 151.0, 76.24},
    {25.27, 149.3, 76.61},
    {24.64, 147.48, 76.81},
    {24.03, 145.54, 76.82},
    {23.44, 143.48, 76.66},
    {22.87, 141.32, 76.32},
    {22.33, 139.04, 75.8},
    {21.8, 136.66, 75.11}
};


void setup(){
  coxa.attach(coxa_pin);
  femur.attach(femur_pin);
  tibia.attach(tibia_pin);
  

 

}

void loop() {
  
  // int alpha=45;
  // coxa.write(2*alpha);
  // delay(75);
  // femur.write(129.56);
  // delay(75);
  // tibia.write(64.21);
  // delay(75);

  for(int i=0;i<41;i=i+1){
    alpha=Angles[i][0];
    beta=Angles[i][1];
    gamma=Angles[i][2];
    coxa.write(2*alpha);
    delay(25);
    femur.write(beta);
    delay(25);
    tibia.write(gamma);
    delay(25);

  }
  



}
