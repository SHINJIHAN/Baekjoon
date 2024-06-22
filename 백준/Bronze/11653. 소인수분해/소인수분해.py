# 정수 N 입력
N = int(input())

# 2부터 N의 제곱근까지 순회
for i in range(2, int(N**0.5)+1):
    # N이 i에 나누어 떨어질 때까지 나누기
    while N % i == 0:
        # 소인수 출력
        print(i)
        # i에 나누어진 N으로 갱신
        N //= i

# N이 소인수가 되었을 때 출력
if N > 1:
    print(N)