#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    char painel[18];
    char painel_front[18][3] = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"};
    int contA = 0, contB = 0, contC = 0, cont = 0, aleatorio = 0;

    setbuf(stdout, 0);
    srand(time(0));

    while (contA != 6 || contB != 6 || contC != 6) {
        while(1)
        {
            aleatorio = rand() % 3;
            if (aleatorio == 0 && contA < 6) {
                painel[cont] = 'A';
                contA += 1;
                cont += 1;
                break;
            } else if (aleatorio == 1 && contB < 6) {
                painel[cont] = 'B';
                contB += 1;
                cont += 1;
                break;
            } else if (aleatorio == 2 && contC < 6) {
                painel[cont] = 'C';
                contC += 1;
                cont += 1;
                break;
            }
        }
    }

    int a = 0, b = 0, c = 0, numero = 0;
    char check = ' ';

    while(1){
        if(a == 6 || b == 6 || c == 6){
            break;
        }
        printf("ULTIMA LETRA TIRADA: %c\n",check);
        for(int i = 0; i < 18; i++){
            printf("%s ",painel_front[i]);
        }
        printf("\nA: %d",a);
        printf("\nB: %d",b);
        printf("\nC: %d",c);

        while(1) {
            printf("\nDigite um numero: ");
            scanf("%d", &numero);
            if (numero < 0 || numero > 17) {
                printf("\nDigite um numero que esteja no painel");
            } else if (painel[numero] == 'X') {
                printf("\nDigite um numero que nao foi escolhida");
            } else {
                break;
            }
        }
        if(painel[numero] == 'A'){
            strncpy(painel_front[numero],"A",2);
            check = 'A';
            a += 1;
        }else if(painel[numero] == 'B'){
            strncpy(painel_front[numero],"B",2);
            check = 'B';
            b += 1;
        }else if(painel[numero] == 'C') {
            strncpy(painel_front[numero],"C",2);
            check = 'C';
            c += 1;
        }
        painel[numero] = 'X';
        printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    }
    if(a == 6){
        printf("O vencedor da corrida foi: A");
    }else if(b == 6){
        printf("O vencedor da corrida foi: B");
    }else if(c == 6){
        printf("O vencedor da corrida foi: C");
    }
    scanf("%x");
    return 0;
}
