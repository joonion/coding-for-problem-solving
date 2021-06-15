#include <stdio.h>

int summation(int N) {
    if (N % 2 == 0)
        return (N / 2) * (N + 1);
    else
        return ((N + 1) / 2) * N;
}

int main() {
    int N, S;
    scanf("%d", &N);
    S = summation(N);
    printf("%d\n", S);
}
