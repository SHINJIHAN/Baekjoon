# 사용자로부터 정수 N을 입력받음
N = int(input())

# 피보나치 수열의 N번째 항을 계산하는 함수
def fibonacci(N):
    # N이 0일 경우, 0을 반환
    if N == 0:
        return 0
    # N이 1일 경우, 1을 반환
    elif N == 1:
        return 1

    # 피보나치 수열의 첫 두 항 초기화
    a, b = 0, 1

    # 2부터 N까지 반복하여 피보나치 수 계산
    for _ in range(2, N + 1):
        # a는 이전 항, b는 현재 항
        a, b = b, a + b

    # N번째 피보나치 수 반환
    return b

# 피보나치 수를 계산하고 출력
print(fibonacci(N))
