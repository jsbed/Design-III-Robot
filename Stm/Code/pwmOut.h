#include "main.h"
#include "stm32f4xx_usart.h"


void TIM4_Config(void);
void PinRoues_init(void);
void ResetPinRoues(void);
void PWM_init(void);
void ExtPulseCounterR1(void);
void ExtPulseCounterR2(void);
void ExtPulseCounterR3(void);
void ExtPulseCounterR4(void);
void Asservir(int v1, int c1, int v2, int c2, int v3, int c3, int v4, int c4);
void Tourner(int v1, int c1, int v2, int c2, int v3, int c3, int v4, int c4);
void resetPWM(void);





