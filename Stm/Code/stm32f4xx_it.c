
/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_it.h"
#include "main.h"
#include "tlc_spi.h"
#include <stdbool.h>

      //uart
#define MAX_STRLEN 11
extern char received_string[MAX_STRLEN+1];
extern int compteurDeLettre;
//extern volatile uint8_t taille;
//extern int compteurDeLettre;

      //systick
//extern __IO uint32_t Tim5CCR1_Val;
extern uint16_t flagCounter;
extern int flagAsservir;
extern int flagDegre;
extern int cntLedTime;
extern int cntMs;
extern bool flagResetLed;

      //timer
uint16_t capture = 0;
extern __IO uint16_t CCR_Val;
extern uint16_t flag;

    //TLC
uint16_t dispBlankCycleCnt = 0; 

/******************************************************************************/
/*            Cortex-M3 Processor Exceptions Handlers                         */
/******************************************************************************/

/**
  * @brief   This function handles NMI exception.
  * @param  None
  * @retval None
  */
void NMI_Handler(void)
{
}

/**
  * @brief  This function handles Hard Fault exception.
  * @param  None
  * @retval None
  */
void HardFault_Handler(void)
{
  /* Go to infinite loop when Hard Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Memory Manage exception.
  * @param  None
  * @retval None
  */
void MemManage_Handler(void)
{
  /* Go to infinite loop when Memory Manage exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Bus Fault exception.
  * @param  None
  * @retval None
  */
void BusFault_Handler(void)
{
  /* Go to infinite loop when Bus Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Usage Fault exception.
  * @param  None
  * @retval None
  */
void UsageFault_Handler(void)
{
  /* Go to infinite loop when Usage Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles SVCall exception.
  * @param  None
  * @retval None
  */
void SVC_Handler(void)
{
}

/**
  * @brief  This function handles Debug Monitor exception.
  * @param  None
  * @retval None
  */
void DebugMon_Handler(void)
{
}

/**
  * @brief  This function handles PendSVC exception.
  * @param  None
  * @retval None
  */
void PendSV_Handler(void)
{
}


void EXTI4_IRQHandler(void){
   /* Make sure that interrupt flag is set */
  if (EXTI_GetITStatus(EXTI_Line4) != RESET) {
    USART_puts(USART1, "Switch");
    GPIO_ResetBits(GPIOC, GPIO_Pin_4);
    EXTI_ClearITPendingBit(EXTI_Line4);
  }
}

/**
  * Systick interrupt
  */
void SysTick_Handler(void)
{
if (flagCounter == 0 && (flagAsservir == 1 || flagDegre == 1)){
    flagCounter = 1;
  }
  
  TimingDelay_Decrement();
  cntLedTime++;
  cntMs++;
  
  if(cntLedTime == 50){
    flagResetLed = !flagResetLed;
    cntLedTime = 0;
  }
}

/**
  * Usart1 interrupt
  */
void USART1_IRQHandler(void){
	
	// RX interrupt
	if( USART_GetITStatus(USART1, USART_IT_RXNE) ){
          
          static uint8_t cnt = 0; // grandeur string
          char t = USART1->DR;          
          if( t != '\n' ){ 
            received_string[cnt] = t;
            cnt++;
            //taille += cnt;
            if(cnt == MAX_STRLEN) {
              cnt = 0;
            }
            compteurDeLettre++;
          }
          else{
            cnt = 0;
            USART_puts(USART1, received_string);
          }         
	}
        
}

/******************************************************************************/
/*            STM32F4xx Peripherals Interrupt Handlers                        */
/******************************************************************************/

void TIM8_BRK_TIM12_IRQHandler(void)
    {
        //TIM12 IRQ Handler Tasks:
        //All this should be performed within the window of the BLANK signal (TIM12 OC1) being high (not the full SPI transmission)

        if(TIM_GetFlagStatus(TIM12,TIM_IT_CC1))
        {
            //Clear the TIM12 CC1 interrupt bit
            TIM_ClearITPendingBit(TIM12, TIM_IT_CC1);

                //Check if we require a 'SCAN' update (XLAT pulse, SCAN toggle, and next transfer triggered)
                if(dispBlankCycleCnt++ >= DISP_BLANK_CYCLE_LIMIT)
                {
                    GPIO_SetBits(GPIO_XLAT_PORT, GPIO_XLAT_PIN);                //Set the XLAT pin
                    dispBlankCycleCnt = 0;                                      //Reset the counter

                    GPIO_ResetBits(GPIO_XLAT_PORT, GPIO_XLAT_PIN);              //Clear the XLAT pin

                }
        }
    }

/******************************************************************************/