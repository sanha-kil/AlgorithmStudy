#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int data[]={1,2,3,4,5};
int flag[]={0,0,0,0,0};


void powerset(int n,int depth)
{
    int count = 0;
    for(int i = 0; i < n; i++){
        if (flag[i]==1)
            count += 1;
    }
    if(n == depth){
        if(count==3) {
        for(int i=0; i<n; i++){
            if(flag[i]==1)
                printf("%d ",data[i]);
            }
            printf("\n");
        }
        return;
    }
    count = 0;
    
    flag[depth]=1;
    powerset(n,depth+1);
    flag[depth]=0;
    powerset(n,depth+1);
}

int main()
{
    powerset(sizeof(data)/sizeof(int),0);
    return 0;
}
