/**
  ******************************************************************************
  * @file    Labo5/main.c 
  * @author  WJST-GL
  * @version V1.0.0
  * @date    decembre 2014
  * @brief   Main program body
  ******************************************************************************
   */ 

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f4_discovery.h"
#include "stm32f4xx_gpio.h"
#include "stm32f4xx.h"
#include "stm32f4xx_rcc.h"
#include "uart.h"
#include "pwmOut.h"
#include "tlc_spi.h"
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
     
#define LONG_TABLE 2310 // longueur table mm
#define LARG_TABLE 1110 // largeur table mm
#define CONSIGNE_MAX 30 // vitesse maximale en ticks
#define CONSIGNE_MED 20 // vitesse moyenne en ticks
#define CONSIGNE_MIN 10 // vitesse minimale en ticks
#define NUM_LEDS 9
     
#define TOUR 1600 // 1600 ticks/tour (rising edges)
#define CIRCONFERENCE 219.44 // diametre de la roue en mm
double tickParMm = (TOUR/CIRCONFERENCE); // ticks/mm
double mmParTick =  0.137;  // 0.137145; // mm/tick
double degreParTick =  0.0700288174;
double tickParDegre =  14.27996661;
short TimingDelay = 0;

/***
PWM
***/
int mesure1 = 0;
int mesure2 = 0;
int mesure3 = 0;
int mesure4 = 0;
uint16_t flagCounter = 0;
int flagAsservir = 0;
int flagDegre = 0;


/***
UART
****/
int compteurDeLettre = 0;
double distance = 0;
double degre = 0;
int mesure = 0;
int flagLed = 0;
int leds[NUM_LEDS] = {0,0,0, 0,0,0, 0,0,0};
int redLed = 0;

/***
LED
***/
bool flagResetLed = false;
int ledToFlash = 0;
int resetAllLeds = 0;
int cntMs = 0;
int cntLedTime = 0;

/***
FONCTION PRINCIPALE
***/
int main(void) {
  
  /***********SYSTICK_CONFIG***************
   *SystemFrequency/1000      1ms         *
   *SystemFrequency/100000    10us        *
   *SystemFrequency/1000000   1us         *
   *****************************************/
  if (SysTick_Config(SystemCoreClock / 100))
  {  
    while (1);
  }
  
   /**************
  INITIALISATIONS
  ***************/
  USART1_init(19200);
  PWM_init();
  PinRoues_init();
  ExtPulseCounterR1();
  ExtPulseCounterR2();
  ExtPulseCounterR3();
  ExtPulseCounterR4();
  init_Tlc_rcc();
  init_Tlc_pins();
  init_Tlc_spi();
  init_Tlc_interrupt();
  init_Tlc_timers();
  tlc_setAll(0);
  tlc_update();
  
  /****
  BOUCLE PRINCIPALE
  ****/ 
  while (1){
 
    if(compteurDeLettre == 11){
      CommandeUart();
     //compteurDeLettre = 0;
    }
    
    /*****
    BOUCLE D'ASSERVISSEMENT EN DISTANCE DANS LES QUATRE DIRECTIONS
    *****/
    if(flagCounter == 1 && flagAsservir == 1){
      mesure1 = TIM1->CNT;
      mesure2 = TIM2->CNT;
      mesure3 = TIM3->CNT;
      mesure4 = TIM8->CNT;
      distance = calculerDistance(mesure, distance);
     
      //Asservissement lorsque la distance est grande
      if(distance > 10){
        Asservir(mesure1, 8, mesure2, 8, mesure3, 8, mesure4, 8);
      }
      
      //Asservissement vers l'arrêt lorsque la consigne en position est presque atteinte
      else if(distance <= 10 && distance > 0){
        Asservir(mesure1, 0, mesure2, 0, mesure3, 0, mesure4, 0);
      }
      
      //Arrêt et renvoie OkDistance au PC embarqué
      else if(distance <= 0) {
        resetValues();
        ResetPinRoues();
        USART_puts(USART1, "Ok");
        flagAsservir = 0;
      }
      flagCounter = 0;
    }    //if flagCounter && flagAsservir

   
    if(flagCounter == 1 && flagDegre == 1){
      
      mesure1 = TIM1->CNT;
      mesure2 = TIM2->CNT;
      mesure3 = TIM3->CNT;
      mesure4 = TIM8->CNT;
      degre = calculerDegre(degre);
      
      if (degre > 2){
        Tourner(mesure1, 2, mesure2, 2, mesure3, 2, mesure4, 2);
      }
      
//      else if(degre <= 10 && degre > 5){
//        Tourner(mesure1, 2, mesure2, 2, mesure3, 2, mesure4, 2);
//      }
//      
//      else if(degre <= 45 && degre > 1){
//        Tourner(mesure1, 2, mesure2, 2, mesure3, 2, mesure4, 2);
//      }
      
      else if(degre <= 2 && degre > 0){
        Tourner(mesure1, 0, mesure2, 0, mesure3, 0, mesure4, 0);
      }
      
      else if(degre <= 0){
        resetValues();
        ResetPinRoues();
        USART_puts(USART1, "Ok");
        flagDegre = 0;
      }
      flagCounter = 0;
    }//if flagCounter && flagDegre
    
   
    if(flagLed){
      controlerLeds();
      flagLed = 0;
      USART_puts(USART1, "Ok");
    }
    
    if(ledToFlash && cntMs >= 50){
      flashLed();
      cntMs = 0;
    }
    
  } //While
} //Main

