#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main(){
    int sq[5] = {1,3,5,2,4};
    int tmp;
    for(int i=0; i<5; i++){
        if(i == 0)
            tmp = sq[i];
        else if (tmp < sq[i])
            tmp = sq[i];
        else
            continue;
    }
    printf("리스트에서 가장 큰 수 : %d\n", tmp);
}
