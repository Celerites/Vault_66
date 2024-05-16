#include <Servo.h>
#include <ServoSquared.h>

ServoSquared servo_Base, servo_Brazo1, servo_Brazo2, servo_Brazo3, servo_Brazo4, servo_Gripper;

int pinServoBase= 3;      // Definir pin de servo
int pinServoBrazo1= 5;
int pinServoBrazo2= 6;
int pinServoBrazo3= 9;
int pinServoBrazo4= 10;
int pinServoGripper= 11;

String inputString;

void setup() {

  Serial.begin(9600); 

  servo_Base.attach(pinServoBase);// 
  servo_Brazo1.attach(pinServoBrazo1);
  servo_Brazo2.attach(pinServoBrazo2);
  servo_Brazo3.attach(pinServoBrazo3);
  servo_Brazo4.attach(pinServoBrazo4);
  servo_Gripper.attach(pinServoGripper);
}

void loop() {
  if (Serial.available()) {
    readSerial(); // Leer serial desde el GUI
    readSerialButton();

  }

  servo_Base.updatePosition(); // Actualizar ubicaciones de los servos
  servo_Brazo1.updatePosition();
  servo_Brazo2.updatePosition();
  servo_Brazo3.updatePosition();
  servo_Brazo4.updatePosition();
  servo_Gripper.updatePosition();
}

void readSerial() {
  String data = Serial.readStringUntil('\n'); // leer linea hasta nueva linea
  data.trim(); // quitar espacio

  // dividir el dato en :
  int index = data.indexOf(':');

  // revisar si valor valido
  if (index != -1) {
    String servoName = data.substring(0, index);  // Extraer nombre de servo
    String angleString = data.substring(index + 1); // Extraer valor de angulo

    int angle = angleString.toInt(); // convertir valor de angulo a Int

    // controlar servo dependiendo del nombre SLIDER
    if (servoName.equalsIgnoreCase("servo1")) {
      servo_Base.setupEase(angle, 3000);
    } else if (servoName.equalsIgnoreCase("servo2")) {
      servo_Brazo1.setupEase(angle, 3000);
    } else if (servoName.equalsIgnoreCase("servo3")) {
      servo_Brazo2.setupEase(angle, 3000);
    } else if (servoName.equalsIgnoreCase("servo4")) {
      servo_Brazo3.setupEase(angle, 3000);
    } else if (servoName.equalsIgnoreCase("servo5")) {
      servo_Brazo4.setupEase(angle, 3000);
    } else if (servoName.equalsIgnoreCase("servo6")) {
      servo_Gripper.setupEase(angle, 3000);
    }

    else {
      // si valor invalido
      Serial.println("Invalid servo name");
    }
  } else {
    //si formato de dato serial no es valido
    Serial.println("Invalid data format: Expected 'servo1:angle' or 'servo2:angle'");
  }
}

void readSerialButton() {
   if (Serial.available()) {
    inputString = Serial.readStringUntil('\n'); // Read a line until newline
    inputString.trim(); // Remove leading and trailing whitespace

    if (inputString.equalsIgnoreCase("grip")) {
      servo_Base.setupEase(0, 3000);
      servo_Brazo1.setupEase(70, 3000);
      servo_Brazo2.setupEase(30, 3000);
      servo_Brazo3.setupEase(30, 3000);
      servo_Brazo4.setupEase(30, 3000);
      servo_Gripper.setupEase(0, 3000);
   } 

   else if (inputString.equalsIgnoreCase("move")) { 
      servo_Gripper.setupEase(0, 3000);
      delay(3000);
      servo_Gripper.setupEase(150, 3000);


   } else if (inputString.equalsIgnoreCase("updown")) {
      
      servo_Brazo1.setupEase(90, 3000);
      servo_Brazo2.setupEase(0, 3000);
      servo_Brazo3.setupEase(0, 3000);
      servo_Brazo4.setupEase(90, 3000);
      delay(5000);
      servo_Brazo1.setupEase(10, 3000);
      servo_Brazo2.setupEase(0, 3000);
      servo_Brazo3.setupEase(0, 3000);
      servo_Brazo4.setupEase(90, 3000); 

   } else if (inputString.equalsIgnoreCase("side")) {
      servo_Base.setupEase(0, 3000);
      delay(3000);
      servo_Base.setupEase(180, 3000);
   }

   servo_Base.updatePosition();
   servo_Brazo1.updatePosition();
 }
}


 /*/acciones botones GUI

      //Grip
      else if (servoName.equalsIgnoreCase("servo6")) {
      servo_Base.setupEase(angle, 3000);
      servo_Brazo1.setupEase(angle, 3000);
      servo_Brazo2.setupEase(angle, 3000);
      servo_Brazo3.setupEase(angle, 3000);
      servo_Brazo4.setupEase(angle, 3000);
      servo_Gripper.setupEase(angle, 3000);
      
      }

      //move
      else if (servoName.equalsIgnoreCase("servo6")) {
      servo_Base.setupEase(angle, 3000);
      servo_Brazo1.setupEase(angle, 3000);
      servo_Brazo2.setupEase(angle, 3000);
      servo_Brazo3.setupEase(angle, 3000);
      servo_Brazo4.setupEase(angle, 3000);
      servo_Gripper.setupEase(angle, 3000);
      }

      //updown
      else if (servoName.equalsIgnoreCase("servo6")) {
      servo_Base.setupEase(angle, 3000);
      servo_Brazo1.setupEase(angle, 3000);
      servo_Brazo2.setupEase(angle, 3000);
      servo_Brazo3.setupEase(angle, 3000);
      servo_Brazo4.setupEase(angle, 3000);
      servo_Gripper.setupEase(angle, 3000);
      }

      //side
      else if (servoName.equalsIgnoreCase("servo6")) {
      servo_Base.setupEase(angle, 3000);
      servo_Brazo1.setupEase(angle, 3000);
      servo_Brazo2.setupEase(angle, 3000);
      servo_Brazo3.setupEase(angle, 3000);
      servo_Brazo4.setupEase(angle, 3000);
      servo_Gripper.setupEase(angle, 3000);
      }
      
      */