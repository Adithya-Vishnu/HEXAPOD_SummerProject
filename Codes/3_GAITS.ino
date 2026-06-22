//master code
#include <Wire.h>
#include <Servo.h>


Servo coxa;
Servo femur;
Servo tibia;

Servo coxa2;
Servo femur2;
Servo tibia2;

Servo coxa3;
Servo femur3;
Servo tibia3;

const int coxa_pin=2;
const int femur_pin=3;
const int tibia_pin =4;
 
const int coxa2_pin=11;
const int femur2_pin=6;
const int tibia2_pin=7;

const int coxa3_pin=8;
const int femur3_pin=9;
const int tibia3_pin=10;
   //variable to store the servo position

double alpha,beta,gamma,alpha2,beta2,gamma2;

const double Angles[21][3] = {{45.0, 140.02, 120.8}, {44.49, 144.5, 123.15}, {43.94, 149.06, 125.37}, {43.35, 153.71, 127.46}, {42.71, 158.42, 129.4}, {42.01, 163.2, 131.21}, {41.22, 168.02, 132.87}, {40.31, 172.89, 134.4}, {39.21, 177.84, 135.81}, {27.4, 179.26, 141.22}, {26.33, 174.61, 140.6}, {25.38, 169.71, 139.66}, {24.51, 164.67, 138.44}, {23.71, 159.54, 136.96}, {22.96, 154.41, 135.25}, {22.26, 149.31, 133.33}, {21.59, 144.28, 131.23}};
const double Angles2[21][3]={{45.0, 140.02, 120.8}, {45.0, 143.85, 121.82}, {45.0, 147.56, 122.59}, {45.0, 162.49, 121.72}, {45.0, 164.3, 120.27}, {45.0, 165.32, 117.99}, {45.0, 162.99, 111.76}, {45.0, 155.41, 105.17}, {45.0, 150.83, 102.15}, {45.0, 146.71, 99.57}, {45.0, 142.82, 97.14}, {45.0, 139.04, 94.74}, {45.0, 135.33, 92.31}, {45.0, 131.65, 89.82}, {45.0, 128.0, 87.23}, {45.0, 124.37, 84.53}, {45.0, 120.72, 81.71}};
const double Angles3[21][3]={{21.59, 112.87, 67.05}, {22.26, 115.66, 68.63}, {22.96, 118.33, 69.99}, {23.71, 120.89, 71.13}, {24.51, 123.33, 72.03}, {25.38, 125.64, 72.71}, {26.33, 127.8, 73.14}, {27.4, 129.79, 73.29}, {39.21, 126.34, 64.81}, {40.31, 123.46, 63.05}, {41.22, 120.57, 61.23}, {42.01, 117.61, 59.28}, {42.71, 114.6, 57.15}, {43.35, 111.49, 54.83}, {43.94, 108.26, 52.27}, {44.49, 104.91, 49.43}, {45.0, 101.39, 46.26}};
void setup(){
  Serial.begin(9600);
  Wire.begin();
  coxa.attach(coxa_pin);
  femur.attach(femur_pin);
  tibia.attach(tibia_pin);

  coxa2.attach(coxa2_pin);
  femur2.attach(femur2_pin);
  tibia2.attach(tibia2_pin);

  coxa3.attach(coxa3_pin);
  femur3.attach(femur3_pin);
  tibia3.attach(tibia3_pin);
}
void loop() {
  Serial.println("At start of loop");
  for(int i=0;i<17;i=i+1){
    // alpha=Angles[i][0];
    // beta=Angles[i][1];
    // gamma=Angles[i][2];

    // alpha2=Angles2[i][0];
    // beta2=Angles2[i][1];
    // gamma2=Angles2[i][2];

    coxa.write(180-2*(Angles[i][0]));
    coxa2.write(180-2*(Angles3[i][0]));
    coxa3.write(180-2*(Angles2[i][0]));
    delay(20);

    femur.write(Angles[i][1]);
    femur2.write(Angles3[i][1]);
    femur3.write(Angles2[i][1]);
    delay(20);

    tibia.write(Angles[i][2]);
    tibia2.write(Angles3[i][2]);
    tibia3.write(Angles2[i][2]);
    delay(20);
    

  }
  Serial.println("End of loop");
  Wire.beginTransmission(8);
  Wire.write(1);
  delay(20000);
  Wire.endTransmission();
  
  Wire.beginTransmission(8);
  Wire.write(0);
  Wire.endTransmission();
}