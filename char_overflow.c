//char表示範圍較小，容易溢位

#include <stdio.h>
int main(void){
    int i;
    scanf("%d", &i);
    char c =i;
    c++;
    i++;
    printf("c = %d\n", c);
    printf("i = %d\n", i);
    return 0;
}
//輸入127
/*
印出結果：
c = -128  
i = 128
char c 在127後溢位變成-128
int i 是整數，所以127後還是128
*/
