int relevador = 13;
int ENA = 3;
int in1 = 5;
int in2 = 6;
int LDR = A0;
int Pin_echo = 12; 
int Pin_trig = 11; 
void setup() {
  //put your setup code here, to run once:
  pinMode(relevador, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
  Serial.begin (9600); 
  pinMode(Pin_trig, OUTPUT); 
  pinMode(Pin_echo, INPUT); 
}
int estado = 0;
 int pulso, cm; 
void loop() {
  // put your main code here, to run repeatedly:

   estado = Serial.readString().toInt();

  if(estado == 1){
   
    int v = analogRead(LDR);
    digitalWrite(relevador, v);
      if (v <= 341){
        Serial.println("Detenerse");
        digitalWrite(in1, 0);
        digitalWrite(in2, 0);
        analogWrite(ENA, 0);
      }
      else if(v>341 && v<= 682){
        Serial.println("Girar Izquierda");
        digitalWrite(in1, 0);
        digitalWrite(in2, 1);
        analogWrite(ENA, 255);
      }
      else if (v >383 && v>=1023){
        Serial.println("Girar Derecha");      
        digitalWrite(i n1, 1);
        digitalWrite(in2, 0);
        analogWrite(ENA, 255);
      }
      else{
        Serial.println("Movimiento no valido!");
      }
    
    
  }else if(estado == 2){
    digitalWrite(Pin_trig, LOW); 
  delayMicroseconds(2); 
  digitalWrite(Pin_trig, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(Pin_trig, LOW); 
  
  pulso = pulseIn(Pin_echo, HIGH); 
  cm = pulso / 29 / 2;             
  Serial.println("Distancia:" + String(cm) + "cm."); 
  }

  delay(100);

}