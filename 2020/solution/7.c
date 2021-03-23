#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void maxCheck(int tree[], int num){
    for(int i = num; i>0; i--){
        if (tree[i] > tree[i/2]){
            printf("최대힙이 아닙니다.\n");
            return;
        }
    }
    printf("최대힙입니다.\n");
}

void minCheck(int tree[], int num){
    for(int i = num; i>0; i--){
        if (tree[i] < tree[i/2]){
            printf("최소힙이 아닙니다.\n");
            return;
        }
    }
    printf("최소힙입니다.\n");
}

int main()
{
    int tree[] = {0,1,2,3,4};
    maxCheck(tree, sizeof(tree)/sizeof(int));
    minCheck(tree, sizeof(tree)/sizeof(int));
}
