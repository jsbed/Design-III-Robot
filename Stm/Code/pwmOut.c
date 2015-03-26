/**
  ******************************************************************************
    ******************************************************************************
  */ 

/* Includes ------------------------------------------------------------------*/
//#include "pwmOut.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "stm32f4xx_gpio.h"
#include "stm32f4_discovery.h"
#include "pwmOut.h"

//Init des dutys***********
double CCR1_Val = 0;
double CCR2_Val = 0;
double CCR3_Val = 0;
double CCR4_Val = 0;
double duty1 = 0;
double duty2 = 0;
double duty3 = 0;
double duty4 = 0;
double dutyt1 = 200;
double dutyt2 = 200;
double dutyt3 = 200;
double dutyt4 = 200;
//*************************


//************* COnstante de temps
double Ts = 0.01;
//*******************

//Gain Rotation*********
double p1 =13;
double p2 =13;
double p3 =13;
double p4 =13;
double i1 = 0.01;
double i2 = 0.01;
double i3 = 0.01;
double i4 = 0.01;
double d1 = 10;
double d2 = 10;
double d3 = 10;
double d4 = 10;
//**********************

//Gain roue1 PID*********
double kp1 = 10.5;
double ki1 = 0.01;
double kd1 = 1;
//*****************

//Gain roue2 PID*********
double kp2 = 10;
double ki2 = 0.01;
double kd2 = 1;
//*****************

//Gain roue3 PID*********
double kp3 = 10;
double ki3 = 0.01;
double kd3 = 1;
//*****************

//Gain roue4 PID*********
double kp4 = 10;
double ki4 = 0.01;
double kd4 = 1;
//*****************


//**********Init des erreurs**********
double err1 = 0;
double dErr1 = 0;
double lastErr1 = 0;
double sumErr1 = 0;
double PIOutput1 = 0;
double lastPIOutput1 = 0;

double err2 = 0;
double dErr2 = 0;
double lastErr2 = 0;
double sumErr2 = 0;
double PIOutput2 = 0;
double lastPIOutput2 = 0;

double err3 = 0;
double dErr3 = 0;
double lastErr3 = 0;
double sumErr3 = 0;
double PIOutput3 = 0;
double lastPIOutput3 = 0;

double err4 = 0;
double dErr4 = 0;
double lastErr4 = 0;
double sumErr4 = 0;
double PIOutput4 = 0;
double lastPIOutput4 = 0;
//********************************************

//Precision dutys
uint16_t precision = 10;
uint16_t PrescalerValue = 0;


/*
* Avant :
 *Roue2-> PD6
 *Roue4-> PD0
 *
*Arriere :
 *Roue2-> PD5
 *Roue4-> PD1
 *
*Gauche :
 *Roue1-> PD7
 *Roue3-> PD3
 *
*Droite :
 *Roue1-> PB3
 *Roue3-> PD4
 */
