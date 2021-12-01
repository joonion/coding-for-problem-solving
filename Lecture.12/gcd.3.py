def gcd(N, M):
    if M == 0:
        return N
    else:
        return gcd(M, N % M)
    
N = int(input("정수를 입력: "))
M = int(input("정수를 입력: ")) 
print(gcd(N, M))   
