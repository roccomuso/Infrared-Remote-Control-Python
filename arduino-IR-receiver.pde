#include <IRremote.h>

/*
Ricevitore infrarosso. (la parte frontale del ricevitore è quella con la mezza sfera).

primo piedino: è il segnale collegato al pin digitale 7. (è il primo piedino partendo da sinistra).
secondo piedino: è il GND, collegato ad una resistenza 330ohm e poi al pin GND. (piedino centrale).
terzo piedino: collegato a 5V (piedino a destra).

Sfrutta la libreria IRremote.h (non presente di default).
Sito con esempi di codice per la ricezione e l'invio: http://www.arcfn.com/2009/08/multi-protocol-infrared-remote-library.html

*/

int RECV_PIN = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume(); // Receive the next value
  }
}