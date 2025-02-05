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

#endif // DECRYPT_H