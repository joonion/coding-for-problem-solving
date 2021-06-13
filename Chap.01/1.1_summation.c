#include <stdio.h>

int main() {
    int N, S, i;
    scanf("%d", &N);
    for (S = 0, i = 1; i <= N; i++)
        S += i;
    printf("%d\n", S);
}