void PinRoues_init(void){
  GPIO_InitTypeDef GPIO_InitStructure;
  
    /* GPIOB Configuration:  SetBitsRoue1 (PB3) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP ;
  GPIO_Init(GPIOB, &GPIO_InitStructure);
  GPIO_ResetBits(GPIOB, GPIO_Pin_3);
  
  /* GPIOD Configuration:  SetBitsRoue1 (PD7) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7 | GPIO_Pin_6 | GPIO_Pin_5 | GPIO_Pin_4 | GPIO_Pin_3 | GPIO_Pin_1 | GPIO_Pin_0;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP ;
  GPIO_Init(GPIOD, &GPIO_InitStructure);
  GPIO_ResetBits(GPIOD, GPIO_Pin_7 | GPIO_Pin_6 | GPIO_Pin_5 | GPIO_Pin_4 | GPIO_Pin_3 | GPIO_Pin_1 | GPIO_Pin_0);
}

void ResetPinRoues(void){
  GPIO_ResetBits(GPIOB, GPIO_Pin_3);
  GPIO_ResetBits(GPIOD, GPIO_Pin_7 | GPIO_Pin_6 | GPIO_Pin_5 | GPIO_Pin_4 | GPIO_Pin_3 | GPIO_Pin_1 | GPIO_Pin_0);
}

void PWM_init(void){
  
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;

  /* TIM Configuration */
  TIM4_Config();

  /* Compute the prescaler value */
  PrescalerValue = (uint16_t) ((SystemCoreClock /2) / (10000*precision)) - 1;

  /* Time base configuration */
  TIM_TimeBaseStructure.TIM_Period = 100*precision - 1;
  TIM_TimeBaseStructure.TIM_Prescaler = PrescalerValue;
  TIM_TimeBaseStructure.TIM_ClockDivision = 0;
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;

  TIM_TimeBaseInit(TIM4, &TIM_TimeBaseStructure);

  /* PWM1 Mode configuration: Channel1 */
  TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;
  TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OCInitStructure.TIM_Pulse = (uint16_t)(CCR1_Val*precision);
  TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;

  TIM_OC1Init(TIM4, &TIM_OCInitStructure);

  TIM_OC1PreloadConfig(TIM4, TIM_OCPreload_Enable);

  /* PWM1 Mode configuration: Channel2 */
  TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OCInitStructure.TIM_Pulse = (uint16_t)(CCR2_Val*precision);

  TIM_OC2Init(TIM4, &TIM_OCInitStructure);

  TIM_OC2PreloadConfig(TIM4, TIM_OCPreload_Enable);

  /* PWM1 Mode configuration: Channel3 */
  TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OCInitStructure.TIM_Pulse = (uint16_t)(CCR3_Val*precision);

  TIM_OC3Init(TIM4, &TIM_OCInitStructure);

  TIM_OC3PreloadConfig(TIM4, TIM_OCPreload_Enable);

  /* PWM1 Mode configuration: Channel4 */
  TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OCInitStructure.TIM_Pulse = (uint16_t)(CCR4_Val*precision);

  TIM_OC4Init(TIM4, &TIM_OCInitStructure);

  TIM_OC4PreloadConfig(TIM4, TIM_OCPreload_Enable);

  TIM_ARRPreloadConfig(TIM4, ENABLE);

  /* TIM4 enable counter */
  TIM_Cmd(TIM4, ENABLE);
}


/**
 *Param [in] = vitesse (ticks/période)
 *Param[out] = %Duty Cycle 
**/
void Asservir(int mesure1, int consigne1, int mesure2, int consigne2, int mesure3, int consigne3, int mesure4, int consigne4){

  /**************************PID-Vitesse_EMILE*******************/
  err1 = consigne1 - mesure1;
  sumErr1 += err1;
  dErr1 = err1 - lastErr1;
  PIOutput1 = (kp1*err1) + (ki1*sumErr1* Ts) + (kd1*dErr1/Ts);
  duty1 += PIOutput1;
  lastErr1 = err1;
  if(duty1 < 0){
    duty1 = 0;
  }
  else if(duty1>((100*precision)*precision)){
    duty1 = (100*precision)*precision;
  }

  err2 = consigne2 - mesure2;
  sumErr2 += err2;
  dErr2 = err2 - lastErr2;
  PIOutput2 = (kp2*err2) + (ki2*sumErr2* Ts) + (kd2*dErr2/Ts);
  duty2 += PIOutput2;
  lastErr2 = err2;
  if(duty2 < 0){
    duty2 = 0;
  }
  else if(duty2>((100*precision)*precision)){
    duty2 = (100*precision)*precision;
  }

  err3= consigne3 - mesure3;
  sumErr3 += err3;
  dErr3 = err3 - lastErr3;
  PIOutput3 = (kp3*err3) + (ki3*sumErr3* Ts) + (kd3*dErr3/Ts);
  duty3 += PIOutput3;
  lastErr3 = err3;
  if(duty3 < 0){
    duty3 = 0;
  }
  else if(duty3>((100*precision)*precision)){
    duty3 = (100*precision)*precision;
  }

  err4 = consigne4 - mesure4;
  sumErr4 += err4;
  dErr4 = err4 - lastErr4;
  PIOutput4 = (kp4*err4) + (ki4*sumErr4* Ts) + (kd4*dErr4/Ts);
  duty4 += PIOutput4;
  lastErr4 = err4;
  if(duty4 < 0){
    duty4 = 0;
  }
  else if(duty4>((100*precision)*precision)){
    duty4 = (100*precision)*precision;
  }
//************************************************Fin PID-Vitesse_EMILE
 
  TIM4->CCR1 = (uint16_t)(duty1/precision);
  TIM4->CCR2 = (uint16_t)(duty2/precision);
  TIM4->CCR3 = (uint16_t)(duty3/precision);
  TIM4->CCR4 = (uint16_t)(duty4/precision);
 
  TIM1->CNT = 0;
  TIM2->CNT = 0;
  TIM3->CNT = 0;
  TIM8->CNT = 0;
}

