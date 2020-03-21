#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
   int m, n;
   int gcd=1;
   scanf("%d %d",&m, &n);
   
   for(int i = 1; i <= m; i++){
    if(m%i==0){
       if(n%i==0)
           gcd=i;
    }
   }
    printf("%d",gcd);
    return 0; //main 문을 종료한다.
}
