/* == data format ==
left_stick;right_stick;ABC;buttons;stick_buttons

>> left_stick X:Y
X - 00-FF
Y - 00-FF

>> right_stick X:Y
Аналогично X:Y

>> ABC int
Передаётся A, B или C

>> buttons int
l_but + r_but*2

>> stick_buttons
l_stck_but + r_stck_but*2

X:Y;X:Y;ABC;l_but + r_but*2;l_stck_but + r_stck_but*2
*/

#define LJX A3
#define LJY A4
#define RJX A2
#define RJY A2
#define LSWBUT A5
#define RSWBUT A2

#define ABUT 1
#define RBUT 2
#define CBUT 3
#define BBUT 4
#define LBUT 5

void setup() {
  Serial.begin(115200);
  pinMode(LSWBUT, INPUT_PULLUP);
  pinMode(RSWBUT, INPUT_PULLUP);
  
  pinMode(LBUT, INPUT_PULLUP);
  pinMode(RBUT, INPUT_PULLUP);

} 

void loop() {
  char ABCresult = 'N';
  if (digitalRead(ABUT))
    ABCresult = 'A';
  else if (digitalRead(BBUT))
    ABCresult = 'B';
  else if (digitalRead(CBUT))
    ABCresult = 'C';

  char buffer [30];

  sprintf(buffer, "%X:%X;%X:%X;%c;%d;%d",
    analogRead(LJX),
    analogRead(LJY),
    analogRead(RJX),
    analogRead(RJY),
    ABCresult,
    !digitalRead(LBUT) + (!digitalRead(RBUT))*2,
    !digitalRead(LSWBUT) + (!digitalRead(RSWBUT))*2
  );
  Serial.println(buffer);
}