void Tourner(int mesure1, int consigne1, int mesure2, int consigne2, int mesure3, int consigne3, int mesure4, int consigne4){
    /**************************PID-Vitesse_EMILE*******************/
  err1 = consigne1 - mesure1;
  sumErr1 += err1;
  dErr1 = err1 - lastErr1;
  PIOutput1 = (p1*err1) + (i1*sumErr1* Ts) + (d1*dErr1/Ts);
  dutyt1 += PIOutput1;
  lastErr1 = err1;
  if(dutyt1 < 0){
    dutyt1 = 0;
  }
  else if(dutyt1>((100*precision)*precision)){
    dutyt1 = (100*precision)*precision;
  }

  err2 = consigne2 - mesure2;
  sumErr2 += err2;
  dErr2 = err2 - lastErr2;
  PIOutput2 = (p2*err2) + (i2*sumErr2* Ts) + (d2*dErr2/Ts);
  dutyt2 += PIOutput2;
  lastErr2 = err2;
  if(dutyt2 < 0){
    dutyt2 = 0;
  }
  else if(dutyt2>((100*precision)*precision)){
    dutyt2 = (100*precision)*precision;
  }

  err3= consigne3 - mesure3;
  sumErr3 += err3;
  dErr3 = err3 - lastErr3;
  PIOutput3 = (p3*err3) + (i3*sumErr3* Ts) + (d3*dErr3/Ts);
  dutyt3 += PIOutput3;
  lastErr3 = err3;
  if(dutyt3 < 0){
    dutyt3 = 0;
  }
  else if(dutyt3>((100*precision)*precision)){
    dutyt3 = (100*precision)*precision;
  }

  err4 = consigne4 - mesure4;
  sumErr4 += err4;
  dErr4 = err4 - lastErr4;
  PIOutput4 = (p4*err4) + (i4*sumErr4* Ts) + (d4*dErr4/Ts);
  dutyt4 += PIOutput4;
  lastErr4 = err4;
  if(dutyt4 < 0){
    dutyt4 = 0;
  }
  else if(dutyt4>((100*precision)*precision)){
    dutyt4 = (100*precision)*precision;
  }
//************************************************Fin PID-Vitesse_EMILE
 
  TIM4->CCR1 = (uint16_t)(dutyt1/precision);
  TIM4->CCR2 = (uint16_t)(dutyt2/precision);
  TIM4->CCR3 = (uint16_t)(dutyt3/precision);
  TIM4->CCR4 = (uint16_t)(dutyt4/precision);
 
  TIM1->CNT = 0;
  TIM2->CNT = 0;
  TIM3->CNT = 0;
  TIM8->CNT = 0;
//  
//  err1 = consigne1 - mesure1;
//  PIOutput1 = err1 * p1;
//  duty1 += PIOutput1 + 110;
//  if(duty1 < 0){
//  duty1 = 0;
//}
//else if(duty1>((100*precision)*precision)){
//  duty1 = (100*precision)*precision;
//}
//  
//
//  err2 = consigne2 - mesure2;
//  PIOutput2 = err2 * p2;
//  duty2 += PIOutput2 + 100;
//  if(duty2 < 0){
//  duty2 = 0;
//}
//else if(duty2>((100*precision)*precision)){
//  duty2 = (100*precision)*precision;
//}
//
//  err3 = consigne3 - mesure3;
//  PIOutput3 = err3 * p3;
//  duty3 += PIOutput3 + 100;
//  if(duty3 < 0){
//  duty3 = 0;
//}
//else if(duty3>((100*precision)*precision)){
//  duty3 = (100*precision)*precision;
//}
//
//  err4 = consigne4 - mesure4;
//  PIOutput4 = err4 * p4;
//  duty4 += PIOutput4 + 100;
//  if(duty4 < 0){
//  duty4 = 0;
//}
//else if(duty4>((100*precision)*precision)){
//  duty4 = (100*precision)*precision;
//}
//
//  TIM4->CCR1 = (uint16_t)(duty1/precision);
//  TIM4->CCR2 = (uint16_t)(duty2/precision);
//  TIM4->CCR3 = (uint16_t)(duty3/precision);
//  TIM4->CCR4 = (uint16_t)(duty4/precision);
// 
//  TIM1->CNT = 0;
//  TIM2->CNT = 0;
//  TIM3->CNT = 0;
//  TIM8->CNT = 0;
}


