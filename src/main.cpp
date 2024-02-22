#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(0xF0F0F0F0E1LL);
}

void loop() {
  const char* message = "Hello, world!";
  radio.write(message, strlen(message));
  delay(1000);
}

void main() {
  setup();
  while (true) {
    loop();
  }
}
