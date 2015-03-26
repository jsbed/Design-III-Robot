/* Includes ------------------------------------------------------------------*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <misc.h>
#include "stm32f4xx_gpio.h"
#include "stm32f4xx_rcc.h"
#include "stm32f4xx_spi.h"
#include "stm32f4xx_tim.h"
#include "stm32f4_discovery.h"
#include "tlc_spi.h"

uint8_t tlc_GSData[NUM_TLCS * 24];

//Configure the clocks for the required modules
void init_Tlc_rcc(void){
    //Enable GPIO peripheral clocks
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA, ENABLE);
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOB, ENABLE);
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOC, ENABLE);
    RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOD, ENABLE);
    //Enable the Serial Peripheral Interface peripheral clocks
    RCC_APB1PeriphClockCmd(RCC_APB1Periph_SPI2, ENABLE);

   //Enable the timer peripheral clocks
    RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM5, ENABLE);
    RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM12, ENABLE);
}
    //Configure the GPIO Pins
void init_Tlc_pins(void){
   GPIO_InitTypeDef GPIO_InitStructure;
  
  //Timer5 Outputs (TLC5940 GSCLK)
  GPIO_InitStructure.GPIO_Pin = (GPIO_Pin_1);
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  //Connect Timers to the GPIO Pins
  GPIO_PinAFConfig(GPIOA, GPIO_PinSource1, GPIO_AF_TIM5);            //Connect TIM5 OC2 output to PortA Pin1 (GSCLK)
  
  //Timer12 Outputs (TLC5940 BLANK)
  GPIO_InitStructure.GPIO_Pin = (GPIO_Pin_14);
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIOB, &GPIO_InitStructure);
  //Connect Timers to the GPIO Pins
  GPIO_PinAFConfig(GPIOB, GPIO_PinSource14, GPIO_AF_TIM12);            //Connect TIM12 OC1 output to PortB Pin14 (BLANK)

  //TLC5940 XLAT Pin
  GPIO_InitStructure.GPIO_Pin = GPIO_XLAT_PIN;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIO_XLAT_PORT, &GPIO_InitStructure);

  //SPI2 Pins
  //    SCLK =    PB10
  //    NSS =     PB9
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9 | GPIO_Pin_10;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_2MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIOB, &GPIO_InitStructure);
  GPIO_PinAFConfig(GPIOB, GPIO_PinSource9, GPIO_AF_SPI2);
  GPIO_PinAFConfig(GPIOB, GPIO_PinSource10, GPIO_AF_SPI2);

  //    MISO =    PC2
  //    MOSI =    PC3
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2 | GPIO_Pin_3;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  GPIO_PinAFConfig(GPIOC, GPIO_PinSource2, GPIO_AF_SPI2);
  GPIO_PinAFConfig(GPIOC, GPIO_PinSource3, GPIO_AF_SPI2);
  

  /* GPIOD Configuration:  LED_ROUGE (PD10) */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP ;
  GPIO_Init(GPIOD, &GPIO_InitStructure);
  GPIO_ResetBits(GPIOD, GPIO_Pin_10);
}    
    //Initialise the SPI module
void init_Tlc_spi(void){
    SPI_InitTypeDef SPI_InitStructure;
    SPI_InitStructure.SPI_Direction = SPI_Direction_2Lines_FullDuplex;       //The SPI bus setup uses two lines, one for Rx and one for Tx
    SPI_InitStructure.SPI_Mode = SPI_Mode_Master;                                //STM32 is the master with the TLC5940s as slaves
    SPI_InitStructure.SPI_DataSize = SPI_DataSize_8b;                             //Use 8-bit data transfers
    SPI_InitStructure.SPI_CPOL = SPI_CPOL_Low;                                    //TLC5940 clock is low when idle
    SPI_InitStructure.SPI_CPHA = SPI_CPHA_1Edge;                                //TLC5940 uses first clock transition as the "capturing edge"
    SPI_InitStructure.SPI_NSS = SPI_NSS_Soft;                                        //Software slave-select operation
    SPI_InitStructure.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_8; //Set the prescaler
    SPI_InitStructure.SPI_FirstBit = SPI_FirstBit_MSB;                             //TLC5940 data is transferred MSB first
    SPI_InitStructure.SPI_CRCPolynomial = 0;                                          //No CRC used

    SPI_Init(SPI2, &SPI_InitStructure);                                                    //Initialise the SPI2 peripheral
    SPI_SSOutputCmd(SPI2, ENABLE);                                                 //Set the SS Pin as an Output (master mode)
    SPI_Cmd(SPI2, ENABLE); 
}

