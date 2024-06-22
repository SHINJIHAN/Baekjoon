import math

# 최소공배수 구하는 함수
def lcm(A, B):
    # 두 수의 곱을 최대공약수로 나누어 최소공배수를 계산
    return (A*B)//math.gcd(A, B)

# 케이스 횟수 입력
T = int(input())

# 케이스 처리
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
