
/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

/* Includes ------------------------------------------------------------------*/
#include "stm32f4_discovery.h"

void USART_puts(USART_TypeDef* USARTx, volatile char *s);
void TimingDelay_Decrement(void);
void ResetPinRoues(void);
void Delay(__IO uint32_t nTime);
void CommandeUart();
double calculerDistance(int mesure, double dist);
double calculerDegre(double deg);
void resetValues(void);
void controlerLeds(void);
void flashLed(void);

#endif /* __MAIN_H */

/******************* (C) COPYRIGHT 2011 STMicroelectronics *****END OF FILE****/
