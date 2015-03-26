#include "main.h"
#include "stm32f4xx_usart.h"

#define TX      6
#define RX      7

void USART1_init(uint32_t baudrate);
void CommandeUart(void);
void USART_puts(USART_TypeDef* USARTx, volatile char *s);


