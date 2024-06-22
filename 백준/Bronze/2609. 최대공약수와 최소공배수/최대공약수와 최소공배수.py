import math

# 최소공배수 계산 함수
def lcm(A, B):
    return A * B // math.gcd(A, B)

# 최대공약수 계산 함수
def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))