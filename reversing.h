#ifndef DECRYPT_H
#define DECRYPT_H

#include <stdio.h>

void decrypt_and_print(char to_decryp[], int size) {
    

    for (int i = 0; i < size; i++) {
        to_decryp[i] -= (2 * i);
        to_decryp[i] ^= i;
        printf("%s\n", to_decryp);

    }

}

#endif // DECRYPT_H