/**
  * Configuration TIM4
  * PWM (out) pour les roues
  */
void TIM4_Config(void){
  GPIO_InitTypeDef GPIO_InitStructure;

  /* TIM3 clock enable */
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);

  /* GPIOD clock enable */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOD, ENABLE);
  
  /* GPIOD Configuration: TIM4 CH1 (PD12), TIM4 CH2 (PD13), TIM4 CH3 (PD14) and TIM4 CH4 (PD15)*/
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12 | GPIO_Pin_13 | GPIO_Pin_14 | GPIO_Pin_15;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP ;
  GPIO_Init(GPIOD, &GPIO_InitStructure); 
  
  /* Connect TIM4 pins to AF2 */  
  GPIO_PinAFConfig(GPIOD, GPIO_PinSource12, GPIO_AF_TIM4);
  GPIO_PinAFConfig(GPIOD, GPIO_PinSource13, GPIO_AF_TIM4); 
  GPIO_PinAFConfig(GPIOD, GPIO_PinSource14, GPIO_AF_TIM4);
  GPIO_PinAFConfig(GPIOD, GPIO_PinSource15, GPIO_AF_TIM4); 
}


/**
  * Configuration TIM1 ETR
  * Compteur de rising edges
  * Timer configuré en mode ETR : Permet de l'incrémenter avec sa pin ETR (in)
 **/
void ExtPulseCounterR1(void){
  
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  
  /* GPIOE clock enable */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOE, ENABLE);
 
  /* TIM1 clock enable */
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_TIM1, ENABLE);
  
  /* GPIOE Configuration: TIM1 ETR (PE7) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF; 
  GPIO_Init(GPIOE, &GPIO_InitStructure);
 
    /* Connect TIM1 pins to AF */
  GPIO_PinAFConfig(GPIOE, GPIO_PinSource7, GPIO_AF_TIM1);

  TIM_TimeBaseStructure.TIM_Period = 10000;//À CHANGER' QUELLE EST LA VITESSE D'ECHANTILLONAGE VOULUE?
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM1, &TIM_TimeBaseStructure);
  
  TIM_ETRClockMode2Config(TIM1, TIM_ExtTRGPSC_OFF, TIM_ExtTRGPolarity_NonInverted, 0x00);
  
  TIM_Cmd(TIM1, ENABLE);
  TIM1->CNT = 0;
}

/**
  * Configuration TIM2 ETR
  * Compteur de rising edges
  * Timer configuré en mode ETR : Permet de l'incrémenter avec sa pin ETR (in)
 **/
void ExtPulseCounterR2(void){
  
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  
  /* GPIOD clock enable */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA, ENABLE);
 
  /* TIM4 clock enable */
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);
  
  /* GPIOA Configuration: TIM2 ETR (PA15) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF; 
  GPIO_Init(GPIOA, &GPIO_InitStructure);
 
    /* Connect TIM2 pins to AF */
  GPIO_PinAFConfig(GPIOA, GPIO_PinSource15, GPIO_AF_TIM2);

  TIM_TimeBaseStructure.TIM_Period = 10000;//À CHANGER' QUELLE EST LA VITESSE D'ECHANTILLONAGE VOULUE?
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM2, &TIM_TimeBaseStructure);
  
  TIM_ETRClockMode2Config(TIM2, TIM_ExtTRGPSC_OFF, TIM_ExtTRGPolarity_NonInverted, 0x00);
  
  TIM_Cmd(TIM2, ENABLE);
  TIM2->CNT = 0;

} 