double calculerDistance(int mesure, double dist){
  int tmpMesure = 0;
  if(mesure == 1){ 
    tmpMesure = TIM1->CNT;
  }
  else if(mesure == 2){
    tmpMesure = TIM2->CNT;
  }
  else if(mesure == 3){
    tmpMesure = TIM3->CNT;
  }
  dist -= tmpMesure*mmParTick;
  return dist;
}

double calculerDegre(double deg){
  double tmpMesure = 0;
  tmpMesure = TIM2->CNT;
  deg -= tmpMesure*degreParTick;
  return deg;
  
}


void resetValues(void){
  distance = 0;
  degre = 0;
  mesure = 0;
  resetPWM();
}

/*
 * 0 = Éteinte
 * 1 = Rouge
 * 2 = Vert
 * 3 = Bleu
 * 4 = Jaune
 * 5 = Blanc
 * 6 = Noir
*/
void controlerLeds(void){
  
  int i = 0;
  if(resetAllLeds) {
    tlc_setAll(0);
    resetAllLeds = 0;
    ledToFlash = 0;
    tlc_update();
    GPIO_ResetBits(GPIOD, GPIO_Pin_10);
    return;
  }
  
  //Led Rouge
  if(redLed){
    GPIO_SetBits(GPIOD, GPIO_Pin_10);
  }
  if(redLed == 0){
    GPIO_ResetBits(GPIOD, GPIO_Pin_10);
  }
  
  //Drapeau
  for(i = 0; i < NUM_LEDS; i++)
  {
    if(leds[i] == 0){
      tlc_set(i*3, 0);
      tlc_set(i*3+1, 0);
      tlc_set(i*3+2, 0);
    }
    else if(leds[i] == 1){
      tlc_set(i*3, 4095);
      tlc_set(i*3+1, 0);
      tlc_set(i*3+2, 0);
    }
    else if(leds[i] == 2){
      tlc_set(i*3+1, 4095);
      tlc_set(i*3, 0);
      tlc_set(i*3+2, 0);
    }
    else if(leds[i] == 3){
      tlc_set(i*3+2, 4095);
      tlc_set(i*3, 0);
      tlc_set(i*3+1, 0);
    }
    else if(leds[i] == 4){
      tlc_set(i*3, 2000);
      tlc_set(i*3+1, 2000);
      tlc_set(i*3+2, 0);
    }
    else if(leds[i] == 5){
      tlc_set(i*3, 4000);
      tlc_set(i*3+1, 4000);
      tlc_set(i*3+2, 4000);
    }
    else if(leds[i] == 6){
      tlc_set(i*3, 4000);
      tlc_set(i*3+1, 4000);
      tlc_set(i*3+2, 4000);
      ledToFlash = 1;
    }
    
  }
  tlc_update();
}

//LedNoire
void flashLed(void){
  
  for(int i = 0; i<NUM_LEDS; i++){
      if(leds[i] == 6  && !flagResetLed){
        tlc_set(i*3, 4000);
        tlc_set(i*3+1, 4000);
        tlc_set(i*3+2, 4000);
      }
      if(leds[i] == 6  && flagResetLed){
        tlc_set(i*3, 0);
        tlc_set(i*3+1, 0);
        tlc_set(i*3+2, 0);
      }
  }
  tlc_update();
}

void Delay(__IO uint32_t nTime)
{   
  TimingDelay = nTime;
  while(TimingDelay != 0);
}

void TimingDelay_Decrement(void)
{  
  if (TimingDelay != 0)
  { 
    TimingDelay--;
  }
}

#ifdef  USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{ 
  while (1)
  {
  }
}
#endif