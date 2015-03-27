#include "prehenseur.h"
#include "stm32f4xx_gpio.h"
#include "stm32f4_discovery.h"
#include "stm32f4xx.h"
#include "stm32f4xx_exti.h"
#include "stm32f4xx_syscfg.h"
#include <misc.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 *Fonction d'initialisation de pins en source d'interruptions externes
 */
void Exti_init(void){

    GPIO_InitTypeDef GPIO_InitStruct;
    EXTI_InitTypeDef EXTI_InitStruct;
    NVIC_InitTypeDef NVIC_InitStruct;
    
    /* Enable clock for GPIOC */
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOC, ENABLE);
    /* Enable clock for SYSCFG */
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_SYSCFG, ENABLE);
    
    /* Set pin as input */
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_IN;
    GPIO_InitStruct.GPIO_OType = GPIO_OType_PP;
    GPIO_InitStruct.GPIO_Pin = GPIO_Pin_4;
    GPIO_InitStruct.GPIO_PuPd = GPIO_PuPd_UP;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_100MHz;
    GPIO_Init(GPIOC, &GPIO_InitStruct);
    
    /* Tell system that you will use PC4 for EXTI_Line4 */
    SYSCFG_EXTILineConfig(EXTI_PortSourceGPIOD, EXTI_PinSource0);
    
    /* PD4 is connected to EXTI_Line4 */
    EXTI_InitStruct.EXTI_Line = EXTI_Line4;
    /* Enable interrupt */
    EXTI_InitStruct.EXTI_LineCmd = ENABLE;
    /* Interrupt mode */
    EXTI_InitStruct.EXTI_Mode = EXTI_Mode_Interrupt;
    /* Triggers on rising and falling edge */
    EXTI_InitStruct.EXTI_Trigger = EXTI_Trigger_Rising_Falling;
    /* Add to EXTI */
    EXTI_Init(&EXTI_InitStruct);
 
    /* Add IRQ vector to NVIC */
    /* PC4 is connected to EXTI_Line40, which has EXTI4_IRQn vector */
    NVIC_InitStruct.NVIC_IRQChannel = EXTI4_IRQn;
    /* Set priority */
    NVIC_InitStruct.NVIC_IRQChannelPreemptionPriority = 0x00;
    /* Set sub priority */
    NVIC_InitStruct.NVIC_IRQChannelSubPriority = 0x00;
    /* Enable interrupt */
    NVIC_InitStruct.NVIC_IRQChannelCmd = ENABLE;
    /* Add to NVIC */
    NVIC_Init(&NVIC_InitStruct);
}