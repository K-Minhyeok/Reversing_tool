#ifndef DECRYPT_H
#define DECRYPT_H

#include <stdio.h>

void decrypt_and_print1(char to_decryp[], int size) {
    

    for (int i = 0; i < size; i++) {
        to_decryp[i] -= (2 * i);
        to_decryp[i] ^= i;
        printf("%s\n", to_decryp);

    }

}

void decrypt_and_print2(int to_decryp[]) {

//if ( ((unsigned __int8)(16 * *(_BYTE *)(a1 + i)& 0xF0) | ((int)*(unsigned __int8 *)(a1 + i) >> 4)) != byte_140003000[i] )

    for (int i = 0; i < 27; i++) {
        to_decryp[i]= ( (16*to_decryp[i]) & 0xF0 | (to_decryp[i]>>4) ) ;
        printf("%c", to_decryp[i]);

    }

}

void quiz20(int to_decryp[],int cmp_decryp[],int to_size, int cmp_size) {

//   if ( byte_140003020[*(unsigned __int8 *)(a1 + i)] != byte_140003000[i] )

    for (int i = 0; i < to_size; i++) {
        for(int j = 0 ; j<cmp_size;j++){
            if(to_decryp[i]==cmp_decryp[j]){
                // printf("%d , %d \n",i,j);
                printf("%c",j);
            }
        }

    }
}

void quiz22 (int to_decryp[]){

//    if ( (unsigned __int8)(-5 * *(_BYTE *)(a1 + i)) != byte_140003000[i] )

    for(int i=0; i< 21; i++){
        for (int j=0 ; j<255 ; j++){
            if(((0xFB * j) & 0xFF) == to_decryp[i]){
                printf("%c",j);
            }
        }

    }

}

void quiz517(char to_decryp[],int size){

    for(int j=0; j<100;j++){
        printf("%d:   ",j);
        for (int i=0;i<size;i++){
            if (to_decryp[i] == 'Z')  
            to_decryp[i] = 'A'; 
            else 
                to_decryp[i]++;
            printf("%c", to_decryp[i]);
        }
        printf("\n");
    }

}

void quiz559(char to_decryp[] , int size){
    for(int i=0; i<126; i++){
        printf("%d:   ",i);
        for (int j = 0 ; j<size;j++){
            printf("%c", to_decryp[j] ^ i);
        }
        printf("\n");

    }
}



#endif // DECRYPT_H