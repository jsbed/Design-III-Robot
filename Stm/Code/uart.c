#include "uart.h"
#include "stm32f4xx_gpio.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "stm32f4_discovery.h"

#define MAX_STRLEN 11 
#define NUM_LEDS 9

extern int compteurDeLettre;
extern double distance;
extern double degre;
extern int mesure;
extern int flagAsservir;
extern int flagDegre;
extern int flagLed;
extern int resetAllLeds;
extern int leds[NUM_LEDS];
extern int redLed;
char received_string[MAX_STRLEN+1]; 

/*
 * Initialisation du UART pour communication avec le pc
*/
void USART1_init(uint32_t baudrate){
	
	GPIO_InitTypeDef GPIO_InitStruct; 
	USART_InitTypeDef USART_InitStruct;
	NVIC_InitTypeDef NVIC_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1, ENABLE);
	
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOB, ENABLE);
	
	GPIO_InitStruct.GPIO_Pin = GPIO_Pin_6 | GPIO_Pin_7; // Pins 6 (TX) et 7 (RX)
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_AF;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStruct.GPIO_PuPd = GPIO_PuPd_UP;
	GPIO_Init(GPIOB, &GPIO_InitStruct);	
	
	GPIO_PinAFConfig(GPIOB, GPIO_PinSource6, GPIO_AF_USART1); //
	GPIO_PinAFConfig(GPIOB, GPIO_PinSource7, GPIO_AF_USART1);
	
        USART_InitStruct.USART_BaudRate = baudrate;
	USART_InitStruct.USART_WordLength = USART_WordLength_8b;// 8bits
	USART_InitStruct.USART_StopBits = USART_StopBits_1;//stopbit
	USART_InitStruct.USART_Parity = USART_Parity_No;
	USART_InitStruct.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
	USART_InitStruct.USART_Mode = USART_Mode_Tx | USART_Mode_Rx;
	USART_Init(USART1, &USART_InitStruct);
	
	USART_ITConfig(USART1, USART_IT_RXNE, ENABLE); // interrupt
	
	NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);		

	USART_Cmd(USART1, ENABLE);
}

/*
 * Fonction pour effacer la commande recue
*/
void EffaceCommande(void){
  int i;
  
  for(i = 0; i < MAX_STRLEN+1; i++){
      received_string[i] = '\0';
  }
}


