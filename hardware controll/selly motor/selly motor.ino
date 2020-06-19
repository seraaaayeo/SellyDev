// 모터 A
#define ENA 10 //PWM
#define INA1 9
#define INA2 8

//모터B 컨트롤
int IN3=5;
int IN4=4;

int Motor_speed=255;


void setup() {
  // PWM 제어핀 출력 설정
  pinMode(ENA,OUTPUT);

  // 방향 제어핀 출력 설정
  pinMode(INA1,OUTPUT);
  pinMode(INA2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);

}

void loop() {
  
  delay(40000);
  digitalWrite(INA1, HIGH);   
  digitalWrite(INA2, LOW);  
  analogWrite(ENA, Motor_speed);

  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);

}
