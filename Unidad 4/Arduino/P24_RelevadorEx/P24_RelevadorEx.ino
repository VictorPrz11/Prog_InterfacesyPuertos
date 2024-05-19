int relevador=13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relevador,OUTPUT);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    digitalWrite(relevador,v);
    Serial.println("Estado aplicado: "+String(v));
  }
  delay(100);
}
