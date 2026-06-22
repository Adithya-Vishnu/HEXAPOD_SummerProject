#include<stdio.h>

int main(){
    char str[12];
    fgets(str,12,stdin);
    printf("%s",str);
}