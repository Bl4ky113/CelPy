// Made By Bl4ky113

// Led
int led = 7;

// Bluetooth Input
char btInfo = 'f';
bool btResult = false;

void setup() {
  // Setup the Led
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);

  // General Setup
  Serial.begin(9600);
}

void loop() {
  btInfo = Serial.read();
  if (btInfo == 't') {
    btResult = true;
  } else if (btInfo == 'f') {
    btResult = false;
  }

  Serial.println(btInfo);

  switch (btResult) {
    case false:
      digitalWrite(led, LOW);
      break;
    
    case true:
      digitalWrite(led, HIGH);
      break;
  }
  delay(5000);
}