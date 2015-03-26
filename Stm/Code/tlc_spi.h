#include "stm32f4_discovery.h"
#include "main.h"

#define NUM_TLCS                2
#define GPIO_SCAN_PORT          GPIOA
#define GPIO_SCAN_PIN           GPIO_Pin_7
#define GPIO_XLAT_PORT          GPIOA
#define GPIO_XLAT_PIN           GPIO_Pin_5
#define GPIO_BLANK_PORT         GPIOA
#define GPIO_BLANK_PIN          GPIO_Pin_1

#define TLC5940_GSCLK_COUNTS    256               //GSCLK Counts between BLANK Pulses
#define TLC5940_GSCLK_FREQ      1000000           //GSCLK Frequency
#define TLC5940_BLANK_COUNT     50                //Padding to allow previous SCAN column’s positive supply rail to turn off before switching to the next column
#define TIM_APB1_FREQ           84000000          //Internal TIMx Clock frequency (CK_INT)

#define DISP_SCAN_FREQ          200                                                                                                                                                                           //Frequency of the SCAN signal
#define DISP_BLANK_CYCLE_LIMIT  ((((TLC5940_GSCLK_FREQ / (TLC5940_GSCLK_COUNTS + TLC5940_BLANK_COUNT)) / DISP_SCAN_FREQ) / 2) - 1)   //Number of BLANK cycles to count before SCANing

//fonctions:
void init_Tlc_rcc(void);
void init_Tlc_pins(void);
void init_Tlc_spi(void);
void init_Tlc_interrupt(void);
void init_Tlc_timers(void);

uint8_t SPI_send(uint8_t data);
void tlc_clear(void);
uint8_t tlc_update(void);
void tlc_set(uint8_t channel, uint16_t value);
uint16_t tlc_get(uint8_t channel);
void tlc_setAll(uint16_t value);