/**
  * Configuration TIM3 ETR
  * Compteur de rising edges
  * Timer configuré en mode ETR : Permet de l'incrémenter avec sa pin ETR (in)
 **/
void ExtPulseCounterR3(void){
  
  GPIO_InitTypeDef GPIO_InitStructure;
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOD, ENABLE);

  GPIO_PinAFConfig(GPIOD, GPIO_PinSource2, GPIO_AF_TIM3); // PD2
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_Init(GPIOD, &GPIO_InitStructure);
  
  TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;

  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  TIM_TimeBaseInitStructure.TIM_Prescaler = 0;
  TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInitStructure.TIM_Period = 100000;
  TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;
  TIM_TimeBaseInit(TIM3, &TIM_TimeBaseInitStructure);

  TIM_ETRClockMode2Config(TIM3, TIM_ExtTRGPSC_OFF, TIM_ExtTRGPolarity_NonInverted, 0x00);

  TIM_Cmd(TIM3, ENABLE);
  
  //TIM4->CNT = 0;
} 

/**
  * Configuration TIM1 ETR
  * Compteur de rising edges
  * Timer configuré en mode ETR : Permet de l'incrémenter avec sa pin ETR (in)
 **/
void ExtPulseCounterR4(void){
  
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  
  /* GPIOA clock enable */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA, ENABLE);
 
  /* TIM8 clock enable */
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_TIM8, ENABLE);
  
  /* GPIOA Configuration: TIM8 ETR (PA0) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF; 
  GPIO_Init(GPIOA, &GPIO_InitStructure);
 
    /* Connect TIM8 pins to AF */
  GPIO_PinAFConfig(GPIOA, GPIO_PinSource0, GPIO_AF_TIM8);

  TIM_TimeBaseStructure.TIM_Period = 10000;//À CHANGER' QUELLE EST LA VITESSE D'ECHANTILLONAGE VOULUE?
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM8, &TIM_TimeBaseStructure);
  
  TIM_ETRClockMode2Config(TIM8, TIM_ExtTRGPSC_OFF, TIM_ExtTRGPolarity_NonInverted, 0x00);
  
  TIM_Cmd(TIM8, ENABLE);
  TIM8->CNT = 0;
}

void resetPWM(void){
 dutyt1 = 200;
 dutyt2 = 200;
 dutyt3 = 200;
 dutyt4 = 200;
  
  duty1 = 0;
  duty2 = 0;
  duty3 = 0;
  duty4 = 0;

 err1 = 0;
 dErr1 = 0;
 lastErr1 = 0;
 sumErr1 = 0;
 PIOutput1 = 0;
 lastPIOutput1 = 0;
 
 err2 = 0;
 dErr2 = 0;
 lastErr2 = 0;
 sumErr2 = 0;
 PIOutput2 = 0;
 lastPIOutput2 = 0;
 
 err3 = 0;
 dErr3 = 0;
 lastErr3 = 0;
 sumErr3 = 0;
 PIOutput3 = 0;
 lastPIOutput3 = 0;
 
 err4 = 0;
 dErr4 = 0;
 lastErr4 = 0;
 sumErr4 = 0;
 PIOutput4 = 0;
 lastPIOutput4 = 0;
 
 TIM4->CCR1 = 0;
 TIM4->CCR2 = 0;
 TIM4->CCR3 = 0;
 TIM4->CCR4 = 0;
 
  TIM1->CNT = 0;
  TIM2->CNT = 0;
  TIM3->CNT = 0;
  TIM8->CNT = 0;
 
}



#ifdef  USE_FULL_ASSERT

void assert_failed(uint8_t* file, uint32_t line)
{
  while (1)
  {}
}
#endif