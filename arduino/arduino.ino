#include <Servo.h>

char c;

Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(9);
  servo.write(93);
  servo.detach();
}

void loop(){
  servo.detach();
  if(Serial.available()){
    c = char(Serial.read());
    Serial.print(c);
    if(c == '0'){
      servo.attach(9);
      servo.write(93);
      delay(100);
      servo.write(180);
      delay(500);
      servo.write(93);
      delay(500);
      servo.detach();
    }
    else if(c == '1'){
      servo.attach(9);
      servo.write(93);
      delay(100);
      servo.write(0);
      delay(500);
      servo.write(93);
      delay(500);
      servo.detach();
    }
    c = "";
  }
}
