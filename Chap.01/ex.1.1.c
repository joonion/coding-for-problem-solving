#include <stdio.h>

typedef unsigned long long LongInteger;

LongInteger summation(LongInteger N) {
    if (N % 2 == 0)
        return (N / 2) * (N + 1);
    else
        return ((N + 1) / 2) * N;
}

int main() {
    LongInteger N, S;
    scanf("%lld", &N);
    S = summation(N);
    printf("%lld\n", S);
}