/*******************************************************************************  
      COMMANDES                 PARAM
      (GO): avance              (X)(Y)? ou (vitesse1,vitesse2,v3,v4)?
      (BA)CK: arriere (recule)  (X)(Y)? ou ( ",",",")?
      (DI)AGONAL : en diagonale (X)(Y)? ou ( ",",",")?
      (RO)TATE: rotation        (DEG)?
      (ST)OP : arrêter          (-NONE-)
      (FL)ASH: flash led        (BLACK)?
      (LI)GTH: allume led       (<RGBs>)?
      (FI)NISH: fin             (-NONE-)
      (OF)F : éteindre LED      (<Leds>)?
*******************************************************************************/  
void CommandeUart(void){
  
  //Avancer (GO) - V1,V2,[V3,V4]
  if(received_string[0] == 'G' && received_string[1] == 'O'){
   
    int j = 0;
    char dist[4];
    resetValues();
    
    for(j = 8; j < 12; j++) {
       dist[j-8] = received_string[j];
    }
    distance = atof(dist);

    ResetPinRoues();
    GPIO_SetBits(GPIOD, GPIO_Pin_7);
    GPIO_SetBits(GPIOD, GPIO_Pin_4);

    mesure = 1;
    
    EffaceCommande();
    //USART_puts(USART1, "GO");
    flagAsservir = 1;
    compteurDeLettre = 0;
    return;
  }
  
  //Reculer (BA)CK - x[5]distance[4]
  else if(received_string[0] == 'B' && received_string[1] == 'A'){
  
    int j = 0;
    char dist[4];
    resetValues();
    
    for(j = 8; j < 12; j++) {
      dist[j-8] = received_string[j];
    }
    //dist[4] = '\0';
    distance = atof(dist);
    mesure = 1;
    
    ResetPinRoues();
    GPIO_SetBits(GPIOD, GPIO_Pin_3);
    GPIO_SetBits(GPIOB, GPIO_Pin_3);
    
    EffaceCommande();
    //USART_puts(USART1, "BA");
    flagAsservir = 1;
    compteurDeLettre = 0;
    return;
  }
  
  //Aller vers la droite (RI)GHT - x[5]distance[4]
  else if(received_string[0] == 'R' && received_string[1] == 'I'){

    int j = 0;
    char dist[4];
    resetValues();
    
    for(j = 8; j < 12; j++) {
      dist[j-8] = received_string[j];
    }
    //dist[4] = '\0';
    distance = atof(dist);

    mesure = 2;
    
    ResetPinRoues();
    GPIO_SetBits(GPIOD, GPIO_Pin_1);
    GPIO_SetBits(GPIOD, GPIO_Pin_6);
 
    EffaceCommande();
    //USART_puts(USART1, "RI");
    flagAsservir = 1;
    compteurDeLettre = 0;
    return;
  }
  
  //Aller vers la gauche (LE)FT - x[5]distance[4]
  else if(received_string[0] == 'L' && received_string[1] == 'E'){
    
    int j = 0;
    char dist[4];
    resetValues();
    
    for(j = 8; j < 12; j++) {
      dist[j-8] = received_string[j];
    }
    //dist[4] = '\0';
    distance = atof(dist);
    
    mesure = 2;
    
    ResetPinRoues();
    GPIO_SetBits(GPIOD, GPIO_Pin_5);
    GPIO_SetBits(GPIOD, GPIO_Pin_0);
    
    EffaceCommande();
    //USART_puts(USART1, "LE");
    flagAsservir = 1;
    compteurDeLettre = 0;
    return;
  }
  
  //Aller en diagonale (DI)AGONAL - V1,V2,V3,V4
  else if(received_string[0] == 'D' && received_string[1] == 'I'){
    GPIO_ResetBits(GPIOD, GPIO_Pin_12);
    GPIO_ResetBits(GPIOD, GPIO_Pin_13);
    EffaceCommande();
    USART_puts(USART1, "DI");
    flagAsservir = 1;
    return;
  }
  
  //Arrêter le déplacement (ST)OP - [None]
  else if(received_string[0] == 'S' && received_string[1] == 'T'){
    resetValues();
    ResetPinRoues();
    EffaceCommande();
    USART_puts(USART1, "ST");
    compteurDeLettre = 0;
    return;
  }
  
  //Faire tourner (RO)TATE - [(R)IGHT/(L)EFT - degree]
  else if(received_string[0] == 'R' && received_string[1] == 'O'){
    
    int j = 0;
    char deg[4];
    resetValues();
    
    for(j = 8; j < 12; j++) {
      deg[j-8] = received_string[j];
    }
    degre = atof(deg);
    mesure = 3;
    ResetPinRoues();
    
    if(received_string[2] == 'L'){
      GPIO_SetBits(GPIOD, GPIO_Pin_6);
      GPIO_SetBits(GPIOD, GPIO_Pin_4);
      GPIO_SetBits(GPIOD, GPIO_Pin_0);
      GPIO_SetBits(GPIOB, GPIO_Pin_3);
    }
    
   if(received_string[2] == 'R'){
      GPIO_SetBits(GPIOD, GPIO_Pin_7);
      GPIO_SetBits(GPIOD, GPIO_Pin_5);
      GPIO_SetBits(GPIOD, GPIO_Pin_3);
      GPIO_SetBits(GPIOD, GPIO_Pin_1);
    }
    
    EffaceCommande();
    //USART_puts(USART1, "RO");
    flagDegre = 1;
    compteurDeLettre = 0;
    return;
  }
  
    //LEDs
  else if(received_string[0] == 'F' ){
    
   char c1[2], c2[2], c3[2], c4[2], c5[2], c6[2], c7[2], c8[2], c9[2], c10[2];
    
    if(strcmp(received_string, "F0000000000") == 0){
      resetAllLeds = 1;
    }
    
    c1[0] = received_string[1];
    c2[0] = received_string[2];
    c3[0] = received_string[3];
    c4[0] = received_string[4];
    c5[0] = received_string[5];
    c6[0] = received_string[6];
    c7[0] = received_string[7];
    c8[0] = received_string[8];
    c9[0] = received_string[9];
    c10[0] = received_string[10];
    
    leds[0] = atoi(c1);
    leds[1] = atoi(c2);//c6
    leds[2] = atoi(c3);
    leds[3] = atoi(c4);
    leds[4] = atoi(c5);
    leds[5] = atoi(c6);//c2
    leds[6] = atoi(c7);
    leds[7] = atoi(c8);
    leds[8] = atoi(c9);
    redLed = atoi(c10);
    
    flagLed = 1;
    EffaceCommande();
    compteurDeLettre = 0;
    return;
  }
  
}

/*
 * Fonction qui envoie une réponse au pc
*/
void USART_puts(USART_TypeDef* USARTx, volatile char *s){

	while(*s){
		while( !(USARTx->SR & 0x00000040) ); 
		USART_SendData(USARTx, *s);
		*s++;
	}
}