//Initialise the Nested Vectored Interrupt Controller
void init_Tlc_interrupt(void){
  
    NVIC_InitTypeDef NVIC_InitStructure;
    //Enable the TIM12 (BLANK) Interrupt
    NVIC_InitStructure.NVIC_IRQChannel = TIM8_BRK_TIM12_IRQn;
    NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
    NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
    NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
    NVIC_Init(&NVIC_InitStructure);
}

//Initalise the Timer Modules
void init_Tlc_timers(void){
    TIM_TimeBaseInitTypeDef TIM_BaseInitStructure;
    TIM_OCInitTypeDef TIM_OCInitStructure;

    //Deinitialise timer modules and the initialisation structures
    TIM_DeInit(TIM5);
    TIM_DeInit(TIM12);
    TIM_TimeBaseStructInit(&TIM_BaseInitStructure);
    TIM_OCStructInit(&TIM_OCInitStructure);

    //Setup the TIM5 to generate the 'master clock'
    TIM_BaseInitStructure.TIM_Period = 1;
    TIM_BaseInitStructure.TIM_Prescaler = (uint16_t) (((TIM_APB1_FREQ / TLC5940_GSCLK_FREQ)/4) - 1);    //Note that the division factor of 4 is due to the OC1 freq vs CK_INT freq
    TIM_BaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;
    TIM_BaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;
    TIM_TimeBaseInit(TIM5, &TIM_BaseInitStructure);
    //Configure Channel 2 Output Compare as the Trigger Output (used to generate the 'GSCLK' signal)
    TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_Toggle;
    TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
    TIM_OCInitStructure.TIM_Pulse = 1;
    TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
    TIM_OC2Init(TIM5, &TIM_OCInitStructure);
    TIM_OC2PreloadConfig(TIM5, TIM_OCPreload_Enable);

   //Setup the TIM12 base for a symmetrical counter with a maximum count specified as the 'GSCLK count' (effectively the TLC5940's greyscale resolution)
    TIM_BaseInitStructure.TIM_Period = TLC5940_GSCLK_COUNTS + TLC5940_BLANK_COUNT;                   //GSCLK overflow count (with 1 extra for the BLANK signal to 'block')
    TIM_BaseInitStructure.TIM_Prescaler = 1;
    TIM_BaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;
    TIM_BaseInitStructure.TIM_CounterMode = TIM_CounterMode_CenterAligned1;
    TIM_TimeBaseInit(TIM12, &TIM_BaseInitStructure);
    //Configure Channel 1 Output Compare as the Trigger Output (used as the clock signal by TIM12 to generate 'BLANK' pulses)
    TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;
    TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
    TIM_OCInitStructure.TIM_Pulse = TLC5940_BLANK_COUNT;
    TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
    TIM_OC1Init(TIM12, &TIM_OCInitStructure);
    TIM_OC1PreloadConfig(TIM12, TIM_OCPreload_Enable);

    //Configure TIM5 as a master timer
    TIM_SelectOutputTrigger(TIM5, TIM_TRGOSource_Update);        //TRGO is tied to the update of TIM5
    TIM_SelectMasterSlaveMode(TIM5, TIM_MasterSlaveMode_Enable); //TIM5 enabled as a master

   //Configure TIM12 as a slave
    TIM_SelectInputTrigger(TIM12, TIM_TS_ITR1); //TIM 9 12                                  //Set TIM12 (slave) to trigger off TIM5 (master)
    TIM_SelectSlaveMode(TIM12, TIM_SlaveMode_External1); //TIM 9 12                  //Use the master signal input as an 'external clock'

    //Configure the TIM12 module to interrupt at Capture/Compare 1 events (match on both up and down-counting)
    TIM_ITConfig(TIM12, TIM_IT_CC1, ENABLE);

    //Enable Timers 5 and 12
    TIM_Cmd(TIM12, ENABLE);
    TIM_Cmd(TIM5, ENABLE);
}

