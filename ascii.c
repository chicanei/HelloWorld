//印出由32到127的ASCII碼
#include <stdio.h>
int main(void){
    printf("0123456789abcdef\n");
    for(int i =2;i <=7;i++){
        for(int j =0; j<=15; j++){
            char c = i*16+j;
            printf("%c",c);
        }
        printf("\n");
    }
    return 0;
}
/--*
 0123456789abcdef
 !"#$%&'()*+,-./
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[\]^_
`abcdefghijklmno
pqrstuvwxyz{|}~
--*/
