#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
   int c, a, v;
   scanf("%i %i", &c, &a);
   v = a / c;
   v = v + 1;
   printf("%i", v);
   return 0;
}