uint8_t SPI_send(uint8_t data){
       
	SPI2->DR = data; 
	while( !(SPI2->SR & SPI_I2S_FLAG_TXE) ); 
	while( !(SPI2->SR & SPI_I2S_FLAG_RXNE) ); 
	while( SPI2->SR & SPI_I2S_FLAG_BSY ); 
        
	return SPI2->DR; 
        
}

void tlc_clear(void)
{
    tlc_setAll(0);
}

/** Shifts in the data from the grayscale data array, #tlc_GSData.
    If data has already been shifted in this grayscale cycle, another call to
    update() will immediately return 1 without shifting in the new data.  To
    ensure that a call to update() does shift in new data, use
    \code while(Tlc.update()); \endcode
    or
    \code while(tlc_needXLAT); \endcode
    \returns 1 if there is data waiting to be latched, 0 if data was
             successfully shifted in */
uint8_t tlc_update(void)
{
    uint8_t *p = tlc_GSData;
    while (p < tlc_GSData + NUM_TLCS * 24) {
        SPI_send(*p++);
        SPI_send(*p++);
        SPI_send(*p++);
    }
   
    return 0;
}

/** Sets channel to value in the grayscale data array, #tlc_GSData.
    \param channel (0 to #NUM_TLCS * 16 - 1).  OUT0 of the first TLC is
           channel 0, OUT0 of the next TLC is channel 16, etc.
    \param value (0-4095).  The grayscale value, 4095 is maximum.
    \see get */
void tlc_set(uint8_t channel, uint16_t value)
{
    uint8_t index8 = (NUM_TLCS * 16 - 1) - channel;
    uint8_t *index12p = tlc_GSData + ((((uint16_t)index8) * 3) >> 1);
    if (index8 & 1) { // starts in the middle
                      // first 4 bits intact | 4 top bits of value
        *index12p = (*index12p & 0xF0) | (value >> 8);
                      // 8 lower bits of value
        *(++index12p) = value & 0xFF;
    } else { // starts clean
                      // 8 upper bits of value
        *(index12p++) = value >> 4;
                      // 4 lower bits of value | last 4 bits intact
        *index12p = ((uint8_t)(value << 4)) | (*index12p & 0xF);
    }
}

/** Gets the current grayscale value for a channel
    \param channel (0 to #NUM_TLCS * 16 - 1).  OUT0 of the first TLC is
           channel 0, OUT0 of the next TLC is channel 16, etc.
    \returns current grayscale value (0 - 4095) for channel
    \see set */
uint16_t tlc_get(uint8_t channel)
{
    uint8_t index8 = (NUM_TLCS * 16 - 1) - channel;
    uint8_t *index12p = tlc_GSData + ((((uint16_t)index8) * 3) >> 1);
    return (index8 & 1)? // starts in the middle
            (((uint16_t)(*index12p & 15)) << 8) | // upper 4 bits
            *(index12p + 1)                       // lower 8 bits
        : // starts clean
            (((uint16_t)(*index12p)) << 4) | // upper 8 bits
            ((*(index12p + 1) & 0xF0) >> 4); // lower 4 bits
}

/** Sets all channels to value.
    \param value grayscale value (0 - 4095) */
void tlc_setAll(uint16_t value)
{
    uint8_t firstByte = value >> 4;
    uint8_t secondByte = (value << 4) | (value >> 8);
    uint8_t *p = tlc_GSData;
    while (p < tlc_GSData + NUM_TLCS * 24) {
        *p++ = firstByte;
        *p++ = secondByte;
        *p++ = (uint8_t)value;
    }
}