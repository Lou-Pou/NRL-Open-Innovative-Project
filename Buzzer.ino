const int buzzer = 9;


void setup(){
 
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);

}

void loop(){

 if(Serial.available()>0)
 {
  if (Serial.read() <= 100)
    {
      tone(buzzer, 1000); 
      delay(1000);        
      noTone(buzzer);     
      delay(1000);        
    }
 }
}
