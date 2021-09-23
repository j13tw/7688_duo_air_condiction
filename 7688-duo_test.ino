#include <DHT.h>

#define DHTPIN 2     
#define DHTTYPE DHT22   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  // conntect to MT7688 MPU
  Serial1.begin(57600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    return;
  }
  Serial.print("{\"humi\": ");
  Serial.print(h);
  Serial.print(", \"temp\": ");
  Serial.print(t);
  Serial.println("}");
  Serial1.print("{\"humi\": ");
  Serial1.print(h);
  Serial1.print(", \"temp\": ");
  Serial1.print(t);
  Serial1.println("}");
  delay(1000);
}
